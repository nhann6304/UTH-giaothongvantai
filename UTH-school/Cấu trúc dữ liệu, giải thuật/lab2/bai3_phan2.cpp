#include <iostream>
using namespace std;

int main() {
    int count = 0;
    
    cout << "Cac so chia het cho 3 hoac 7 tu 1 den 100: " << endl;
    for (int i = 1; i <= 100; i++) {
        if (i % 3 == 0 || i % 7 == 0) {
            cout << i << " ";
            count++;
        }
    }
    
    cout << endl << "So luong: " << count << endl;
    
    return 0;
}
