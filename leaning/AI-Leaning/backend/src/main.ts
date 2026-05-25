import { NestFactory } from '@nestjs/core';
import { ConfigService } from '@nestjs/config';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const config = app.get(ConfigService);

  app.enableCors({
    origin: config.get<string>('FRONTEND_ORIGIN') || 'http://localhost:4001',
  });

  const port = config.get<number>('PORT') || 4000;
  await app.listen(port);
  console.log(`[Backend] http://localhost:${port}`);
}
bootstrap();
