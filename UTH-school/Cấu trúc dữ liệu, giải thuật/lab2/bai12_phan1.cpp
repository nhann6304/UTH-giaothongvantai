#include <iostream>
using namespace std;

int main() {
    char c;
    cout << "Nhap vao mot ky tu: ";
    cin >> c;
    
    if (c >= 'A' && c <= 'Z') {
        cout << "Day la ky tu chu in hoa" << endl;
    } else if (c >= 'a' && c <= 'z') {
        cout << "Day la ky tu chu thuong" << endl;
    } else if (c >= '0' && c <= '9') {
        cout << "Day la ky tu so" << endl;
    } else {
        cout << "Day la ky tu dac biet" << endl;
    }
    
    return 0;
}
