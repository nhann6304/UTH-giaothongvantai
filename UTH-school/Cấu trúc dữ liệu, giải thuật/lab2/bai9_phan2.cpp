#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

#define PI 3.14159265

int main() {
    cout << "BANG LUONG GIAC" << endl;
    cout << "===============================================" << endl;
    cout << setw(10) << "Goc (do)" << setw(15) << "Sin" << setw(15) << "Cos" << setw(15) << "Tan" << endl;
    cout << "===============================================" << endl;
    
    for (int goc = 0; goc <= 180; goc += 5) {
        double radian = goc * PI / 180.0;
        cout << setw(10) << goc 
             << setw(15) << fixed << setprecision(4) << sin(radian)
             << setw(15) << cos(radian);
        
        if (goc == 90) {
            cout << setw(15) << "Khong xac dinh";
        } else {
            cout << setw(15) << tan(radian);
        }
        cout << endl;
    }
    
    return 0;
}
