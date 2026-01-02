#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    
    cout << "Nhap so nguyen a: ";
    cin >> a;
    cout << "Nhap so nguyen b: ";
    cin >> b;
    cout << "Nhap so nguyen c: ";
    cin >> c;
    
    int tong = a + b + c;
    int tich = a * b * c;
    
    cout << "Tong cua " << a << ", " << b << ", " << c << " la: " << tong << endl;
    cout << "Tich cua " << a << ", " << b << ", " << c << " la: " << tich << endl;
    
    return 0;
}