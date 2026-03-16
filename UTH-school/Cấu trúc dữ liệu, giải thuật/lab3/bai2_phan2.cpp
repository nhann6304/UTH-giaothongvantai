#include <iostream>
using namespace std;

const int MAX = 100;

// Hàm nhập mảng
void nhapMang(int a[], int &n) {
    cout << "Nhap so phan tu: ";
    cin >> n;
    if (n > MAX) n = MAX;
    
    for (int i = 0; i < n; i++) {
        cout << "a[" << i << "] = ";
        cin >> a[i];
    }
}

// Hàm xuất mảng
void xuatMang(int a[], int n) {
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}

// Hàm trộn 2 mảng tăng dần thành 1 mảng tăng dần
int tronMang(int a[], int n, int b[], int m, int c[]) {
    int i = 0, j = 0, k = 0;
    
    // Trộn 2 mảng
    while (i < n && j < m) {
        if (a[i] <= b[j]) {
            c[k++] = a[i++];
        } else {
            c[k++] = b[j++];
        }
    }
    
    // Thêm phần còn lại của mảng a
    while (i < n) {
        c[k++] = a[i++];
    }
    
    // Thêm phần còn lại của mảng b
    while (j < m) {
        c[k++] = b[j++];
    }
    
    return k;
}

int main() {
    int a[MAX], b[MAX], c[MAX * 2];
    int n, m, p;
    
    cout << "Nhap mang A (tang dan):" << endl;
    nhapMang(a, n);
    
    cout << "\nNhap mang B (tang dan):" << endl;
    nhapMang(b, m);
    
    cout << "\nMang A: ";
    xuatMang(a, n);
    
    cout << "Mang B: ";
    xuatMang(b, m);
    
    p = tronMang(a, n, b, m, c);
    
    cout << "\nMang C (tron A va B): ";
    xuatMang(c, p);
    
    return 0;
}
