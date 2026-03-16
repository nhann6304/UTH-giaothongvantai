#include <iostream>
using namespace std;

// Hàm tính UCLN
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

// Hàm tính BCNN
int BCNN(int a, int c) {
    return abs(a * c) / UCLN(a, c);
}

int main() {
    int a, b, c;
    cout << "Nhap 3 so nguyen a, b, c: ";
    cin >> a >> b >> c;
    
    int S = UCLN(a, b) + BCNN(a, c);
    
    cout << "S = UCLN(" << a << "," << b << ") + BCNN(" << a << "," << c << ")" << endl;
    cout << "S = " << UCLN(a, b) << " + " << BCNN(a, c) << endl;
    cout << "S = " << S << endl;
    
    return 0;
}
