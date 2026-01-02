#include <iostream>
using namespace std;

int main() {
    int soLuong;
    float donGia;
    
    cout << "Nhap so luong: ";
    cin >> soLuong;
    cout << "Nhap don gia: ";
    cin >> donGia;
    
    // Tinh tien va thue
    float tien = soLuong * donGia;
    float thueVAT = tien * 0.10;  
    float tongTien = tien + thueVAT;
    
    cout << "\n===== KET QUA =====" << endl;
    cout << "Tien hang: " << tien << " VND" << endl;
    cout << "Thue VAT (10%): " << thueVAT << " VND" << endl;
    cout << "Tong tien phai tra: " << tongTien << " VND" << endl;
    
    return 0;
}