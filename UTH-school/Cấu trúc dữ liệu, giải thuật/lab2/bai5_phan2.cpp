#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap vao mot so nguyen duong: ";
    cin >> n;
    
    cout << n << " = ";
    
    int temp = n;
    bool first = true;
    
    for (int i = 2; i <= temp; i++) {
        while (temp % i == 0) {
            if (!first) {
                cout << " x ";
            }
            cout << i;
            first = false;
            temp /= i;
        }
    }
    
    cout << endl;
    
    return 0;
}
