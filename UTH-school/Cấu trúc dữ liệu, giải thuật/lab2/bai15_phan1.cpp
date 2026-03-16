#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap vao mot so nguyen co 3 chu so: ";
    cin >> n;
    
    if (n < 100 || n > 999) {
        cout << "So nhap vao khong phai la so co 3 chu so!" << endl;
        return 0;
    }
    
    int tram = n / 100;
    int chuc = (n / 10) % 10;
    int donvi = n % 10;
    
    string docTram[] = {"", "mot tram", "hai tram", "ba tram", "bon tram", "nam tram", "sau tram", "bay tram", "tam tram", "chin tram"};
    string docChuc[] = {"", "muoi", "hai muoi", "ba muoi", "bon muoi", "nam muoi", "sau muoi", "bay muoi", "tam muoi", "chin muoi"};
    string docDonVi[] = {"", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"};
    
    cout << docTram[tram];
    
    if (chuc == 0 && donvi != 0) {
        cout << " linh " << docDonVi[donvi];
    } else if (chuc == 1) {
        cout << " muoi";
        if (donvi == 5) {
            cout << " lam";
        } else if (donvi != 0) {
            cout << " " << docDonVi[donvi];
        }
    } else if (chuc != 0) {
        cout << " " << docChuc[chuc];
        if (donvi == 1) {
            cout << " mot";
        } else if (donvi == 5) {
            cout << " lam";
        } else if (donvi != 0) {
            cout << " " << docDonVi[donvi];
        }
    }
    
    cout << endl;
    
    return 0;
}
