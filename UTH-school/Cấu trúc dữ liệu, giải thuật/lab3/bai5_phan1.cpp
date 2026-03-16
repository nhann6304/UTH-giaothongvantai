#include <iostream>
using namespace std;

// Hàm tính Fibonacci không đệ quy
long long fibonacci(int n) {
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
    int M, N;
    cout << "Nhap M: ";
    cin >> M;
    cout << "Nhap N: ";
    cin >> N;
    
    if (M >= N) {
        cout << "M phai nho hon N!" << endl;
        return 0;
    }
    
    long long tong = 0;
    cout << "Cac so Fibonacci chan tu F(" << M << ") den F(" << N << "): ";
    
    for (int i = M; i <= N; i++) {
        long long fib = fibonacci(i);
        if (fib % 2 == 0) {
            cout << fib << " ";
            tong += fib;
        }
    }
    
    cout << endl << "Tong cac so chan: " << tong << endl;
    
    return 0;
}
