import type { SessionContext, TargetConfig } from '../types';

export async function login(
  target: TargetConfig,
  email: string,
  password: string,
): Promise<{ ok: boolean; cookies: string; message: string }> {
  const url = target.baseUrl + target.auth.loginPath;
  const body: Record<string, string> = {};
  body[target.auth.credentialsField.email] = email;
  body[target.auth.credentialsField.password] = password;

  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });

  const setCookie = res.headers.get('set-cookie') || '';
  const cookieJar = parseCookieHeader(setCookie, target.auth.cookieName);

  let text = '';
  try {
    text = await res.text();
  } catch {}

  return {
    ok: res.ok && !!cookieJar,
    cookies: cookieJar,
    message: res.ok ? 'login success' : `HTTP ${res.status}: ${text.slice(0, 200)}`,
  };
}

function parseCookieHeader(setCookie: string, name: string): string {
  // Node fetch trả về single header với multiple cookies separated by ", " — chỉ giữ pair name=value đầu của mỗi cookie
  if (!setCookie) return '';
  const parts = setCookie.split(/,(?=\s*\w+=)/);
  const collected: string[] = [];
  for (const p of parts) {
    const pair = p.trim().split(';')[0];
    if (!pair) continue;
    const [k] = pair.split('=');
    if (!k) continue;
    // chỉ giữ cookie có tên = name hoặc các cookie phụ (vd refresh-token)
    if (k === name || /token/i.test(k)) {
      collected.push(pair);
    }
  }
  return collected.join('; ');
}

export async function apiGet(
  ctx: SessionContext,
  path: string,
  query?: Record<string, string | number | undefined>,
): Promise<{ status: number; data: any; raw?: string }> {
  const url = new URL(ctx.baseUrl + path);
  if (query) {
    for (const [k, v] of Object.entries(query)) {
      if (v !== undefined && v !== null && v !== '') {
        url.searchParams.set(k, String(v));
      }
    }
  }
  const res = await fetch(url.toString(), {
    headers: ctx.cookies ? { Cookie: ctx.cookies } : {},
  });
  const text = await res.text();
  let data: any = null;
  try {
    data = JSON.parse(text);
  } catch {
    data = { raw: text };
  }
  return { status: res.status, data, raw: text.slice(0, 1000) };
}

export function buildFilterParam(filters: Array<{ field: string; values?: any[]; dateFrom?: string; dateTo?: string }>): string {
  const out = filters
    .map((f) => {
      if (f.dateFrom || f.dateTo) {
        return { f: f.field, o: { r: { vf: f.dateFrom, vt: f.dateTo } } };
      }
      if (f.values && f.values.length) {
        return { f: f.field, o: { in: { t: 'in', v: f.values } } };
      }
      return null;
    })
    .filter(Boolean);
  return JSON.stringify(out);
}

export function extractItems(data: any, itemsPath: string): any[] {
  const v = getByPath(data, itemsPath);
  return Array.isArray(v) ? v : [];
}

export function extractTotal(data: any, totalPath: string): number {
  const v = getByPath(data, totalPath);
  return typeof v === 'number' ? v : 0;
}

function getByPath(obj: any, path: string): any {
  return path.split('.').reduce((acc, key) => (acc == null ? acc : acc[key]), obj);
}
