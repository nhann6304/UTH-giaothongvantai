#include <iostream>
using namespace std;

// Hàm tính chiều dài của số nguyên
int chieuDai(int n) {
    if (n == 0) return 1;
    
    int count = 0;
    if (n < 0) n = -n; // Xử lý số âm
    
    while (n != 0) {
        count++;
        n /= 10;
    }
    return count;
}

int main() {
    int n;
    cout << "Nhap so nguyen: ";
    cin >> n;
    
    cout << "Chieu dai cua so: " << chieuDai(n) << endl;
    
    return 0;
}
