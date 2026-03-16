#include <iostream>
using namespace std;

int main() {
    int a, b, c, d, max, min;
    cout << "Nhap vao 4 so: ";
    cin >> a >> b >> c >> d;
    
    // Tìm max
    max = a;
    if (b > max) max = b;
    if (c > max) max = c;
    if (d > max) max = d;
    
    // Tìm min
    min = a;
    if (b < min) min = b;
    if (c < min) min = c;
    if (d < min) min = d;
    
    cout << "So lon nhat la: " << max << endl;
    cout << "So nho nhat la: " << min << endl;
    
    return 0;
}
