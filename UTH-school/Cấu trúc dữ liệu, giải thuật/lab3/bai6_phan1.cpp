#include <iostream>
using namespace std;

// Hàm tính UCLN bằng thuật toán Euclid
int UCLN(int a, int b) {
    a = abs(a);
    b = abs(b);
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int a, b, c;
    cout << "Nhap 3 so nguyen a, b, c: ";
    cin >> a >> b >> c;
    
    int S = UCLN(a, b) + UCLN(b, c) + UCLN(a, c);
    
    cout << "S = UCLN(" << a << "," << b << ") + UCLN(" << b << "," << c << ") + UCLN(" << a << "," << c << ")" << endl;
    cout << "S = " << UCLN(a, b) << " + " << UCLN(b, c) << " + " << UCLN(a, c) << endl;
    cout << "S = " << S << endl;
    
    return 0;
}
