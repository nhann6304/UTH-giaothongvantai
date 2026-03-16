#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap vao mot so: ";
    cin >> n;
    
    if (n % 2 == 0) {
        cout << "so chan" << endl;
    } else {
        cout << "so le" << endl;
    }
    
    return 0;
}
