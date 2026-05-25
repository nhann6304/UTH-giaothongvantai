import { chromium, type Browser, type BrowserContext, type Page } from 'playwright';
import * as path from 'path';
import * as fs from 'fs';
import type { TargetConfig } from '../types';

let _browser: Browser | null = null;
let _context: BrowserContext | null = null;
let _page: Page | null = null;

export async function getBrowser(): Promise<Browser> {
  if (_browser) return _browser;
  const headless = !!process.env.PLAYWRIGHT_HEADLESS;
  _browser = await chromium.launch({ headless });
  return _browser;
}

export async function getContext(): Promise<BrowserContext> {
  if (_context) return _context;
  const browser = await getBrowser();
  _context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  return _context;
}

export async function getPage(): Promise<Page> {
  if (_page && !_page.isClosed()) return _page;
  const ctx = await getContext();
  _page = await ctx.newPage();
  return _page;
}

export async function browserLogin(
  target: TargetConfig,
  email: string,
  password: string,
): Promise<{ ok: boolean; message: string; cookies: string }> {
  const page = await getPage();
  const loginUrl = target.frontendUrl + '/auth/login';
  await page.goto(loginUrl, { waitUntil: 'domcontentloaded', timeout: 15000 });

  // Strategy: tìm input email + password phổ biến rồi điền
  const emailSel = await firstVisible(page, [
    'input[type="email"]',
    'input[name="email"]',
    'input[name="user_email"]',
    'input[placeholder*="mail" i]',
  ]);
  const passSel = await firstVisible(page, [
    'input[type="password"]',
    'input[name="password"]',
    'input[name="user_password"]',
  ]);
  if (!emailSel || !passSel) {
    return { ok: false, message: 'Không tìm được input email/password trên trang login', cookies: '' };
  }
  await page.fill(emailSel, email);
  await page.fill(passSel, password);

  // Nút submit
  const btnSel = await firstVisible(page, [
    'button[type="submit"]',
    'button:has-text("Login")',
    'button:has-text("Đăng nhập")',
    'button:has-text("Sign in")',
  ]);
  if (!btnSel) {
    return { ok: false, message: 'Không tìm được nút submit', cookies: '' };
  }
  await Promise.all([
    page.waitForLoadState('networkidle', { timeout: 15000 }).catch(() => {}),
    page.click(btnSel),
  ]);

  const cookies = await (await getContext()).cookies();
  const tokenCookie = cookies.find((c) => c.name === target.auth.cookieName || /token/i.test(c.name));
  const cookieHeader = cookies
    .filter((c) => /token/i.test(c.name))
    .map((c) => `${c.name}=${c.value}`)
    .join('; ');

  return {
    ok: !!tokenCookie,
    message: tokenCookie ? 'login success via browser' : 'Không thấy cookie token sau login',
    cookies: cookieHeader,
  };
}

async function firstVisible(page: Page, selectors: string[]): Promise<string | null> {
  for (const sel of selectors) {
    const loc = page.locator(sel).first();
    try {
      await loc.waitFor({ state: 'visible', timeout: 1500 });
      return sel;
    } catch {}
  }
  return null;
}

export async function screenshot(label: string): Promise<string> {
  const page = await getPage();
  const dir = path.join(process.cwd(), 'screenshots');
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  const safe = label.replace(/[^a-z0-9_-]+/gi, '_').slice(0, 60);
  const file = path.join(dir, `${Date.now()}_${safe}.png`);
  await page.screenshot({ path: file, fullPage: true });
  return file;
}

export async function closeBrowser(): Promise<void> {
  try {
    await _page?.close();
  } catch {}
  try {
    await _context?.close();
  } catch {}
  try {
    await _browser?.close();
  } catch {}
  _page = null;
  _context = null;
  _browser = null;
}
