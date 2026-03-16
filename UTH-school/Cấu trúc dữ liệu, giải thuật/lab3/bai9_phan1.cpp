#include <iostream>
using namespace std;

// Giả sử t(n) được định nghĩa như sau:
// t(0) = 0
// t(1) = 1
// t(n) = t(n-1) + t(n-2) + n (ví dụ)
// Bạn có thể thay đổi công thức theo đề bài cụ thể

// Cách 1: Đệ quy
int tDeQuy(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return tDeQuy(n - 1) + tDeQuy(n - 2) + n;
}

// Cách 2: Không đệ quy
int tKhongDeQuy(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    int t0 = 0, t1 = 1, tn;
    for (int i = 2; i <= n; i++) {
        tn = t0 + t1 + i;
        t0 = t1;
        t1 = tn;
    }
    return tn;
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;
    
    cout << "t(" << n << ") de quy: " << tDeQuy(n) << endl;
    cout << "t(" << n << ") khong de quy: " << tKhongDeQuy(n) << endl;
    
    cout << "\nLuu y: Cong thuc t(n) = t(n-1) + t(n-2) + n" << endl;
    cout << "Ban co the thay doi cong thuc theo de bai cu the!" << endl;
    
    return 0;
}
