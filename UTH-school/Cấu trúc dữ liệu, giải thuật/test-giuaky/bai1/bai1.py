import math


def main():
    print("Nhap gia tri x (radian): ", end="")
    x = float(input())

    current_sum = 0.0
    term = x
    n = 0
    epsilon = 1e-6

    while abs(term) >= epsilon:
        current_sum += term

        term = term * (-x * x) / ((2 * n + 2) * (2 * n + 3))

        n += 1

    print(f"Gia tri gan dung cua sin({x}) la: {current_sum:.7f}")

    print(f"Gia tri thuc te (math.sin):      {math.sin(x)}")


if __name__ == "__main__":
    main()
