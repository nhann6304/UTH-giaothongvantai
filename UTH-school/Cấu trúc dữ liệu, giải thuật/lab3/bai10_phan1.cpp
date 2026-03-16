#include <iostream>
#include <cmath>
using namespace std;

// Hàm tính giai thừa
long long giaiThua(int n) {
    long long gt = 1;
    for (int i = 2; i <= n; i++) {
        gt *= i;
    }
    return gt;
}

// Hàm tính lũy thừa
double luythua(double x, int n) {
    double result = 1;
    for (int i = 0; i < n; i++) {
        result *= x;
    }
    return result;
}

// Hàm tính sin(x) gần đúng
// sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
double tinhSin(double x, double epsilon = 0.00001) {
    double sin_x = 0;
    double phanTu = x;
    int n = 1;
    
    while (abs(phanTu) >= epsilon) {
        sin_x += phanTu;
        phanTu = -phanTu * x * x / ((2 * n) * (2 * n + 1));
        n++;
    }
    
    return sin_x;
}

int main() {
    double x, epsilon;
    
    cout << "Nhap gia tri x (radian): ";
    cin >> x;
    cout << "Nhap sai so epsilon (vi du 0.00001): ";
    cin >> epsilon;
    
    double ketQua = tinhSin(x, epsilon);
    
    cout << "\nsin(" << x << ") gan dung = " << ketQua << endl;
    cout << "sin(" << x << ") thu vien = " << sin(x) << endl;
    cout << "Sai so: " << abs(ketQua - sin(x)) << endl;
    
    return 0;
}
