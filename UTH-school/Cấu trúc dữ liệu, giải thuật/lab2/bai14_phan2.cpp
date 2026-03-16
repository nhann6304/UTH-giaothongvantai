#include <iostream>
using namespace std;

int main() {
    float xA, yA, xB, yB, xC, yC;
    
    cout << "Nhap toa do diem A (x y): ";
    cin >> xA >> yA;
    cout << "Nhap toa do diem B (x y): ";
    cin >> xB >> yB;
    cout << "Nhap toa do diem C (x y): ";
    cin >> xC >> yC;
    
    // Kiểm tra A và B có trùng nhau không
    if (xA == xB && yA == yB) {
        cout << "Hai diem A va B trung nhau, khong the tao duong thang!" << endl;
        return 0;
    }
    
    // Phương trình đường thẳng qua A, B có dạng: ax + by + c = 0
    // Với a = yB - yA, b = xA - xB, c = xB*yA - xA*yB
    float a = yB - yA;
    float b = xA - xB;
    float c = xB * yA - xA * yB;
    
    cout << "\nPhuong trinh duong thang d qua A va B:" << endl;
    
    if (b == 0) {
        cout << "x = " << -c/a << endl;
    } else if (a == 0) {
        cout << "y = " << -c/b << endl;
    } else {
        cout << a << "x + " << b << "y + " << c << " = 0" << endl;
        // Hoặc dạng y = mx + n
        float m = -a / b;
        float n = -c / b;
        cout << "Hoac: y = " << m << "x + " << n << endl;
    }
    
    // Kiểm tra vị trí của C so với đường thẳng d
    float ketQua = a * xC + b * yC + c;
    
    cout << "\nVi tri cua diem C so voi duong thang d:" << endl;
    if (ketQua == 0) {
        cout << "Diem C nam tren duong thang d" << endl;
    } else if (ketQua > 0) {
        cout << "Diem C nam ve mot phia cua duong thang d (phia duong)" << endl;
    } else {
        cout << "Diem C nam ve mot phia cua duong thang d (phia am)" << endl;
    }
    
    return 0;
}
