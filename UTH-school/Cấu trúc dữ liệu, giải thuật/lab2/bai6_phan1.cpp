#include <iostream>
using namespace std;

int main() {
    int ngay, thang, nam = 2024; // Năm hiện tại
    int soNgayTrongThang;
    
    cout << "Nhap ngay: ";
    cin >> ngay;
    cout << "Nhap thang: ";
    cin >> thang;
    
    // Kiểm tra tính hợp lệ của tháng
    if (thang < 1 || thang > 12) {
        cout << "Thang khong hop le!" << endl;
        return 0;
    }
    
    // Xác định số ngày trong tháng
    if (thang == 2) {
        soNgayTrongThang = 28;
    } else if (thang == 4 || thang == 6 || thang == 9 || thang == 11) {
        soNgayTrongThang = 30;
    } else {
        soNgayTrongThang = 31;
    }
    
    // Kiểm tra tính hợp lệ của ngày
    if (ngay < 1 || ngay > soNgayTrongThang) {
        cout << "Ngay khong hop le!" << endl;
        return 0;
    }
    
    cout << "Ngay thang hop le!" << endl;
    
    // Xác định quý
    if (thang >= 1 && thang <= 3) {
        cout << "Thang nay thuoc quy 1" << endl;
    } else if (thang >= 4 && thang <= 6) {
        cout << "Thang nay thuoc quy 2" << endl;
    } else if (thang >= 7 && thang <= 9) {
        cout << "Thang nay thuoc quy 3" << endl;
    } else {
        cout << "Thang nay thuoc quy 4" << endl;
    }
    
    cout << "Thang " << thang << " co " << soNgayTrongThang << " ngay" << endl;
    
    // Ngày hôm sau
    int ngayMoi = ngay + 1;
    int thangMoi = thang;
    if (ngayMoi > soNgayTrongThang) {
        ngayMoi = 1;
        thangMoi++;
        if (thangMoi > 12) {
            thangMoi = 1;
        }
    }
    cout << "Ngay hom sau la: " << ngayMoi << "/" << thangMoi << endl;
    
    // Ngày hôm trước
    ngayMoi = ngay - 1;
    thangMoi = thang;
    if (ngayMoi < 1) {
        thangMoi--;
        if (thangMoi < 1) {
            thangMoi = 12;
        }
        // Xác định số ngày của tháng trước
        if (thangMoi == 2) {
            ngayMoi = 28;
        } else if (thangMoi == 4 || thangMoi == 6 || thangMoi == 9 || thangMoi == 11) {
            ngayMoi = 30;
        } else {
            ngayMoi = 31;
        }
    }
    cout << "Ngay hom truoc la: " << ngayMoi << "/" << thangMoi << endl;
    
    return 0;
}
