# Áp dụng ECC vào AutoSocialsWebClient

## 🔍 Bước 1: Tìm dự án của bạn

Dự án AutoSocialsWebClient có thể ở:
- Desktop: `C:\Users\Nhan\Desktop\AutoSocialsWebClient`
- Documents: `C:\Users\Nhan\Documents\AutoSocialsWebClient`
- Projects folder: `C:\Projects\AutoSocialsWebClient`
- Hoặc bất kỳ đâu bạn đã clone/download

**Cách tìm nhanh:**
1. M Windows Explorer
2. Search "AutoSocialsWebClient"
3. Copy đường dẫn đầy đủ

## 🚀 Bước 2: Setup ECC cho AutoSocialsWebClient

Khi đã có đường dẫn, chạy các lệnh sau:

```bash
# Ví dụ: cd C:\Users\Nhan\Desktop\AutoSocialsWebClient
cd /path/to/AutoSocialsWebClient

# Clone ECC vào project
git clone https://github.com/affaan-m/everything-claude-code.git ecc

# Cài đặt ECC
cd ecc
npm install
.\install.ps1 --profile typescript  # Cho React/Next.js
# hoặc
.\install.ps1 --profile full        # Cho tất cả

# Quay lại project root
cd ..
```

## 📝 Bước 3: Tạo CLAUDE.md cho AutoSocialsWebClient

Tạo file `CLAUDE.md` trong root của AutoSocialsWebClient:

```markdown
# CLAUDE.md - AutoSocialsWebClient

## Project Overview
AutoSocialsWebClient - Web client for automated social media management

## Tech Stack
- Frontend: React/Next.js, TypeScript, Tailwind CSS
- State Management: Redux Toolkit / Zustand
- API: REST API / GraphQL
- Authentication: JWT / OAuth
- Testing: Jest, React Testing Library, Playwright
- Build: Vite / Next.js

## Features
- Multi-platform social media integration
- Scheduled posting
- Content management
- Analytics dashboard
- User authentication
- Real-time updates

## ECC Skills được sử dụng
- `/react-reviewer` - Review React components
- `/typescript-reviewer` - Review TypeScript code
- `/security-reviewer` - Check authentication & API security
- `/performance-optimizer` - Optimize bundle size & loading
- `/e2e-testing` - E2E test patterns
- `/frontend-patterns` - React/Next.js best practices

## Commands hữu ích
- `/plan` - Lập kế hoạch feature mới
- `/code-review` - Review code trước khi commit
- `/security-reviewer` - Check security issues
- `/build-fix` - Fix TypeScript/build errors
- `/test-coverage` - Kiểm tra độ phủ test

## Quy tắc coding
- Sử dụng TypeScript strict mode
- Component naming: PascalCase
- File naming: kebab-case
- Custom hooks: use* pattern
- API calls: trong service layer
- Error boundaries cho mỗi route

## File structure quan trọng
```
AutoSocialsWebClient/
├── src/
│   ├── components/     # React components
│   ├── pages/         # Page components
│   ├── hooks/         # Custom hooks
│   ├── services/      # API services
│   ├── store/         # State management
│   ├── types/         # TypeScript types
│   └── utils/         # Utility functions
├── tests/             # Test files
├── public/            # Static assets
└── CLAUDE.md          # File này
```

## Workflow cho AutoSocialsWebClient

### Khi làm feature mới:
1. `/plan "Thêm tính năng X cho social platform Y"`
2. `/tdd` (nếu feature phức tạp)
3. Implement code
4. `/typescript-reviewer`
5. `/react-reviewer`
6. `/security-reviewer` (nếu liên quan đến auth/API)
7. `/e2e-testing` (nếu là user flow)
8. Manual test
9. Commit

### Khi fix bug:
1. `/build-error-resolver "Bug description"`
2. Fix code
3. `/code-review`
4. Test lại
5. Commit

### Khi review PR:
1. `/code-review` trên changed files
2. `/security-reviewer` cho sensitive changes
3. `/test-coverage` check
4. Approve/request changes

## Areas cần chú ý
- **Security**: Authentication tokens, API keys, user data
- **Performance**: Large social media feeds, image uploads
- **UX**: Loading states, error handling, offline support
- **Testing**: Critical user flows, API integration
```

## 🔧 Bước 4: Áp dụng vào code hiện có

### Ví dụ: Cải thiện một React component

**Code cũ (ví dụ):**
```typescript
// src/components/SocialPost.tsx
import React from 'react'

function SocialPost({ post, onLike, onComment }) {
  return (
    <div>
      <h3>{post.title}</h3>
      <p>{post.content}</p>
      <button onClick={() => onLike(post.id)}>Like</button>
      <button onClick={() => onComment(post.id)}>Comment</button>
    </div>
  )
}

export default SocialPost
```

**Sau khi áp dụng ECC:**
```typescript
// src/components/SocialPost.tsx
import React, { memo, useCallback } from 'react'
import type { SocialPost as PostType, SocialPostProps } from '../types/social'

/**
 * SocialPost Component
 * Displays a social media post with interaction buttons
 */
const SocialPost: React.FC<SocialPostProps> = ({ 
  post, 
  onLike, 
  onComment,
  className = ''
}) => {
  const handleLike = useCallback(() => {
    if (post.id) {
      onLike(post.id)
    }
  }, [post.id, onLike])

  const handleComment = useCallback(() => {
    if (post.id) {
      onComment(post.id)
    }
  }, [post.id, onComment])

  return (
    <article className={`social-post ${className}`}>
      <header className="post-header">
        <h3 className="post-title">{post.title}</h3>
        <time className="post-date" dateTime={post.createdAt}>
          {new Date(post.createdAt).toLocaleDateString()}
        </time>
      </header>
      
      <div className="post-content">
        <p>{post.content}</p>
        {post.image && (
          <img 
            src={post.image} 
            alt={post.title}
            className="post-image"
            loading="lazy"
          />
        )}
      </div>
      
      <footer className="post-actions">
        <button 
          onClick={handleLike}
          className="like-button"
          aria-label={`Like post ${post.title}`}
        >
          ❤️ {post.likes || 0}
        </button>
        
        <button 
          onClick={handleComment}
          className="comment-button"
          aria-label={`Comment on post ${post.title}`}
        >
          💬 {post.comments || 0}
        </button>
      </footer>
    </article>
  )
}

export default memo(SocialPost)
```

## 📊 Bước 5: Audit toàn bộ project

Chạy các lệnh sau để audit project:

```bash
# Review toàn bộ TypeScript files
/typescript-reviewer "Review entire codebase"

# Check security issues
/security-reviewer "Audit authentication and API security"

# Performance analysis
/performance-optimizer "Analyze bundle size and loading performance"

# Test coverage
/test-coverage "Check current test coverage"

# Create project-specific skills
/skill-create "Generate AutoSocials-specific patterns"
```

## 🎯 Bước 6: Continuous Improvement

### Hàng tuần:
```bash
/learn "Extract patterns from this week's development"
/evolve "Cluster patterns into reusable skills"
/instinct-status "Check what we've learned"
```

### Hàng tháng:
```bash
/skill-stocktake "Audit and clean up skills"
/security-scan "Run full security audit"
/harness-audit "Check ECC configuration"
```

## 🚀 Benefits cho AutoSocialsWebClient

### Code Quality:
- ✅ TypeScript strict mode
- ✅ React best practices
- ✅ Proper error handling
- ✅ Performance optimization

### Security:
- ✅ Authentication security
- ✅ API token protection
- ✅ Input validation
- ✅ XSS prevention

### Testing:
- ✅ Unit tests cho components
- ✅ Integration tests cho APIs
- ✅ E2E tests cho user flows
- ✅ 80%+ test coverage

### Developer Experience:
- ✅ Consistent code style
- ✅ Automated reviews
- ✅ Fast feedback loops
- ✅ Documentation standards

## 📝 Next Steps

1. **Setup ECC** - Clone và cài đặt
2. **Create CLAUDE.md** - Config cho project
3. **Audit existing code** - Find improvement areas
4. **Apply improvements** - Gradual migration
5. **Measure results** - Track quality metrics
6. **Team adoption** - Onboard team members

## 🆘 Troubleshooting

Nếu gặp issues:
```bash
/troubleshooting "ECC setup problems"
/docs-lookup "AutoSocials best practices"
/learn "Extract error patterns"
```

---

**Ready to transform AutoSocialsWebClient with ECC?** 🚀
