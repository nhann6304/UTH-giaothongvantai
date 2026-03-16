#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    // Phiên bản 1: Máy đoán số của người
    cout << "=== TRO CHOI DOAN SO - MAY DOAN ===" << endl;
    cout << "Ban hay nghi mot so tu 1 den 100" << endl;
    
    int min = 1, max = 100, n = 7;
    int lanDoan = 0;
    
    while (lanDoan < n) {
        lanDoan++;
        int soDoan = (min + max) / 2;
        
        cout << "\nLan doan thu " << lanDoan << ": May doan so " << soDoan << endl;
        cout << "So ban nghi lon hon (1), nho hon (2), hay bang (3) so may doan? ";
        
        int phanHoi;
        cin >> phanHoi;
        
        if (phanHoi == 3) {
            cout << "May da doan trung sau " << lanDoan << " lan!" << endl;
            return 0;
        } else if (phanHoi == 1) {
            min = soDoan + 1;
        } else {
            max = soDoan - 1;
        }
    }
    
    cout << "May da thua! Khong doan trung sau " << n << " lan." << endl;
    
    return 0;
}
