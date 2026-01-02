#include <iostream>
#include <cmath>
using namespace std;

int main() {
    float a;
    
    cout << "Nhap canh a cua hinh vuong: ";
    cin >> a;
    
    float chuVi = 4 * a;
    float dienTich = a * a;
    float duongCheo = a * sqrt(2);
    
    cout << "\n===== KET QUA =====" << endl;
    cout << "Canh hinh vuong a = " << a << endl;
    cout << "Chu vi hinh vuong: " << chuVi << endl;
    cout << "Dien tich hinh vuong: " << dienTich << endl;
    cout << "Duong cheo hinh vuong: " << duongCheo << endl;
    
    return 0;
}