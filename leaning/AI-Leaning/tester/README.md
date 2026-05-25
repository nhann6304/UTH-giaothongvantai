# AI-Leaning Tester

> AI QA Agent **black-box** cho web app — chat tiếng Việt: "test filter module users với account X" → AI tự login, áp filter, verify kết quả, báo bug.
>
> Mục tiêu: viết 1 lần dùng cho **nhiều dự án**. Mỗi dự án chỉ cần thêm 1 file config trong `src/targets/`.
>
> **KHÔNG** chỉnh sửa source AutoSocialsWebClient / AutoSocialsWebServer. Tester chỉ gọi HTTP/Playwright vào instance đang chạy.

---

## Architecture

```
User chat (tiếng Việt)
   ↓
[Express server :4100]
   ↓
[Gemini 2.5 Flash + 8 tools]
   ↓
┌── loginApi  ──→ POST /api/auth/login          (fetch)
├── loginBrowser → /auth/login                  (Playwright)
├── getModuleSchema → đọc src/targets/*.json
├── getFilterOptions → GET /api/users/find-filter-options
├── findMulti → GET /api/users/find-multi?filters=...
├── verifyResults → so từng row vs filter (oracle local)
├── screenshotPage → Playwright screenshot
└── reportBug → ghi vào session bugs[]
```

---

## Setup

```powershell
cd e:\auto\giathongvantai\leaning\AI-Leaning\tester
npm install
npx playwright install chromium
copy .env.example .env
# Mở .env, paste GEMINI_API_KEY (https://aistudio.google.com/app/apikey)
npm run dev
```

Server chạy ở `http://localhost:4100`.

---

## Smoke test

```powershell
# Health
curl http://localhost:4100/health

# Targets có sẵn (đọc từ src/targets/*.json)
curl http://localhost:4100/targets

# Chat
curl -X POST http://localhost:4100/chat `
  -H "Content-Type: application/json" `
  -d '{"message":"Login vào target autosocials với admin@example.com / Admin123@ rồi test filter Position của module users"}'
```

---

## Yêu cầu trước khi chạy thật

1. **BE đang chạy**: `e:\auto\AutoSocialsWebServer` ở port 9000 (xem `AutoSocialsWebClient/CLAUDE.md` để start).
2. **FE đang chạy** (nếu test browser flow): port 3000.
3. **Có tài khoản test**: gợi ý tạo account read-only, KHÔNG dùng admin thật.
4. **`src/targets/autosocials.json` đúng**:
   - `baseUrl` = nơi BE đang chạy (vd `http://localhost:9000`)
   - `frontendUrl` = nơi FE đang chạy
   - Nếu test environment khác (staging/prod), tạo file mới: `src/targets/<name>.json`

---

## Cách chat hiệu quả

| Câu chat | AI sẽ làm gì |
|---|---|
| "Login target autosocials với A / B rồi test filter Position module users" | loginApi → getModuleSchema → findMulti baseline → findMulti với Position → verifyResults → reportBug nếu fail |
| "Test toàn bộ filter của module users" | Loop từng field (xem `filterFields` trong config), apply 1 cái 1 → verify → report |
| "Test edge case date range Created At" | findMulti với startDate > endDate, boundary cuối ngày |
| "Báo cáo bug đã tìm được" | List bugs từ session |

---

## Thêm module mới (vd "proxy")

1. Mở `src/targets/autosocials.json`
2. Thêm vào `modules`:
   ```json
   "proxy": {
     "label": "Tools > Account Proxy",
     "basePath": "/api/proxy",
     "endpoints": { "findMulti": "/find-multi", "findOverview": "/find-overview", "findFilterOptions": "/find-filter-options" },
     "filterFields": [ ... ],
     "verifyRules": { "rowFieldMapping": { ... } }
   }
   ```
3. Đọc `e:\auto\AutoSocialsWebClient\src\layouts\<group>\<module>\filter-<module>-filed.ts` để biết fields → copy y nguyên vào `filterFields`.
4. Done — không phải chạm code.

Xem thêm: `../docs/filter-endpoints-map.md` để hiểu pattern.

---

## Output bug

```json
{
  "id": "bug_1",
  "severity": "HIGH",
  "title": "Filter hasPermission=YES vẫn trả row không có role",
  "steps": [
    "loginApi",
    "findMulti({filters:[{field:hasPermission,values:[YES]}]})",
    "verifyResults phát hiện 3/20 row có roles=[]"
  ],
  "expected": "Mọi row trả về phải có roles.length > 0",
  "actual": "Có 3 row roles=[]: id=xxx, yyy, zzz",
  "field": "hasPermission"
}
```

GET `http://localhost:4100/bugs` để xem.

---

## Giới hạn (nói thẳng)

| Bắt được tốt | Bắt được kém |
|---|---|
| Filter field bị bỏ quên (apply nhưng row không khớp) | Visual layout bug (lệch px, overlap) |
| Range comparator sai (`<` thay `<=`) | Race condition |
| Combo filter break | Business rule sâu cần domain knowledge |
| Reset filter không clear | Performance regression |
| Date boundary bug | Bug chỉ xảy ra với user role cụ thể (cần switch account) |

Tỷ lệ catch bug filter logic kỳ vọng: **70-80%**.

---

## Pending

- [ ] Frontend chat UI riêng cho tester (hiện tại chỉ có HTTP endpoint)
- [ ] Hỗ trợ 2FA / OAuth login
- [ ] Multi-target test (chạy cùng filter trên local vs staging, so diff)
- [ ] Schedule chạy cron + post slack
- [ ] Module config registry tự đọc từ source AutoSocialsWebClient (không phải copy tay)
