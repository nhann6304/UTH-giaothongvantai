#include <iostream>
using namespace std;

int main() {
    int tnct;
    double heSo, luongCanBan = 650000, luong;
    
    cout << "Nhap vao tham nien cong tac (thang): ";
    cin >> tnct;
    
    if (tnct < 12) {
        heSo = 1.92;
    } else if (tnct < 36) {
        heSo = 2.34;
    } else if (tnct < 60) {
        heSo = 3;
    } else {
        heSo = 4.5;
    }
    
    luong = heSo * luongCanBan;
    cout << "Luong cua nhan vien la: " << luong << " dong" << endl;
    
    return 0;
}
