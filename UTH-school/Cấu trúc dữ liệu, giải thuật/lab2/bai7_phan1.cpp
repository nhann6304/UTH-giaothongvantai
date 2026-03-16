#include <iostream>
using namespace std;

int main() {
    int a, b, c, max, min;
    cout << "Nhap vao 3 so: ";
    cin >> a >> b >> c;
    
    // Tìm max
    max = a;
    if (b > max) max = b;
    if (c > max) max = c;
    
    // Tìm min
    min = a;
    if (b < min) min = b;
    if (c < min) min = c;
    
    cout << "So lon nhat la: " << max << endl;
    cout << "So nho nhat la: " << min << endl;
    
    return 0;
}
