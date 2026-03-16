#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap vao mot so nguyen duong: ";
    cin >> n;
    
    if (n < 2) {
        cout << n << " khong phai la so nguyen to" << endl;
        return 0;
    }
    
    bool laSoNguyenTo = true;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            laSoNguyenTo = false;
            break;
        }
    }
    
    if (laSoNguyenTo) {
        cout << n << " la so nguyen to" << endl;
    } else {
        cout << n << " khong phai la so nguyen to" << endl;
    }
    
    return 0;
}
