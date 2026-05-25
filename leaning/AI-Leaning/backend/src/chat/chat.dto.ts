export class ChatRequestDto {
  message: string;
}

export interface ToolCallTrace {
  name: string;
  args: any;
  result: any;
}

export interface ChatResponseDto {
  reply: string;
  toolCalls: ToolCallTrace[];
  profile: any;
  filterState?: any;
  bugs?: any[];
}
