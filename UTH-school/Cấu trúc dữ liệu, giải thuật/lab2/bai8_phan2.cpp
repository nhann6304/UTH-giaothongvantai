#include <iostream>
using namespace std;

int main() {
    cout << "BANG CUU CHUONG" << endl;
    cout << "===============" << endl;
    
    for (int i = 1; i <= 10; i++) {
        cout << "\nBang cuu chuong " << i << ":" << endl;
        for (int j = 1; j <= 10; j++) {
            cout << i << " x " << j << " = " << (i * j) << endl;
        }
    }
    
    return 0;
}
