#include <iostream>
using namespace std;

// Hàm tính lũy thừa không dùng hàm có sẵn
double luythua(double x, int n) {
    double result = 1;
    for (int i = 0; i < n; i++) {
        result *= x;
    }
    return result;
}

// Hàm tính giá trị đa thức F(x) = a_n*x^n + a_(n-1)*x^(n-1) + ... + a_1*x + a_0
double tinhDaThuc(double a[], int n, double x) {
    double ketQua = 0;
    
    for (int i = 0; i <= n; i++) {
        ketQua += a[i] * luythua(x, i);
    }
    
    return ketQua;
}

// Cách 2: Sử dụng sơ đồ Horner (hiệu quả hơn)
// F(x) = a_0 + x(a_1 + x(a_2 + x(a_3 + ... + x*a_n)))
double tinhDaThucHorner(double a[], int n, double x) {
    double ketQua = a[n];
    
    for (int i = n - 1; i >= 0; i--) {
        ketQua = ketQua * x + a[i];
    }
    
    return ketQua;
}

int main() {
    int n;
    double x;
    
    cout << "Nhap bac cua da thuc n: ";
    cin >> n;
    
    double a[n + 1];
    
    cout << "Nhap cac he so (tu a0 den a" << n << "):" << endl;
    for (int i = 0; i <= n; i++) {
        cout << "a[" << i << "] = ";
        cin >> a[i];
    }
    
    cout << "Nhap gia tri x: ";
    cin >> x;
    
    // Hiển thị đa thức
    cout << "\nDa thuc: F(x) = ";
    for (int i = n; i >= 0; i--) {
        if (i == 0) {
            cout << a[i];
        } else if (i == 1) {
            cout << a[i] << "x + ";
        } else {
            cout << a[i] << "x^" << i << " + ";
        }
    }
    cout << endl;
    
    double ketQua1 = tinhDaThuc(a, n, x);
    double ketQua2 = tinhDaThucHorner(a, n, x);
    
    cout << "\nF(" << x << ") = " << ketQua1 << " (cach 1)" << endl;
    cout << "F(" << x << ") = " << ketQua2 << " (Horner)" << endl;
    
    return 0;
}
