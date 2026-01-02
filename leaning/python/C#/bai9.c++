#include <iostream>
using namespace std;

int main() {
    int N;
    
    cout << "Nhap so nguyen N (4 chu so): ";
    cin >> N;
    
    if (N < 1000 || N > 9999) {
        cout << "So vua nhap khong phai la so 4 chu so!" << endl;
        return 1;
    }
    
    int donVi = N % 10;          
    int chuc = (N / 10) % 10;    
    int tram = (N / 100) % 10;   
    int nghin = N / 1000;       
    
    int tong = donVi + chuc + tram + nghin;
    
    cout << "So N = " << N << endl;
    cout << "Cac chu so: " << nghin << ", " << tram << ", " << chuc << ", " << donVi << endl;
    cout << "Tong cac chu so: " << tong << endl;
    
    return 0;
}