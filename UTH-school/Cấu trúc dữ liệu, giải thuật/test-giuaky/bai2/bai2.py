import sys

sys.setrecursionlimit(2000)

# ==========================================
# BÀI 2.1: Tính Sn
# ==========================================


# Hàm phụ tính giai thừa
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Cách 1: Không đệ quy (Iterative)
def bai2_1_iterative(n):
    total = 0.0
    fact = 1
    for i in range(1, n + 1):
        fact *= i  # Tính giai thừa dồn: i! = (i-1)! * i
        total += fact / (i + 1)
    return total


# Cách 2: Đệ quy (Recursive)
def bai2_1_recursive(n):
    if n == 0:
        return 0
    return bai2_1_recursive(n - 1) + factorial(n) / (n + 1)


# ==========================================
# BÀI 2.2: Tổng chữ số chia hết cho k
# ==========================================


# Cách 1: Không đệ quy (Iterative)
def bai2_2_iterative(n, k):
    total = 0
    temp_n = n
    while temp_n > 0:
        digit = temp_n % 10
        if digit % k == 0:
            total += digit
        temp_n //= 10  # Phép chia lấy nguyên
    return total


# Cách 2: Đệ quy (Recursive)
def bai2_2_recursive(n, k):
    if n == 0:
        return 0

    digit = n % 10
    # Nếu chia hết thì cộng digit, không thì cộng 0
    current_val = digit if (digit % k == 0) else 0

    return current_val + bai2_2_recursive(n // 10, k)


# ==========================================
# BÀI 2.3: Fibonacci lẻ trong đoạn [m, n]
# ==========================================
def bai2_3_fibonacci(m, n):
    result = []

    # F1 = 1, F2 = 1
    f1, f2 = 1, 1

    # Kiểm tra F1, F2 (đều là 1)
    if m <= 1 <= n:
        result.append(1)
        # Nếu muốn in số 1 hai lần (do F1, F2) thì append thêm,
        # nhưng thông thường liệt kê tập hợp thì chỉ cần một số 1.

    while True:
        fn = f1 + f2
        f1, f2 = f2, fn  # Cập nhật

        if fn > n:
            break

        if fn >= m and fn % 2 != 0:
            result.append(fn)

    print(f"Fibonacci le trong [{m}, {n}]: {result}")


# --- MAIN TEST ---
if __name__ == "__main__":
    # Test 2.1
    print("--- Bai 2.1 (n=5) ---")
    print(f"Iterative: {bai2_1_iterative(5)}")
    print(f"Recursive: {bai2_1_recursive(5)}")

    # Test 2.2
    print("\n--- Bai 2.2 (N=123456, k=2) ---")
    print(f"Iterative: {bai2_2_iterative(123456, 2)}")
    print(f"Recursive: {bai2_2_recursive(123456, 2)}")

    # Test 2.3
    print("\n--- Bai 2.3 ---")
    bai2_3_fibonacci(10, 30)
