#include <iostream>
#include <cmath>
#include <iomanip> 

using namespace std;

int main() {
    double x;
    cout << "Nhap gia tri x (radian): ";
    cin >> x;

    double sum = 0;     
    double term = x;    
    int n = 0;         

    while (fabs(term) >= 1e-6) {
        sum += term; 
        
        term = term * (-x * x) / ((2 * n + 2) * (2 * n + 3));
        
        n++;
    }

    cout << "Gia tri gan dung cua sin(" << x << ") la: " << setprecision(7) << sum << endl;
    cout << "Gia tri thuc te (thu vien): " << sin(x) << endl;

    return 0;
}