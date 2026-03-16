#include <iostream>
#include <map>
using namespace std;

const int MAX = 10;

// a. Nhập ma trận vuông
void nhapMaTran(int a[][MAX], int &n) {
    cout << "Nhap cap cua ma tran vuong n (<=10): ";
    cin >> n;
    if (n > MAX) n = MAX;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << "A[" << i << "][" << j << "] = ";
            cin >> a[i][j];
        }
    }
}

// a. Xuất ma trận
void xuatMaTran(int a[][MAX], int n) {
    cout << "Ma tran A:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << a[i][j] << "\t";
        }
        cout << endl;
    }
}

// b. Tổng ngoài đường chéo chính
int tongNgoaiCheoChinh(int a[][MAX], int n) {
    int tong = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j) tong += a[i][j];
        }
    }
    return tong;
}

// c. Max trên đường chéo chính
int maxCheoChinh(int a[][MAX], int n) {
    int max = a[0][0];
    for (int i = 1; i < n; i++) {
        if (a[i][i] > max) max = a[i][i];
    }
    return max;
}

// d. Đếm số âm trên đường chéo phụ
int demAmCheoPhu(int a[][MAX], int n) {
    int dem = 0;
    for (int i = 0; i < n; i++) {
        if (a[i][n - 1 - i] < 0) dem++;
    }
    return dem;
}

// e. Kiểm tra số nguyên tố
bool laSoNguyenTo(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int demSoNguyenTo(int a[][MAX], int n) {
    int dem = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (laSoNguyenTo(a[i][j])) dem++;
        }
    }
    return dem;
}

// f. Tìm số xuất hiện nhiều nhất
void timSoXuatHienNhieuNhat(int a[][MAX], int n) {
    map<int, int> dem;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dem[a[i][j]]++;
        }
    }
    
    int maxLan = 0;
    for (auto p : dem) {
        if (p.second > maxLan) maxLan = p.second;
    }
    
    cout << "Cac so xuat hien nhieu nhat (" << maxLan << " lan): ";
    for (auto p : dem) {
        if (p.second == maxLan) {
            cout << p.first << " ";
        }
    }
    cout << endl;
}

// g. Liệt kê dòng có nhiều số chẵn nhất
void dongNhieuSoChanNhat(int a[][MAX], int n) {
    int maxChan = 0;
    int demChan[MAX] = {0};
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] % 2 == 0) demChan[i]++;
        }
        if (demChan[i] > maxChan) maxChan = demChan[i];
    }
    
    cout << "Cac dong co nhieu so chan nhat (" << maxChan << " so): ";
    for (int i = 0; i < n; i++) {
        if (demChan[i] == maxChan) {
            cout << i << " ";
        }
    }
    cout << endl;
}

// h. Liệt kê dòng có nhiều SNT nhất
void dongNhieuSNTNhat(int a[][MAX], int n) {
    int maxSNT = 0;
    int demSNT[MAX] = {0};
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (laSoNguyenTo(a[i][j])) demSNT[i]++;
        }
        if (demSNT[i] > maxSNT) maxSNT = demSNT[i];
    }
    
    cout << "Cac dong co nhieu SNT nhat (" << maxSNT << " so): ";
    for (int i = 0; i < n; i++) {
        if (demSNT[i] == maxSNT) {
            cout << i << " ";
        }
    }
    cout << endl;
}

// j. Tổng đường biên
int tongDuongBien(int a[][MAX], int n) {
    int tong = 0;
    
    // Dòng đầu và dòng cuối
    for (int j = 0; j < n; j++) {
        tong += a[0][j];
        if (n > 1) tong += a[n - 1][j];
    }
    
    // Cột đầu và cột cuối (trừ góc đã tính)
    for (int i = 1; i < n - 1; i++) {
        tong += a[i][0];
        if (n > 1) tong += a[i][n - 1];
    }
    
    return tong;
}

int main() {
    int a[MAX][MAX];
    int n, choice;
    
    nhapMaTran(a, n);
    xuatMaTran(a, n);
    
    do {
        cout << "\n===== MENU =====" << endl;
        cout << "1. Xuat ma tran" << endl;
        cout << "2. Tong ngoai duong cheo chinh" << endl;
        cout << "3. Max tren duong cheo chinh" << endl;
        cout << "4. Dem so am tren duong cheo phu" << endl;
        cout << "5. Dem so nguyen to" << endl;
        cout << "6. Tim so xuat hien nhieu nhat" << endl;
        cout << "7. Dong co nhieu so chan nhat" << endl;
        cout << "8. Dong co nhieu SNT nhat" << endl;
        cout << "9. Tong duong bien" << endl;
        cout << "0. Thoat" << endl;
        cout << "Chon: ";
        cin >> choice;
        
        switch(choice) {
            case 1:
                xuatMaTran(a, n);
                break;
            case 2:
                cout << "Tong ngoai duong cheo chinh: " << tongNgoaiCheoChinh(a, n) << endl;
                break;
            case 3:
                cout << "Max tren duong cheo chinh: " << maxCheoChinh(a, n) << endl;
                break;
            case 4:
                cout << "So luong so am tren duong cheo phu: " << demAmCheoPhu(a, n) << endl;
                break;
            case 5:
                cout << "So luong so nguyen to: " << demSoNguyenTo(a, n) << endl;
                break;
            case 6:
                timSoXuatHienNhieuNhat(a, n);
                break;
            case 7:
                dongNhieuSoChanNhat(a, n);
                break;
            case 8:
                dongNhieuSNTNhat(a, n);
                break;
            case 9:
                cout << "Tong duong bien: " << tongDuongBien(a, n) << endl;
                break;
        }
    } while (choice != 0);
    
    return 0;
}
