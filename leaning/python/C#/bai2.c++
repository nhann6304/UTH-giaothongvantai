#include <iostream>
using namespace std;

int main() {
    float a, b;
    
    cout << "Nhap chieu dai a: ";
    cin >> a;
    cout << "Nhap chieu rong b: ";
    cin >> b;
    
    float chuVi = 2 * (a + b);
    float dienTich = a * b;
    
    cout << "Chu vi hinh chu nhat: " << chuVi << endl;
    cout << "Dien tich hinh chu nhat: " << dienTich << endl;
    
    return 0;
}