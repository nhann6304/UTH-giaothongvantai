import 'dotenv/config';
import express from 'express';
import cors from 'cors';
import * as fs from 'fs';
import * as path from 'path';
import { ChatService } from './chat.service';
import { session } from './session';
import { closeBrowser } from './tools/browser';

const app = express();
app.use(cors());
app.use(express.json({ limit: '2mb' }));

const screenshotsDir = path.join(process.cwd(), 'screenshots');
if (!fs.existsSync(screenshotsDir)) fs.mkdirSync(screenshotsDir, { recursive: true });
app.use('/screenshots', express.static(screenshotsDir));

const chat = new ChatService();

app.get('/health', (_req, res) => {
  res.json({ ok: true, model: 'gemini-2.5-flash' });
});

app.get('/targets', (_req, res) => {
  const dir = path.join(__dirname, 'targets');
  const files = fs.readdirSync(dir).filter((f) => f.endsWith('.json'));
  const list = files.map((f) => {
    const j = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
    return { id: f.replace('.json', ''), name: j.name, modules: Object.keys(j.modules || {}) };
  });
  res.json({ targets: list });
});

app.post('/chat', async (req, res) => {
  const { message } = req.body || {};
  if (!message || typeof message !== 'string') {
    res.status(400).json({ message: 'Body cần { message: string }' });
    return;
  }
  try {
    const out = await chat.send(message);
    res.json(out);
  } catch (e: any) {
    res.status(500).json({ message: e?.message || String(e) });
  }
});

app.post('/reset', async (_req, res) => {
  session.reset();
  await closeBrowser();
  res.json({ ok: true });
});

app.post('/session/target', (req, res) => {
  const { target, baseUrl, frontendUrl, loginPath } = req.body || {};
  if (!target || typeof target !== 'string') {
    res.status(400).json({ message: 'Body cần { target: string, baseUrl?, frontendUrl?, loginPath? }' });
    return;
  }
  session.setOverride({ target, baseUrl, frontendUrl, loginPath });
  res.json({ ok: true, override: session.get().override });
});

app.get('/session', (_req, res) => {
  const s = session.get();
  res.json({
    loggedIn: !!s.ctx,
    target: s.ctx?.targetName,
    bugs: s.bugs.length,
    toolCalls: s.toolCalls.length,
    override: s.override,
  });
});

app.get('/bugs', (_req, res) => {
  res.json({ bugs: session.get().bugs });
});

const port = Number(process.env.PORT) || 4100;
app.listen(port, () => {
  console.log(`[ai-leaning-tester] listening on http://localhost:${port}`);
  console.log(`POST /chat   { message: string }`);
  console.log(`GET  /targets`);
  console.log(`GET  /bugs`);
  console.log(`POST /reset`);
});
