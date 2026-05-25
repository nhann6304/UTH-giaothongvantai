import { Module } from '@nestjs/common';
import { ChatController } from './chat.controller';
import { ChatService } from './chat.service';
import { UserModule } from '../user/user.module';
import { FilterModule } from '../filter/filter.module';

@Module({
  imports: [UserModule, FilterModule],
  controllers: [ChatController],
  providers: [ChatService],
})
export class ChatModule {}
