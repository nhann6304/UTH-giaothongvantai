#include <iostream>
#include <cmath>

using namespace std;

long long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// Cách 1: Không đệ quy (Iterative) -> Tối ưu hơn vì tính dồn giai thừa
double bai2_1_Iterative(int n) {
    double sum = 0;
    long long fact = 1
    for (int i = 1; i <= n; i++) {
        fact *= i;
        sum += (double)fact / (i + 1);
    }
    return sum;
}

// Cách 2: Đệ quy (Recursive)
double bai2_1_Recursive(int n) {
    if (n == 0) return 0; 
    // Công thức truy hồi: S(n) = S(n-1) + n!/(n+1)
    return bai2_1_Recursive(n - 1) + (double)factorial(n) / (n + 1);
}

// ==========================================
// BÀI 2.2: Tổng các chữ số của N chia hết cho k
// ==========================================

// Cách 1: Không đệ quy (Iterative)
int bai2_2_Iterative(int n, int k) {
    int sum = 0;
    while (n > 0) {
        int digit = n % 10; 
        if (digit % k == 0) {
            sum += digit;
        }
        n /= 10; 
    }
    return sum;
}

// Cách 2: Đệ quy (Recursive)
int bai2_2_Recursive(int n, int k) {
    if (n == 0) return 0; // Điều kiện dừng
    
    int digit = n % 10;
    int currentVal = (digit % k == 0) ? digit : 0;
    
    return currentVal + bai2_2_Recursive(n / 10, k);
}

// ==========================================
// BÀI 2.3: Xuất số Fibonacci lẻ trong đoạn [m, n]
// F1=1, F2=1, Fn = Fn-1 + Fn-2
// ==========================================

void bai2_3_Fibonacci(int m, int n) {
    long long f1 = 1, f2 = 1;
    long long fn = 1;
    
    cout << "Fibonacci le trong [" << m << ", " << n << "]: ";
    
    if (1 >= m && 1 <= n) cout << "1 "; 
    
    while (true) {
        fn = f1 + f2; 
        f1 = f2;
        f2 = fn;
        
        if (fn > n) break; 
        
        if (fn >= m && fn % 2 != 0) {
            cout << fn << " ";
        }
    }
    cout << endl;
}

int main() {
    int n1 = 5;
    cout << "--- Bai 2.1 (n=" << n1 << ") ---" << endl;
    cout << "Khong de quy: " << bai2_1_Iterative(n1) << endl;
    cout << "De quy:       " << bai2_1_Recursive(n1) << endl;

    // --- TEST BÀI 2.2 ---
    int N = 123456, k = 2;
    cout << "\n--- Bai 2.2 (N=" << N << ", k=" << k << ") ---" << endl;
    cout << "Khong de quy: " << bai2_2_Iterative(N, k) << endl;
    cout << "De quy:       " << bai2_2_Recursive(N, k) << endl;

    // --- TEST BÀI 2.3 ---
    int m = 10, n3 = 30;
    cout << "\n--- Bai 2.3 ([m, n] = [" << m << ", " << n3 << "]) ---" << endl;
    bai2_3_Fibonacci(m, n3);

    return 0;
}