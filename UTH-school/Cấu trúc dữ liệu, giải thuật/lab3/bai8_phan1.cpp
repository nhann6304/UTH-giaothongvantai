#include <iostream>
using namespace std;

// Hàm tính giai thừa
long long giaiThua(int n) {
    if (n <= 1) return 1;
    long long gt = 1;
    for (int i = 2; i <= n; i++) {
        gt *= i;
    }
    return gt;
}

// Cách 1: Đệ quy - Tính i! * (i+1) đệ quy
long long phanTuDeQuy(int i) {
    if (i == 1) return 2; // 1! * 2 = 2
    return giaiThua(i) * (i + 1);
}

long long tongDeQuy(int n) {
    if (n == 1) return 2;
    return tongDeQuy(n - 1) + phanTuDeQuy(n);
}

// Cách 2: Không đệ quy
long long tongKhongDeQuy(int n) {
    long long tong = 0;
    for (int i = 1; i <= n; i++) {
        tong += giaiThua(i) * (i + 1);
    }
    return tong;
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;
    
    cout << "Sn = 1!*2 + 2!*3 + ... + " << n << "!*" << (n+1) << endl;
    cout << "Ket qua (de quy): " << tongDeQuy(n) << endl;
    cout << "Ket qua (khong de quy): " << tongKhongDeQuy(n) << endl;
    
    return 0;
}
