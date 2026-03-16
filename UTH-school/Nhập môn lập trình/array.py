def nhapmang(arr, n):
    for i in range(n):
        num = int(input(f"Nhập số thứ {i + 1}: "))
        arr.append(num)


def xuatmang(arr):
    for x in arr:
        print(x, end=" ")
    print()


def sumA(arr):
    s = 0
    for x in arr:
        s += x
    return s


def checkNguyenTo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def countNguyenTo(arr):
    count = 0
    for x in arr:
        if checkNguyenTo(x):
            count += 1
    return count


def kiemtramang(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True


def main():
    n = int(input("Nhập số phần tử trong mảng: "))
    arr = []

    nhapmang(arr, n)

    print("The array you entered is:")
    xuatmang(arr)

    print("<<Sum Array>> ===", sumA(arr))
    print("<<Count Prime Numbers>> ===", countNguyenTo(arr))
    print("<<Is Array Sorted in Ascending Order?>> ===", kiemtramang(arr))


main()
