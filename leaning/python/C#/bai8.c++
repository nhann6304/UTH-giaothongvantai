#include <iostream>
using namespace std;

int main() {
    float soKm;
    
    cout << "Nhap so Km da di: ";
    cin >> soKm;
    
    float tienCuoc = 0;
    
    if (soKm <= 0) {
        tienCuoc = 0;
    } else if (soKm <= 1) {
        tienCuoc = soKm * 15000;
    } else {
        tienCuoc = 15000 + (soKm - 1) * 12000;
    }
    
    float thueVAT = tienCuoc * 0.10;
    float tongTien = tienCuoc + thueVAT;
    
    cout << "So Km da di: " << soKm << " km" << endl;
    cout << "Tien cuoc: " << tienCuoc << " VND" << endl;
    cout << "Thue VAT (10%): " << thueVAT << " VND" << endl;
    cout << "------------------------" << endl;
    cout << "TONG TIEN: " << tongTien << " VND" << endl;
    
    return 0;
}