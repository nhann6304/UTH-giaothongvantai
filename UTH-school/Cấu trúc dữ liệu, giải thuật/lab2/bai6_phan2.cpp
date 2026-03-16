#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap so luong sinh vien: ";
    cin >> n;
    
    float tong = 0;
    for (int i = 1; i <= n; i++) {
        float diem;
        cout << "Nhap diem sinh vien thu " << i << ": ";
        cin >> diem;
        tong += diem;
    }
    
    float diemTB = tong / n;
    cout << "Diem trung binh cua " << n << " sinh vien la: " << diemTB << endl;
    
    return 0;
}
