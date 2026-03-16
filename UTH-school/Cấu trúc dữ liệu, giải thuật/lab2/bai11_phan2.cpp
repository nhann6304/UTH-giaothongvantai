#include <iostream>
using namespace std;

int main() {
    cout << "CAC KY TU ASCII TU 33 DEN 255" << endl;
    cout << "==============================" << endl;
    
    for (int i = 33; i <= 255; i++) {
        cout << "Ma " << i << ": " << (char)i << "\t";
        if (i % 5 == 0) {
            cout << endl;
        }
    }
    
    cout << endl;
    
    return 0;
}
