"""Demo: Python type checking giống TypeScript khi bật Pylance strict mode."""

# ✓ ĐÚNG — Pylance không kêu
x: str = "Hello"
x.lower()
print(x)


# ✗ SAI — Pylance gạch đỏ (giống TS error)
# Bỏ comment dòng dưới để thấy lỗi:

# y: str = 123                    # Type "int" not assignable to "str"
# z: int = "abc"                  # Type "str" not assignable to "int"
# x.toUpperCase()                 # str không có method này (Python dùng .upper())


# ✗ SAI — Function type
def greet(name: str) -> str:
    return f"Hello {name}"


# greet(123)                      # Argument of type "int" not assignable to "str"
# result: int = greet("Nhan")     # str không gán được vào int


# ✓ Đối chiếu TypeScript:
# TS:     const x: string = "Hello"; x.toLowerCase();
# Python: x: str = "Hello"; x.lower()


# Lưu ý: dù Pylance báo lỗi, Python VẪN chạy được.
# Khác TS (compiler chặn build) — Python chỉ cảnh báo trong IDE.
# Muốn chặn thật sự: dùng `mypy` trong pre-commit hook hoặc CI.

if __name__ == "__main__":
    print(greet("Nhan"))
