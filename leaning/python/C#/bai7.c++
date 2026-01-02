#include <iostream>
#include <cmath>
using namespace std;

// Ham tinh khoang cach giua 2 diem
float khoangCach(float x1, float y1, float x2, float y2) {
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

int main() {
    float xA, yA, xB, yB, xC, yC;
    
    cout << "=== DINH A ===" << endl;
    cout << "Nhap toa do xA: ";
    cin >> xA;
    cout << "Nhap toa do yA: ";
    cin >> yA;
    
    cout << "\n=== DINH B ===" << endl;
    cout << "Nhap toa do xB: ";
    cin >> xB;
    cout << "Nhap toa do yB: ";
    cin >> yB;
    
    cout << "\n=== DINH C ===" << endl;
    cout << "Nhap toa do xC: ";
    cin >> xC;
    cout << "Nhap toa do yC: ";
    cin >> yC;
    
    float a = khoangCach(xB, yB, xC, yC);  
    float b = khoangCach(xA, yA, xC, yC); 
    float c = khoangCach(xA, yA, xB, yB);  
    
    float chuVi = a + b + c;
    
    float p = chuVi / 2;  
    float dienTich = sqrt(p * (p - a) * (p - b) * (p - c));
    
    // Xuat ket qua
    cout << "Diem A(" << xA << ", " << yA << ")" << endl;
    cout << "Diem B(" << xB << ", " << yB << ")" << endl;
    cout << "Diem C(" << xC << ", " << yC << ")" << endl;
    cout << "Canh AB = " << c << endl;
    cout << "Canh BC = " << a << endl;
    cout << "Canh CA = " << b << endl;
    cout << "Chu vi tam giac: " << chuVi << endl;
    cout << "Dien tich tam giac: " << dienTich << endl;
    
    return 0;
}