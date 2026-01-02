#include <iostream>
#include <cmath>
using namespace std;

int main() {
    float xA, yA, xB, yB;
    
    cout << "=== DIEM A ===" << endl;
    cout << "Nhap toa do xA: ";
    cin >> xA;
    cout << "Nhap toa do yA: ";
    cin >> yA;

    cout << "\n=== DIEM B ===" << endl;
    cout << "Nhap toa do xB: ";
    cin >> xB;
    cout << "Nhap toa do yB: ";
    cin >> yB;
    
    float doDaiAB = sqrt(pow(xB - xA, 2) + pow(yB - yA, 2));
    
    cout << "\n===== KET QUA =====" << endl;
    cout << "Diem A(" << xA << ", " << yA << ")" << endl;
    cout << "Diem B(" << xB << ", " << yB << ")" << endl;
    cout << "Do dai vector AB: " << doDaiAB << endl;
    
    return 0;
}