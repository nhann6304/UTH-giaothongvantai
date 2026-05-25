import { GoogleGenerativeAI, SchemaType, type FunctionDeclaration } from '@google/generative-ai';
import * as fs from 'fs';
import * as path from 'path';
import { session } from './session';
import { apiGet, buildFilterParam, extractItems, extractTotal, login as apiLogin } from './tools/api';
import { browserLogin, screenshot } from './tools/browser';
import { verifyRows, type AppliedFilter } from './tools/verify';
import type { TargetConfig, ToolCallLog, BugReport } from './types';

function loadTarget(name: string): TargetConfig {
  const p = path.join(__dirname, 'targets', `${name}.json`);
  if (!fs.existsSync(p)) throw new Error(`Target config not found: ${name}`);
  const cfg: TargetConfig = JSON.parse(fs.readFileSync(p, 'utf8'));
  const ov = session.get().override;
  if (ov && ov.target === name) {
    if (ov.baseUrl) cfg.baseUrl = ov.baseUrl.replace(/\/$/, '');
    if (ov.frontendUrl) cfg.frontendUrl = ov.frontendUrl.replace(/\/$/, '');
    if (ov.loginPath) cfg.auth.loginPath = ov.loginPath;
  }
  return cfg;
}

const TOOLS: FunctionDeclaration[] = [
  {
    name: 'loginApi',
    description:
      'Đăng nhập trực tiếp qua API (POST tới loginPath của target, mặc định /api/v1/auth/login). Nhanh & ổn định hơn UI. Dùng cái này TRƯỚC. Lưu cookie session để các tool sau dùng.',
    parameters: {
      type: SchemaType.OBJECT,
      properties: {
        target: { type: SchemaType.STRING, description: 'tên file config trong src/targets, vd "autosocials"' },
        email: { type: SchemaType.STRING },
        password: { type: SchemaType.STRING },
      },
      required: ['target', 'email', 'password'],
    },
  },
  {
    name: 'loginBrowser',
    description:
      'Đăng nhập qua UI (Playwright) — chậm hơn nhưng test được flow thực tế của user. Chỉ dùng khi loginApi không work hoặc user yêu cầu manual flow.',
    parameters: {
      type: SchemaType.OBJECT,
      properties: {
        target: { type: SchemaType.STRING },
        email: { type: SchemaType.STRING },
        password: { type: SchemaType.STRING },
      },
      required: ['target', 'email', 'password'],
    },
  },
  {
    name: 'getModuleSchema',
    description:
      'Trả về danh sách filter field của 1 module (vd "users"): mỗi field có name, type, source (enum/api), enum values nếu có.',
    parameters: {
      type: SchemaType.OBJECT,
      properties: {
        module: { type: SchemaType.STRING, description: 'vd "users"' },
      },
      required: ['module'],
    },
  },
  {
    name: 'getFilterOptions',
    description:
      'Gọi GET /api/<module>/find-filter-options?fields=... để lấy options động (department, team, larks, ...). Trả về { field: [{value,label},...] }.',
    parameters: {
      type: SchemaType.OBJECT,
      properties: {
        module: { type: SchemaType.STRING },
        fields: {
          type: SchemaType.ARRAY,
          items: { type: SchemaType.STRING },
          description: 'list tên field muốn lấy option',
        },
      },
      required: ['module', 'fields'],
    },
  },
  {
    name: 'findMulti',
    description:
      'Gọi find-multi với filter + paging. Trả về { total, count, verify:{matched,mismatched,mismatchedSamples}, ids }. Tự verify khi có filters.',
    parameters: {
      type: SchemaType.OBJECT,
      properties: {
        module: { type: SchemaType.STRING },
        page: { type: SchemaType.NUMBER },
        limit: { type: SchemaType.NUMBER },
        filters: {
          type: SchemaType.ARRAY,
          description: 'mảng filter: {field, values?:[...], dateFrom?, dateTo?}',
          items: {
            type: SchemaType.OBJECT,
            properties: {
              field: { type: SchemaType.STRING },
              values: { type: SchemaType.ARRAY, items: { type: SchemaType.STRING } },
              dateFrom: { type: SchemaType.STRING },
              dateTo: { type: SchemaType.STRING },
            },
            required: ['field'],
          },
        },
      },
      required: ['module'],
    },
  },
  {
    name: 'screenshotPage',
    description:
      'Chụp screenshot trang FE hiện tại (cần đã loginBrowser trước). Trả về path file để đính kèm bug.',
    parameters: {
      type: SchemaType.OBJECT,
      properties: {
        label: { type: SchemaType.STRING },
      },
      required: ['label'],
    },
  },
  {
    name: 'reportBug',
    description:
      'Ghi nhận 1 bug đã phát hiện. CHỈ gọi khi đã verify thật sự — KHÔNG đoán mò. Truyền screenshotUrl nếu có ảnh kèm.',
    parameters: {
      type: SchemaType.OBJECT,
      properties: {
        severity: { type: SchemaType.STRING, description: 'LOW|MEDIUM|HIGH|CRITICAL' },
        title: { type: SchemaType.STRING },
        steps: { type: SchemaType.ARRAY, items: { type: SchemaType.STRING } },
        expected: { type: SchemaType.STRING },
        actual: { type: SchemaType.STRING },
        field: { type: SchemaType.STRING },
        screenshotUrl: { type: SchemaType.STRING, description: 'URL ảnh từ screenshotPage (vd /screenshots/xxx.png)' },
      },
      required: ['severity', 'title', 'steps', 'expected', 'actual'],
    },
  },
];

const SYSTEM = `Bạn là AI QA tester filter của web app. Trả lời ngắn gọn bằng tiếng Việt.

Flow:
1. loginApi TRƯỚC (404=loginPath sai, báo user; 401/403=sai pass, dừng).
2. getModuleSchema -> getFilterOptions (chỉ field cần) -> findMulti(filter). findMulti tự verify, đọc field "verify" trong response.
3. Nếu verify.mismatched > 0 -> reportBug (severity HIGH).
4. Module: users|departments|teams|roles|proxy|accountVpn|accountVps.
5. Không đoán bug — chỉ report khi verify cho data cụ thể. Không hardcode option của field source=api.
6. Tối đa 6 tool call/turn. Trả lời cuối: tóm tắt pass/fail ngắn.`;

export class ChatService {
  private _genai: GoogleGenerativeAI | null = null;
  private _model: ReturnType<GoogleGenerativeAI['getGenerativeModel']> | null = null;

  private getModel() {
    if (this._model) return this._model;
    const key = process.env.GEMINI_API_KEY;
    if (!key) throw new Error('GEMINI_API_KEY chưa set trong .env');
    this._genai = new GoogleGenerativeAI(key);
    const modelName = process.env.GEMINI_MODEL || 'gemini-2.5-flash-lite';
    this._model = this._genai.getGenerativeModel({
      model: modelName,
      systemInstruction: SYSTEM,
      tools: [{ functionDeclarations: TOOLS }],
      generationConfig: {
        temperature: 0.2,
        maxOutputTokens: 1024,
      },
    });
    return this._model;
  }

  async send(userMessage: string): Promise<{ reply: string; toolCalls: ToolCallLog[]; bugs: BugReport[] }> {
    const chat = this.getModel().startChat();
    let result = await chat.sendMessage(userMessage);
    const localToolCalls: ToolCallLog[] = [];

    let safety = 0;
    while (safety++ < 8) {
      const calls = result.response.functionCalls();
      if (!calls || calls.length === 0) break;

      const parts = [];
      for (const call of calls) {
        const execResult = await this.executeFunction(call.name, (call as any).args || {});
        const log: ToolCallLog = { name: call.name, args: (call as any).args || {}, result: execResult, ts: Date.now() };
        localToolCalls.push(log);
        session.pushTool(log);
        parts.push({
          functionResponse: { name: call.name, response: execResult as Record<string, unknown> },
        });
      }
      result = await chat.sendMessage(parts);
    }

    const text = result.response.text();
    return { reply: text, toolCalls: localToolCalls, bugs: session.get().bugs };
  }

  private async executeFunction(name: string, args: any): Promise<any> {
    try {
      switch (name) {
        case 'loginApi': {
          const target = loadTarget(args.target);
          const r = await apiLogin(target, args.email, args.password);
          if (r.ok) {
            session.setCtx({
              cookies: r.cookies,
              baseUrl: target.baseUrl,
              targetName: args.target,
            });
          }
          return { ok: r.ok, message: r.message };
        }
        case 'loginBrowser': {
          const target = loadTarget(args.target);
          const r = await browserLogin(target, args.email, args.password);
          if (r.ok) {
            session.setCtx({
              cookies: r.cookies,
              baseUrl: target.baseUrl,
              targetName: args.target,
            });
          }
          return { ok: r.ok, message: r.message };
        }
        case 'getModuleSchema': {
          const ctx = session.get().ctx;
          if (!ctx) return { error: 'Chưa login' };
          const target = loadTarget(ctx.targetName);
          const mod = target.modules[args.module];
          if (!mod) return { error: `Module "${args.module}" không có trong config` };
          return {
            label: mod.label,
            basePath: mod.basePath,
            fields: mod.filterFields,
          };
        }
        case 'getFilterOptions': {
          const ctx = session.get().ctx;
          if (!ctx) return { error: 'Chưa login' };
          const target = loadTarget(ctx.targetName);
          const mod = target.modules[args.module];
          if (!mod) return { error: `Module "${args.module}" không tồn tại` };
          const fields = (args.fields as string[]).join(',');
          const r = await apiGet(ctx, mod.basePath + mod.endpoints.findFilterOptions, { fields });
          if (r.status !== 200) return { error: `HTTP ${r.status}`, raw: String(r.raw).slice(0, 200) };
          const meta = r.data?.metadata || r.data || {};
          const slim: Record<string, any> = {};
          for (const k of Object.keys(meta)) {
            const v = meta[k];
            if (Array.isArray(v)) {
              slim[k] = {
                total: v.length,
                items: v.slice(0, 20).map((o: any) => ({
                  value: o.value ?? o.id ?? o._id,
                  label: o.label ?? o.name ?? o.title,
                })),
              };
            } else {
              slim[k] = v;
            }
          }
          return { status: r.status, options: slim };
        }
        case 'findMulti': {
          const ctx = session.get().ctx;
          if (!ctx) return { error: 'Chưa login' };
          const target = loadTarget(ctx.targetName);
          const mod = target.modules[args.module];
          if (!mod) return { error: `Module "${args.module}" không tồn tại` };
          const filtersParam = args.filters && args.filters.length ? buildFilterParam(args.filters) : undefined;
          const r = await apiGet(ctx, mod.basePath + mod.endpoints.findMulti, {
            page: args.page ?? 1,
            limit: args.limit ?? 20,
            filters: filtersParam,
          });
          if (r.status !== 200) return { error: `HTTP ${r.status}`, raw: String(r.raw).slice(0, 200) };
          const items = extractItems(r.data, target.responseShape.itemsPath);
          const total = extractTotal(r.data, target.responseShape.totalPath);
          const verify = args.filters && args.filters.length
            ? verifyRows(items, args.filters as AppliedFilter[], mod)
            : null;
          return {
            status: r.status,
            total,
            count: items.length,
            verify,
            ids: items.map((it: any) => it.id).slice(0, 20),
          };
        }
        case 'verifyResults': {
          return { error: 'verifyResults deprecated — findMulti đã tự verify khi có filters. Đọc field "verify" trong kết quả findMulti.' };
        }
        case 'screenshotPage': {
          const filePath = await screenshot(args.label || 'page');
          const fileName = path.basename(filePath);
          return { file: filePath, url: `/screenshots/${fileName}` };
        }
        case 'reportBug': {
          const id = 'bug_' + (session.get().bugs.length + 1);
          const bug: BugReport = {
            id,
            severity: args.severity,
            title: args.title,
            steps: args.steps,
            expected: args.expected,
            actual: args.actual,
            field: args.field,
            screenshotUrl: args.screenshotUrl,
          };
          session.pushBug(bug);
          return { ok: true, id };
        }
        default:
          return { error: `Unknown function: ${name}` };
      }
    } catch (err: any) {
      return { error: err?.message || String(err) };
    }
  }
}
