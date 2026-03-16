#include <iostream>
using namespace std;

int main() {
    float so, tong = 0;
    int count = 0;
    
    cout << "Nhap cac so (nhap 9999 de ket thuc): " << endl;
    
    while (true) {
        cin >> so;
        if (so == 9999) {
            break;
        }
        tong += so;
        count++;
    }
    
    if (count > 0) {
        float trungBinh = tong / count;
        cout << "Trung binh cong: " << trungBinh << endl;
    } else {
        cout << "Khong co so nao duoc nhap!" << endl;
    }
    
    return 0;
}
