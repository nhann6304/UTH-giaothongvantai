#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 100;

// Hàm nhập mảng
void nhapMang(int a[], int &n) {
    cout << "Nhap so phan tu (toi da " << MAX << "): ";
    cin >> n;
    if (n > MAX) n = MAX;
    
    for (int i = 0; i < n; i++) {
        cout << "a[" << i << "] = ";
        cin >> a[i];
    }
}

// Hàm xuất mảng
void xuatMang(int a[], int n) {
    cout << "Mang: ";
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}

// a. Kiểm tra mảng toàn số chẵn
bool laToanSoChan(int a[], int n) {
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 != 0) return false;
    }
    return true;
}

// b. Kiểm tra số nguyên tố
bool laSoNguyenTo(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

void hienThiSoNguyenTo(int a[], int n) {
    cout << "Cac so nguyen to: ";
    bool coSNT = false;
    for (int i = 0; i < n; i++) {
        if (laSoNguyenTo(a[i])) {
            cout << a[i] << " ";
            coSNT = true;
        }
    }
    if (!coSNT) cout << "Khong co";
    cout << endl;
}

// c. Kiểm tra mảng đã sắp xếp
void kiemTraSapXep(int a[], int n) {
    bool tang = true, giam = true;
    
    for (int i = 0; i < n - 1; i++) {
        if (a[i] > a[i + 1]) tang = false;
        if (a[i] < a[i + 1]) giam = false;
    }
    
    if (tang) cout << "Mang dang sap xep tang dan" << endl;
    else if (giam) cout << "Mang dang sap xep giam dan" << endl;
    else cout << "Mang chua duoc sap xep" << endl;
}

// d. Loại bỏ phần tử trùng
int loaiBoTrung(int a[], int n) {
    int newN = 0;
    for (int i = 0; i < n; i++) {
        bool trung = false;
        for (int j = 0; j < newN; j++) {
            if (a[i] == a[j]) {
                trung = true;
                break;
            }
        }
        if (!trung) {
            a[newN++] = a[i];
        }
    }
    return newN;
}

// e. So sánh số chẵn và số lẻ
void soSanhChanLe(int a[], int n) {
    int demChan = 0, demLe = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) demChan++;
        else demLe++;
    }
    
    cout << "So luong so chan: " << demChan << endl;
    cout << "So luong so le: " << demLe << endl;
    
    if (demChan > demLe) cout << "So chan nhieu hon so le" << endl;
    else if (demChan < demLe) cout << "So le nhieu hon so chan" << endl;
    else cout << "So chan bang so le" << endl;
}

// f. Chèn phần tử vào vị trí p
bool chenPhanTu(int a[], int &n, int x, int p) {
    if (n >= MAX) {
        cout << "Mang da day!" << endl;
        return false;
    }
    if (p < 0 || p > n) {
        cout << "Vi tri khong hop le!" << endl;
        return false;
    }
    
    for (int i = n; i > p; i--) {
        a[i] = a[i - 1];
    }
    a[p] = x;
    n++;
    return true;
}

// g. Tìm SNT đầu tiên mà phần tử trước là số chính phương
bool laSoChinhPhuong(int n) {
    if (n < 0) return false;
    int can = sqrt(n);
    return can * can == n;
}

int timSNTSauSCP(int a[], int n) {
    for (int i = 1; i < n; i++) {
        if (laSoChinhPhuong(a[i - 1]) && laSoNguyenTo(a[i])) {
            return a[i];
        }
    }
    return -1; // Không tìm thấy
}

// h. Tách số không phải SNT
int tachKhongSNT(int a[], int n, int b[]) {
    int m = 0;
    for (int i = 0; i < n; i++) {
        if (!laSoNguyenTo(a[i])) {
            b[m++] = a[i];
        }
    }
    return m;
}

// i. Sắp xếp nửa đầu tăng, nửa sau giảm
void sapXepNuaDau(int a[], int n) {
    int mid = n / 2;
    
    // Sắp xếp nửa đầu tăng dần
    for (int i = 0; i < mid - 1; i++) {
        for (int j = i + 1; j < mid; j++) {
            if (a[i] > a[j]) swap(a[i], a[j]);
        }
    }
    
    // Sắp xếp nửa sau giảm dần
    int start = (n % 2 == 0) ? mid : mid + 1;
    for (int i = start; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] < a[j]) swap(a[i], a[j]);
        }
    }
}

// k. Sắp xếp mảng giảm dần
void sapXepGiam(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] < a[j]) swap(a[i], a[j]);
        }
    }
}

// m. Chèn x vào mảng giảm dần
void chenVaoMangGiam(int a[], int &n, int x) {
    int pos = n;
    for (int i = 0; i < n; i++) {
        if (x > a[i]) {
            pos = i;
            break;
        }
    }
    chenPhanTu(a, n, x, pos);
}

// n. Kiểm tra mảng đối xứng
bool laDoiXung(int a[], int n) {
    for (int i = 0; i < n / 2; i++) {
        if (a[i] != a[n - 1 - i]) return false;
    }
    return true;
}

// l. Kiểm tra mảng tăng dần
bool laTangDan(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        if (a[i] >= a[i + 1]) return false;
    }
    return true;
}

int main() {
    int a[MAX], b[MAX], n, choice;
    
    nhapMang(a, n);
    xuatMang(a, n);
    
    do {
        cout << "\n===== MENU =====" << endl;
        cout << "a. Kiem tra toan so chan" << endl;
        cout << "b. Hien thi so nguyen to" << endl;
        cout << "c. Kiem tra sap xep" << endl;
        cout << "d. Loai bo phan tu trung" << endl;
        cout << "e. So sanh chan/le" << endl;
        cout << "f. Chen phan tu" << endl;
        cout << "g. Tim SNT sau SCP" << endl;
        cout << "h. Tach khong SNT" << endl;
        cout << "i. Sap xep nua dau/sau" << endl;
        cout << "k. Sap xep giam dan" << endl;
        cout << "m. Chen vao mang giam" << endl;
        cout << "n. Kiem tra doi xung" << endl;
        cout << "l. Kiem tra tang dan" << endl;
        cout << "0. Thoat" << endl;
        cout << "Chon: ";
        cin >> choice;
        
        switch(choice) {
            case 'a':
                cout << (laToanSoChan(a, n) ? "Mang toan so chan" : "Mang khong toan so chan") << endl;
                break;
            case 'b':
                hienThiSoNguyenTo(a, n);
                break;
            case 'c':
                kiemTraSapXep(a, n);
                break;
            case 'd': {
                int coTrung = n;
                n = loaiBoTrung(a, n);
                cout << "Da loai bo " << (coTrung - n) << " phan tu trung" << endl;
                xuatMang(a, n);
                break;
            }
            case 'e':
                soSanhChanLe(a, n);
                break;
            case 'f': {
                int x, p;
                cout << "Nhap gia tri x: ";
                cin >> x;
                cout << "Nhap vi tri p: ";
                cin >> p;
                if (chenPhanTu(a, n, x, p)) {
                    cout << "Chen thanh cong!" << endl;
                    xuatMang(a, n);
                }
                break;
            }
            case 'g': {
                int kq = timSNTSauSCP(a, n);
                if (kq != -1) cout << "SNT dau tien sau SCP: " << kq << endl;
                else cout << "Khong tim thay" << endl;
                break;
            }
            case 'h': {
                int m = tachKhongSNT(a, n, b);
                cout << "Cac so khong phai SNT: ";
                xuatMang(b, m);
                break;
            }
            case 'i':
                sapXepNuaDau(a, n);
                cout << "Da sap xep!" << endl;
                xuatMang(a, n);
                break;
            case 'k':
                sapXepGiam(a, n);
                cout << "Da sap xep giam dan!" << endl;
                xuatMang(a, n);
                break;
            case 'm': {
                int x;
                cout << "Nhap x: ";
                cin >> x;
                sapXepGiam(a, n); // Đảm bảo mảng giảm dần
                chenVaoMangGiam(a, n, x);
                cout << "Da chen!" << endl;
                xuatMang(a, n);
                break;
            }
            case 'n':
                cout << (laDoiXung(a, n) ? "Mang doi xung" : "Mang khong doi xung") << endl;
                break;
            case 'l':
                cout << (laTangDan(a, n) ? "Mang tang dan" : "Mang khong tang dan") << endl;
                break;
        }
    } while (choice != '0');
    
    return 0;
}
