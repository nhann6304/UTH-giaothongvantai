#include <iostream>
using namespace std;

int main() {
    int tu1, mau1, tu2, mau2;
    
    cout << "Nhap phan so thu nhat (tu mau): ";
    cin >> tu1 >> mau1;
    
    if (mau1 == 0) {
        cout << "Mau so phan so thu nhat phai khac 0!" << endl;
        return 0;
    }
    
    cout << "Nhap phan so thu hai (tu mau): ";
    cin >> tu2 >> mau2;
    
    if (mau2 == 0) {
        cout << "Mau so phan so thu hai phai khac 0!" << endl;
        return 0;
    }
    
    // Tổng
    int tuTong = tu1 * mau2 + tu2 * mau1;
    int mauTong = mau1 * mau2;
    cout << "Tong: " << tuTong << "/" << mauTong << endl;
    
    // Hiệu
    int tuHieu = tu1 * mau2 - tu2 * mau1;
    int mauHieu = mau1 * mau2;
    cout << "Hieu: " << tuHieu << "/" << mauHieu << endl;
    
    // Tích
    int tuTich = tu1 * tu2;
    int mauTich = mau1 * mau2;
    cout << "Tich: " << tuTich << "/" << mauTich << endl;
    
    // Thương
    if (tu2 == 0) {
        cout << "Khong the chia cho phan so co tu bang 0!" << endl;
    } else {
        int tuThuong = tu1 * mau2;
        int mauThuong = mau1 * tu2;
        cout << "Thuong: " << tuThuong << "/" << mauThuong << endl;
    }
    
    return 0;
}
