#include <iostream>
using namespace std;

int main() {
    int M, N;
    cout << "Nhap so M: ";
    cin >> M;
    cout << "Nhap so N: ";
    cin >> N;
    
    // Tính UCLN (Ước chung lớn nhất) bằng thuật toán Euclid
    int a = M, b = N;
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    int UCLN = a;
    
    // Tính BCNN (Bội chung nhỏ nhất)
    int BCNN = (M * N) / UCLN;
    
    cout << "UCLN cua " << M << " va " << N << " la: " << UCLN << endl;
    cout << "BCNN cua " << M << " va " << N << " la: " << BCNN << endl;
    
    return 0;
}
