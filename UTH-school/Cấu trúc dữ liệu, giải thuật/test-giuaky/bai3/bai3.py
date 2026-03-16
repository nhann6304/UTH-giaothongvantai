import math


# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Hàm tìm cột
def find_column_with_most_primes(matrix):
    if not matrix:
        return -1

    M = len(matrix)  # Số dòng
    N = len(matrix[0])  # Số cột

    max_primes = -1
    best_col_index = -1

    # Duyệt qua từng cột j
    for j in range(N):
        count = 0
        # Duyệt qua từng dòng i
        for i in range(M):
            if is_prime(matrix[i][j]):
                count += 1

        # Logic cập nhật:
        # Nếu số lượng hiện tại >= max cũ, cập nhật lại index.
        # Điều này đảm bảo nếu có 2 cột bằng nhau, cột chạy sau (index lớn hơn) sẽ được chọn.
        if count >= max_primes:
            max_primes = count
            best_col_index = j

    return best_col_index


# --- CHẠY THỬ ---
if __name__ == "__main__":

    A = [[1, 2, 3, 4], [6, 7, 8, 5], [10, 11, 12, 13]]

    # Cột 0: 0
    # Cột 1: 2, 11 (2 số)
    # Cột 2: 3, 7 (2 số)
    # Cột 3: 5, 13 (2 số) -> Cần chọn cột này vì index lớn nhất (3)

    result = find_column_with_most_primes(A)
    print(f"Cot co nhieu so nguyen to nhat (uu tien index lon) la:: {result}")
