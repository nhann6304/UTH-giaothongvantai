import {
  Body,
  Controller,
  Get,
  HttpException,
  HttpStatus,
  Post,
} from '@nestjs/common';
import { ChatService } from './chat.service';
import { ChatRequestDto } from './chat.dto';
import { UserService } from '../user/user.service';

@Controller('chat')
export class ChatController {
  constructor(
    private readonly chatService: ChatService,
    private readonly userService: UserService,
  ) {}

  @Post()
  async chat(@Body() body: ChatRequestDto) {
    if (!body?.message || typeof body.message !== 'string') {
      throw new HttpException('message is required', HttpStatus.BAD_REQUEST);
    }
    try {
      return await this.chatService.chat(body.message);
    } catch (e: any) {
      throw new HttpException(
        e.message || 'Internal error',
        HttpStatus.INTERNAL_SERVER_ERROR,
      );
    }
  }

  @Get('profile')
  getProfile() {
    return this.userService.getProfile();
  }
}
