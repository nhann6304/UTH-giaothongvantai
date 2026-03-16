#include <iostream>
using namespace std;

int main() {
    int n;
    long long gt = 1;
    
    cout << "Nhap n: ";
    cin >> n;
    
    // Xác định bắt đầu từ 1 (lẻ) hay 2 (chẵn)
    for (int i = (n % 2) ? 1 : 2; i <= n; i += 2) {
        gt *= i;
    }
    
    cout << n << "!! = " << gt << endl;
    
    return 0;
}
