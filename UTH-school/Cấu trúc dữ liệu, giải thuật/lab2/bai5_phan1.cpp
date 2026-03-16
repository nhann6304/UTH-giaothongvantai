#include <iostream>
using namespace std;

int main() {
    int gioBatDau, gioKetThuc;
    double soGio, tienPhaiTra;
    
    cout << "Nhap gio bat dau (8-24): ";
    cin >> gioBatDau;
    cout << "Nhap gio ket thuc (8-24): ";
    cin >> gioKetThuc;
    
    soGio = gioKetThuc - gioBatDau;
    
    // Tính tiền
    if (soGio <= 3) {
        tienPhaiTra = soGio * 30000;
    } else {
        tienPhaiTra = 3 * 30000 + (soGio - 3) * 30000 * 0.7;
    }
    
    // Giảm giá 10% nếu thuê từ 8-17h
    if (gioBatDau >= 8 && gioKetThuc <= 17) {
        tienPhaiTra = tienPhaiTra * 0.9;
    }
    
    cout << "So tien khach hang phai tra: " << tienPhaiTra << " dong" << endl;
    
    return 0;
}
