#include <iostream>
#include <cmath>
using namespace std;

int main() {
    float x, y, z;        
    float a, b, c, d;    
    
    cout << "=== NHAP TOA DO DIEM A ===" << endl;
    cout << "Nhap x: ";
    cin >> x;
    cout << "Nhap y: ";
    cin >> y;
    cout << "Nhap z: ";
    cin >> z;
    
    cout << "\n=== NHAP HE SO MAT PHANG (ax + by + cz + d = 0) ===" << endl;
    cout << "Nhap a: ";
    cin >> a;
    cout << "Nhap b: ";
    cin >> b;
    cout << "Nhap c: ";
    cin >> c;
    cout << "Nhap d: ";
    cin >> d;
    
    if (a == 0 && b == 0 && c == 0) {
        cout << "\nLoi: He so a, b, c khong the dong thoi bang 0!" << endl;
        return 1;
    }
    
    float tuSo = abs(a * x + b * y + c * z + d);
    float mauSo = sqrt(a * a + b * b + c * c);
    float khoangCach = tuSo / mauSo;
    
    cout << "\n===== KET QUA =====" << endl;
    cout << "Diem A(" << x << ", " << y << ", " << z << ")" << endl;
    cout << "Mat phang: " << a << "x + " << b << "y + " << c << "z + " << d << " = 0" << endl;
    cout << "Khoang cach tu A den mat phang: " << khoangCach << endl;
    
    return 0;
}