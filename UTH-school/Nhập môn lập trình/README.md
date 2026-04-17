# Nhập môn lập trình với Everything Claude Code

Dự án này trình bày cách áp dụng Everything Claude Code (ECC) vào việc học lập trình cơ bản.

## 🚀 Quick Start

### 1. Cài đặt dependencies
```bash
npm install
```

### 2. Chạy bài tập mảng
```bash
npm start
```

### 3. Chạy test
```bash
npm test
```

### 4. Development mode
```bash
npm run dev
```

## 📁 Cấu trúc project

```
Nhập-môn-lập-trình/
├── array.ts              # Bài tập mảng TypeScript (đã cải tiến)
├── array.test.ts          # Test cho bài tập mảng
├── huynhthanhnhan-*.ipynb # Bài tập Python Jupyter
├── CLAUDE.md             # Config cho Claude Code
├── package.json          # Dependencies và scripts
├── tsconfig.json         # TypeScript config
├── jest.config.js        # Jest test config
└── README.md            # File này
```

## 🛠️ Cách sử dụng ECC

### Workflow chuẩn với ECC:

1. **Lập kế hoạch** - `/plan "Giải bài tập X"`
2. **Viết test** - `/tdd`
3. **Implement code** - Viết code bình thường
4. **Review code** - `/typescript-reviewer`
5. **Fix lỗi** - `/build-error-resolver`

### Ví dụ thực tế:

```bash
# Bắt đầu bài tập mới
/plan "Giải bài tập sắp xếp mảng tăng dần"

# Áp dụng TDD
/tdd

# Sau khi viết xong code
/typescript-reviewer

# Nếu có lỗi build
/build-error-resolver "Lỗi TypeScript"
```

## 📊 Code improvements đã áp dụng

### Trước khi dùng ECC:
```typescript
// Code gốc
function nhapmang1d(arr: number[], num: number): void {
    for (let i = 0; i <= num; i++) {  // Bug: i <= num
        console.log("<<<I>>>", arr[i]);  // Output không rõ ràng
    }
}
```

### Sau khi dùng ECC:
```typescript
// Code cải tiến
function nhapMang1D(arr: number[], num: number): void {
    // Validation: kiểm tra input
    if (!Array.isArray(arr) || num <= 0 || num > arr.length) {
        console.error("Input không hợp lệ");
        return;
    }
    
    console.log("Nhập mảng (hiển thị các phần tử):");
    for (let i = 0; i < num; i++) {  // Fix: i < num
        console.log(`arr[${i}] = ${arr[i]}`);  // Output rõ ràng
    }
}
```

## 🔧 Skills và Commands hữu ích

### Skills cho project này:
- `/typescript-reviewer` - Review code TypeScript
- `/python-reviewer` - Review code Python
- `/tdd-workflow` - Test-driven development
- `/coding-standards` - Coding standards

### Commands hay dùng:
- `/plan` - Lập kế hoạch trước khi code
- `/code-review` - Review code sau khi viết
- `/test-coverage` - Kiểm tra độ phủ test
- `/build-fix` - Fix lỗi build

## 🎯 Các bài tập có thể làm với ECC

1. **Array manipulation** - Sắp xếp, tìm kiếm, đảo ngược
2. **String processing** - Đếm ký tự, chuỗi con
3. **Basic algorithms** - Fibonacci, prime numbers
4. **Data structures** - Stack, Queue, Linked List

## 📝 Tips học tập với ECC

1. **Luôn bắt đầu với `/plan`** - Đừng code ngay, hãy lập kế hoạch trước
2. **Dùng `/tdd` cho bài khó** - Viết test trước giúp hiểu rõ yêu cầu
3. **Review với `/typescript-reviewer`** - Học được best practices
4. **Ghi chú tiếng Việt** - Giúp hiểu và nhớ lâu hơn

## 🚀 Next steps

1. **Thêm bài tập mới** - Áp dụng workflow ECC
2. **Tạo custom skills** - Cho các bài tập đặc thù
3. **Integrate với Python** - Review và test code Python
4. **Continuous learning** - Sử dụng `/learn` để rút kinh nghiệm

## 📚 Tài liệu tham khảo

- [Everything Claude Code](https://github.com/affaan-m/everything-claude-code)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Jest Testing](https://jestjs.io/docs/getting-started)

---

**Author:** Huỳnh Thành Nhán  
**Course:** Nhập môn lập trình  
**Tools:** Everything Claude Code + TypeScript + Jest
