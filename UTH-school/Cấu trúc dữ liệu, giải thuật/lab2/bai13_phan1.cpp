#include <iostream>
using namespace std;

int main() {
    int soDien;
    double tienDien = 0;
    
    cout << "Nhap so dien tieu thu (kWh): ";
    cin >> soDien;
    
    if (soDien <= 100) {
        tienDien = soDien * 550;
    } else if (soDien <= 150) {
        tienDien = 100 * 550 + (soDien - 100) * 900;
    } else if (soDien <= 200) {
        tienDien = 100 * 550 + 50 * 900 + (soDien - 150) * 1250;
    } else if (soDien <= 300) {
        tienDien = 100 * 550 + 50 * 900 + 50 * 1250 + (soDien - 200) * 1450;
    } else {
        tienDien = 100 * 550 + 50 * 900 + 50 * 1250 + 100 * 1450 + (soDien - 300) * 1700;
    }
    
    // Thuế VAT 10%
    tienDien = tienDien * 1.1;
    
    cout << "So tien phai tra: " << tienDien << " VND" << endl;
    
    return 0;
}
