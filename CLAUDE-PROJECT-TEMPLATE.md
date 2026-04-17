# CLAUDE.md - Template cho dự án có sẵn

## Project Overview
<!-- Mô tả ngắn về project của bạn -->
Ví dụ: Dự án e-commerce với Next.js, TypeScript, và PostgreSQL

## Tech Stack
<!-- Liệt kê technologies đang dùng -->
- Frontend: Next.js 14, TypeScript, Tailwind CSS
- Backend: Node.js, Express, PostgreSQL
- Testing: Jest, Playwright
- Deployment: Vercel, Docker

## Quy tắc coding của project
<!-- Các quy tắc riêng của project -->
- Sử dụng TypeScript strict mode
- Component naming: PascalCase
- File naming: kebab-case
- Git hooks: pre-commit với lint-staged

## Skills được sử dụng
<!-- Các ECC skills phù hợp với project -->
- `/typescript-reviewer` - Review TypeScript code
- `/react-reviewer` - Review React components
- `/nextjs-patterns` - Next.js best practices
- `/security-reviewer` - Security checks
- `/performance-optimizer` - Performance optimization
- `/e2e-testing` - E2E test patterns

## Commands hữu ích
<!-- Các commands hay dùng cho project -->
- `/plan` - Lập kế hoạch feature mới
- `/code-review` - Review code trước commit
- `/security-scan` - Quét bảo mật
- `/test-coverage` - Kiểm tra độ phủ test
- `/build-fix` - Fix lỗi build

## File structure quan trọng
```
project/
├── src/
│   ├── components/     # React components
│   ├── pages/         # Next.js pages
│   ├── lib/           # Utility functions
│   └── types/         # TypeScript types
├── tests/             # Test files
├── docs/              # Documentation
└── CLAUDE.md          # File này
```

## Workflow cho project này

### Khi làm feature mới:
1. `/plan "Thêm feature X"`
2. `/tdd` (nếu feature phức tạp)
3. Implement code
4. `/typescript-reviewer`
5. `/security-reviewer` (nếu liên quan đến auth/data)
6. Manual test
7. Commit

### Khi fix bug:
1. `/build-error-resolver "Lỗi X"`
2. Fix code
3. `/code-review`
4. Test lại
5. Commit

### Khi review PR:
1. `/code-review` trên files thay đổi
2. `/security-reviewer` cho sensitive files
3. Check test coverage

## Custom rules cho project
<!-- Các quy tắc riêng -->
- Luôn validate input ở API routes
- Sử dụng React.memo cho components lớn
- Error boundary cho mỗi page
- Loading states cho async operations

## Notes
<!-- Ghi chú quan trọng -->
- Project đang dùng legacy code ở module X
- Cần refactor module Y trong tương lai
- Database schema đang thay đổi
- Performance issues ở page Z
