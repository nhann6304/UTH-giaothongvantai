#include <iostream>
#include <cmath>
using namespace std;

int main() {
    float a, b, c;
    cout << "Giai phuong trinh bac 2: ax^2 + bx + c = 0" << endl;
    cout << "Nhap a: ";
    cin >> a;
    cout << "Nhap b: ";
    cin >> b;
    cout << "Nhap c: ";
    cin >> c;
    
    if (a == 0) {
        // Phương trình bậc nhất
        if (b == 0) {
            if (c == 0) {
                cout << "Phuong trinh vo so nghiem" << endl;
            } else {
                cout << "Phuong trinh vo nghiem" << endl;
            }
        } else {
            float x = -c / b;
            cout << "Phuong trinh co nghiem x = " << x << endl;
        }
    } else {
        float delta = b * b - 4 * a * c;
        
        if (delta < 0) {
            cout << "Phuong trinh vo nghiem" << endl;
        } else if (delta == 0) {
            float x = -b / (2 * a);
            cout << "Phuong trinh co nghiem kep x = " << x << endl;
        } else {
            float x1 = (-b + sqrt(delta)) / (2 * a);
            float x2 = (-b - sqrt(delta)) / (2 * a);
            cout << "Phuong trinh co 2 nghiem phan biet:" << endl;
            cout << "x1 = " << x1 << endl;
            cout << "x2 = " << x2 << endl;
        }
    }
    
    return 0;
}
