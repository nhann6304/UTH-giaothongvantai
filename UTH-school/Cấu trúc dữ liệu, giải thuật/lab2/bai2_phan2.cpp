#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;
    
    // S = 1 + 2 + 3 + ... + n
    int S1 = 0;
    for (int i = 1; i <= n; i++) {
        S1 += i;
    }
    cout << "S1 = 1 + 2 + 3 + ... + " << n << " = " << S1 << endl;
    
    // S = 1 + 3 + 5 + 7 + ... + (2n + 1)
    int S2 = 0;
    for (int i = 0; i <= n; i++) {
        S2 += (2 * i + 1);
    }
    cout << "S2 = 1 + 3 + 5 + ... + " << (2*n+1) << " = " << S2 << endl;
    
    // S = n!
    long long S3 = 1;
    for (int i = 1; i <= n; i++) {
        S3 *= i;
    }
    cout << "S3 = " << n << "! = " << S3 << endl;
    
    // S = 1/(2*3) + 1/(3*4) + 1/(4*5) + ... + 1/(n*(n+1))
    double S4 = 0;
    for (int i = 2; i <= n; i++) {
        S4 += 1.0 / (i * (i + 1));
    }
    cout << "S4 = 1/(2*3) + 1/(3*4) + ... + 1/(" << n << "*" << (n+1) << ") = " << S4 << endl;
    
    return 0;
}
