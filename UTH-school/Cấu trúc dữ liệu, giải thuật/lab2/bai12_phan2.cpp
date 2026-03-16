#include <iostream>
using namespace std;

int main() {
    int N;
    int menhGia[] = {500, 200, 100, 50, 20, 10, 5, 2, 1};
    int soTo[9] = {0};
    
    cout << "Nhap so tien can doi (nghin dong): ";
    cin >> N;
    
    cout << "\nChi tiet doi tien:" << endl;
    for (int i = 0; i < 9; i++) {
        if (N >= menhGia[i]) {
            soTo[i] = N / menhGia[i];
            N = N % menhGia[i];
            cout << "To " << menhGia[i] << " nghin: " << soTo[i] << " to" << endl;
        }
    }
    
    return 0;
}
