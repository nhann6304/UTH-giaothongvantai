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

// Cách 1: Đệ quy - Công thức: C(n,k) = C(n-1,k-1) + C(n-1,k)
long long toHopDeQuy(int n, int k) {
    if (k == 0 || k == n) return 1;
    if (k > n) return 0;
    return toHopDeQuy(n - 1, k - 1) + toHopDeQuy(n - 1, k);
}

// Cách 2: Không đệ quy - Công thức: C(n,k) = n! / (k! * (n-k)!)
long long toHopKhongDeQuy(int n, int k) {
    if (k > n) return 0;
    if (k == 0 || k == n) return 1;
    
    // Tối ưu: C(n,k) = C(n, n-k)
    if (k > n - k) k = n - k;
    
    long long result = 1;
    for (int i = 0; i < k; i++) {
        result = result * (n - i) / (i + 1);
    }
    return result;
}

int main() {
    int n, k;
    cout << "Nhap n: ";
    cin >> n;
    cout << "Nhap k: ";
    cin >> k;
    
    if (k > n || k < 0 || n < 0) {
        cout << "To hop khong ton tai!" << endl;
    } else {
        cout << "C(" << n << "," << k << ") de quy: " << toHopDeQuy(n, k) << endl;
        cout << "C(" << n << "," << k << ") khong de quy: " << toHopKhongDeQuy(n, k) << endl;
    }
    
    return 0;
}
