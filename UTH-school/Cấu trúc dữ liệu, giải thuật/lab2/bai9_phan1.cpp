#include <iostream>
using namespace std;

int main() {
    float diemTB;
    int soNgayNghi;
    
    cout << "Nhap diem trung binh: ";
    cin >> diemTB;
    cout << "Nhap so ngay nghi: ";
    cin >> soNgayNghi;
    
    if (diemTB >= 9.0 && soNgayNghi == 0) {
        cout << "Xep loai: Xuat sac" << endl;
    } else if (diemTB >= 8.0 && soNgayNghi <= 1) {
        cout << "Xep loai: Gioi" << endl;
    } else if (diemTB >= 6.5 && soNgayNghi <= 3) {
        cout << "Xep loai: Kha" << endl;
    } else if (diemTB >= 5.0 && soNgayNghi <= 5) {
        cout << "Xep loai: Trung binh" << endl;
    } else {
        cout << "Xep loai: Yeu" << endl;
    }
    
    return 0;
}
