#include <iostream>
using namespace std;

int main() {
    int a, b, c, max;
    cout << "Nhap vao 3 so nguyen: ";
    cin >> a >> b >> c;
    
    max = a;
    if (b > max) {
        max = b;
    }
    if (c > max) {
        max = c;
    }
    
    cout << "So lon nhat la: " << max << endl;
    
    return 0;
}
