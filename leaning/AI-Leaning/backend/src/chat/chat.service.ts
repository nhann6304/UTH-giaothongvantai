import { Injectable, OnModuleInit, Logger } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import {
  GoogleGenerativeAI,
  Tool,
  SchemaType,
  GenerativeModel,
} from '@google/generative-ai';
import { UserService } from '../user/user.service';
import { FilterService } from '../filter/filter.service';
import { ChatResponseDto, ToolCallTrace } from './chat.dto';

@Injectable()
export class ChatService implements OnModuleInit {
  private readonly logger = new Logger(ChatService.name);
  private genAI: GoogleGenerativeAI;
  private tools: Tool[];

  constructor(
    private readonly config: ConfigService,
    private readonly userService: UserService,
    private readonly filterService: FilterService,
  ) {}

  onModuleInit() {
    const apiKey = this.config.get<string>('GEMINI_API_KEY');
    if (!apiKey || apiKey === 'paste_your_api_key_here') {
      throw new Error(
        'GEMINI_API_KEY chưa được cấu hình. Hãy copy .env.example -> .env và dán API key.',
      );
    }
    this.genAI = new GoogleGenerativeAI(apiKey);

    // ====================================================================
    // KHAI BÁO TOOLS — chia 4 nhóm:
    //   1) Profile (demo cũ)
    //   2) Filter Discovery — AI hiểu schema & options
    //   3) Filter Action — AI thao tác như user
    //   4) Filter Verification + Bug Report — AI kiểm tra & báo bug
    // ====================================================================
    this.tools = [
      {
        functionDeclarations: [
          // ---------------- Profile (giữ nguyên demo gốc) ----------------
          {
            name: 'getUserProfile',
            description: 'Lấy hồ sơ user hiện tại đang đăng nhập (fullName, phone, email, address).',
            parameters: { type: SchemaType.OBJECT, properties: {} },
          },
          {
            name: 'updateUserProfile',
            description:
              'Cập nhật MỘT trường trong profile user (fullName / phone / email / address).',
            parameters: {
              type: SchemaType.OBJECT,
              properties: {
                field: { type: SchemaType.STRING, description: 'fullName | phone | email | address' },
                value: { type: SchemaType.STRING, description: 'Giá trị mới' },
              },
              required: ['field', 'value'],
            },
          },

          // ---------------- DISCOVERY ----------------
          {
            name: 'getFilterSchema',
            description:
              'Lấy schema toàn bộ filter của trang Users: tên trường, loại (select/date), và options khả dụng. Gọi đầu tiên để biết có những filter nào.',
            parameters: { type: SchemaType.OBJECT, properties: {} },
          },
          {
            name: 'getFilterOptions',
            description: 'Lấy danh sách options của 1 trường filter cụ thể (vd: gender → [Male, Female]).',
            parameters: {
              type: SchemaType.OBJECT,
              properties: {
                field: { type: SchemaType.STRING, description: 'Tên field, vd: gender, department, role...' },
              },
              required: ['field'],
            },
          },
          {
            name: 'getCurrentFilterState',
            description: 'Đọc trạng thái filter HIỆN TẠI (filter đang chọn + rows đang hiển thị).',
            parameters: { type: SchemaType.OBJECT, properties: {} },
          },

          // ---------------- ACTION ----------------
          {
            name: 'applyFilter',
            description:
              'Áp dụng filter mới (giống user click các Select rồi bấm Apply). Các field cùng giá trị mảng. Field bỏ qua = không filter trường đó.',
            parameters: {
              type: SchemaType.OBJECT,
              properties: {
                position: { type: SchemaType.ARRAY, items: { type: SchemaType.STRING } },
                statusUser: { type: SchemaType.ARRAY, items: { type: SchemaType.STRING } },
                gender: { type: SchemaType.ARRAY, items: { type: SchemaType.STRING } },
                hasPermission: { type: SchemaType.ARRAY, items: { type: SchemaType.STRING } },
                department: { type: SchemaType.ARRAY, items: { type: SchemaType.STRING } },
                team: { type: SchemaType.ARRAY, items: { type: SchemaType.STRING } },
                role: { type: SchemaType.ARRAY, items: { type: SchemaType.STRING } },
                createdBy: { type: SchemaType.ARRAY, items: { type: SchemaType.STRING } },
                createdAtStart: { type: SchemaType.STRING, description: 'ISO date, vd 2025-01-01' },
                createdAtEnd: { type: SchemaType.STRING, description: 'ISO date, vd 2025-12-31' },
              },
            },
          },
          {
            name: 'resetFilter',
            description: 'Bấm Reset All — xoá toàn bộ filter, quay về full list.',
            parameters: { type: SchemaType.OBJECT, properties: {} },
          },

          // ---------------- VERIFICATION ----------------
          {
            name: 'verifyResults',
            description:
              'Kiểm tra TỪNG row trong kết quả hiện tại có khớp filter đang áp dụng không. Trả về số match + danh sách mismatch + lý do. Đây là cách chính để PHÁT HIỆN BUG.',
            parameters: { type: SchemaType.OBJECT, properties: {} },
          },

          // ---------------- BUG REPORT ----------------
          {
            name: 'reportBug',
            description:
              'Ghi nhận 1 bug đã phát hiện. Chỉ gọi khi verifyResults cho thấy có vấn đề rõ ràng.',
            parameters: {
              type: SchemaType.OBJECT,
              properties: {
                severity: {
                  type: SchemaType.STRING,
                  description: 'CRITICAL | HIGH | MEDIUM | LOW',
                },
                title: { type: SchemaType.STRING, description: 'Tóm tắt bug 1 dòng' },
                steps: {
                  type: SchemaType.ARRAY,
                  items: { type: SchemaType.STRING },
                  description: 'Các bước repro',
                },
                expected: { type: SchemaType.STRING },
                actual: { type: SchemaType.STRING },
              },
              required: ['severity', 'title', 'steps', 'expected', 'actual'],
            },
          },
        ],
      },
    ];

    this.logger.log('Gemini client + tools đã sẵn sàng (Profile + QA Agent)');
  }

  async chat(userMessage: string): Promise<ChatResponseDto> {
    const model: GenerativeModel = this.genAI.getGenerativeModel({
      model: 'gemini-2.5-flash',
      systemInstruction:
        'Bạn là QA Agent tự động cho web admin. Bạn có thể: ' +
        '(1) cập nhật profile user, ' +
        '(2) khám phá schema filter của trang Users, ' +
        '(3) thao tác filter như user (applyFilter / resetFilter), ' +
        '(4) verifyResults để check row có khớp filter không, ' +
        '(5) reportBug khi phát hiện sai lệch. ' +
        'Khi user yêu cầu "test filter X", quy trình chuẩn của bạn là: ' +
        'getFilterSchema → applyFilter với từng option → verifyResults → nếu thấy mismatch (hoặc count bất thường như "filter chọn X nhưng vẫn full list") thì reportBug. ' +
        'Trả lời ngắn gọn bằng tiếng Việt, ghi rõ kết luận cuối cùng (PASS / FAIL / có bug gì).',
      tools: this.tools,
    });

    const chatSession = model.startChat();
    let result = await chatSession.sendMessage(userMessage);
    const toolCalls: ToolCallTrace[] = [];

    // Cho phép AI gọi tối đa 15 tool/loop — đủ để test 1 filter
    let safety = 0;
    while (safety++ < 15) {
      const calls = result.response.functionCalls();
      if (!calls || calls.length === 0) break;

      const parts = calls.map((call) => {
        const execResult = this.executeFunction(call.name, call.args);
        toolCalls.push({ name: call.name, args: call.args, result: execResult });
        this.logger.log(`Tool ${call.name} -> ${JSON.stringify(execResult).slice(0, 200)}`);
        return {
          functionResponse: { name: call.name, response: execResult },
        };
      });

      result = await chatSession.sendMessage(parts);
    }

    return {
      reply: result.response.text(),
      toolCalls,
      profile: this.userService.getProfile(),
      filterState: {
        filter: this.filterService.getState(),
        ...this.filterService.getResults(),
      },
      bugs: this.filterService.getBugs(),
    } as any;
  }

  private executeFunction(name: string, args: any) {
    try {
      switch (name) {
        // Profile
        case 'getUserProfile':
          return { success: true, data: this.userService.getProfile() };
        case 'updateUserProfile': {
          const updated = this.userService.updateField(args.field, args.value);
          return { success: true, message: `Đã đổi ${args.field}`, data: updated };
        }

        // Discovery
        case 'getFilterSchema':
          return { success: true, data: this.filterService.getSchema() };
        case 'getFilterOptions':
          return { success: true, field: args.field, options: this.filterService.getOptions(args.field) };
        case 'getCurrentFilterState':
          return {
            success: true,
            filter: this.filterService.getState(),
            ...this.filterService.getResults(),
          };

        // Action
        case 'applyFilter': {
          this.filterService.applyFilter(args || {});
          const { rows, total } = this.filterService.getResults();
          return {
            success: true,
            filterApplied: this.filterService.getState(),
            total,
            sample: rows.slice(0, 3),
          };
        }
        case 'resetFilter': {
          this.filterService.reset();
          const { total } = this.filterService.getResults();
          return { success: true, message: 'Đã reset filter', total };
        }

        // Verification
        case 'verifyResults':
          return { success: true, ...this.filterService.verify() };

        // Bug report
        case 'reportBug': {
          const bug = this.filterService.reportBug({
            severity: args.severity,
            title: args.title,
            steps: args.steps || [],
            expected: args.expected,
            actual: args.actual,
          });
          return { success: true, bug };
        }

        default:
          return { success: false, error: `Tool "${name}" không tồn tại` };
      }
    } catch (e: any) {
      return { success: false, error: e.message };
    }
  }
}
