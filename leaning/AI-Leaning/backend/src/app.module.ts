import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { ChatModule } from './chat/chat.module';
import { UserModule } from './user/user.module';
import { FilterModule } from './filter/filter.module';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    UserModule,
    FilterModule,
    ChatModule,
  ],
})
export class AppModule {}
