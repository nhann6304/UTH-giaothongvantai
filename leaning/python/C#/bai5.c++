#include <iostream>
using namespace std;

int main() {
    float diemToan, diemLy, diemHoa;
    int hsToan, hsLy, hsHoa;
    
    cout << "=== MON TOAN ===" << endl;
    cout << "Nhap diem Toan: ";
    cin >> diemToan;
    cout << "Nhap he so Toan: ";
    cin >> hsToan;
    
    cout << "\n=== MON LY ===" << endl;
    cout << "Nhap diem Ly: ";
    cin >> diemLy;
    cout << "Nhap he so Ly: ";
    cin >> hsLy;
    
    cout << "\n=== MON HOA ===" << endl;
    cout << "Nhap diem Hoa: ";
    cin >> diemHoa;
    cout << "Nhap he so Hoa: ";
    cin >> hsHoa;
    
    // Tinh diem trung binh
    float diemTB = (diemToan * hsToan + diemLy * hsLy + diemHoa * hsHoa) 
                   / (hsToan + hsLy + hsHoa);
    
    // Xuat ket qua
    cout << "\n===== KET QUA =====" << endl;
    cout << "Diem trung binh cua sinh vien: " << diemTB << endl;
    
    return 0;
}