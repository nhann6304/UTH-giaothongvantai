#include <iostream>
using namespace std;

// Cách 1: Đệ quy
long long fibonacciDeQuy(int n) {
    if (n <= 1) return n;
    return fibonacciDeQuy(n - 1) + fibonacciDeQuy(n - 2);
}

// Cách 2: Không đệ quy
long long fibonacciKhongDeQuy(int n) {
    if (n <= 1) return n;
    
    long long f0 = 0, f1 = 1, fn;
    for (int i = 2; i <= n; i++) {
        fn = f0 + f1;
        f0 = f1;
        f1 = fn;
    }
    return fn;
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;
    
    cout << "Fibonacci thu " << n << " (de quy): " << fibonacciDeQuy(n) << endl;
    cout << "Fibonacci thu " << n << " (khong de quy): " << fibonacciKhongDeQuy(n) << endl;
    
    return 0;
}
