#include <iostream>
using namespace std;

// Hàm tìm số đảo ngược
int soDao(int n) {
    int dao = 0;
    while (n != 0) {
        dao = dao * 10 + n % 10;
        n /= 10;
    }
    return dao;
}

int main() {
    int n;
    cout << "Nhap so nguyen: ";
    cin >> n;
    
    cout << "So dao nguoc: " << soDao(n) << endl;
    
    return 0;
}
