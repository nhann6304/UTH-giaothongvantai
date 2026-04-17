# CLAUDE.md - Hướng dẫn cho Claude Code

## Project Overview
Dự án học tập Nhập môn lập trình với các bài tập cơ bản về:
- Array manipulation (TypeScript)
- Python exercises (Jupyter Notebook)
- Basic programming concepts

## Quy tắc coding
- Sử dụng TypeScript cho file .ts
- Naming convention: camelCase cho variables, PascalCase cho functions
- Comment tiếng Việt
- Kiểm tra đầu vào (input validation)
- Handle edge cases

## Skills được sử dụng
- `/typescript-reviewer` - Review code TypeScript
- `/python-reviewer` - Review code Python  
- `/tdd` - Test-driven development
- `/coding-standards` - Coding standards

## Commands hữu ích
- `/plan` - Lập kế hoạch trước khi code
- `/code-review` - Review code sau khi viết
- `/test-coverage` - Kiểm tra độ phủ test

## File structure
```
Nhập-môn-lập-trình/
├── array.ts              # Bài tập mảng TypeScript
├── *.ipynb              # Bài tập Python Jupyter
├── CLAUDE.md            # File config này
└── ecc/                 # Everything Claude Code
```

## Workflow đề xuất
1. Đọc đề bài -> `/plan "Giải bài tập X"`
2. Viết test -> `/tdd`
3. Implement code
4. Review -> `/typescript-reviewer`
5. Fix lỗi nếu có
