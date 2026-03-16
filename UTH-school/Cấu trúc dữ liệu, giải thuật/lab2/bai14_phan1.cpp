#include <iostream>
using namespace std;

int main() {
    int maSo;
    double luong = 0;
    
    cout << "Nhap ma so nhan vien (1-Quan ly, 2-Cong nhan theo gio, 3-Cong nhan theo loi nhuan, 4-Cong nhan theo san pham): ";
    cin >> maSo;
    
    if (maSo == 1) {
        double X;
        cout << "Nhap luong co dinh X: ";
        cin >> X;
        luong = X;
    } else if (maSo == 2) {
        double Y, soGio;
        cout << "Nhap luong co ban Y: ";
        cin >> Y;
        cout << "Nhap so gio lam viec: ";
        cin >> soGio;
        
        if (soGio <= 40) {
            luong = soGio * Y;
        } else {
            luong = 40 * Y + (soGio - 40) * Y * 1.5;
        }
    } else if (maSo == 3) {
        double Z;
        cout << "Nhap doanh so ban hang Z: ";
        cin >> Z;
        luong = 500000 + Z * 0.07;
    } else if (maSo == 4) {
        int N;
        double S;
        cout << "Nhap so san pham N: ";
        cin >> N;
        cout << "Nhap don gia moi san pham S: ";
        cin >> S;
        luong = N * S;
    } else {
        cout << "Ma so khong hop le!" << endl;
        return 0;
    }
    
    cout << "Luong phai tra: " << luong << " dong" << endl;
    
    return 0;
}
