#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 10;

// a. Nhập ma trận
void nhapMaTran(int a[][MAX], int &m, int &n) {
    cout << "Nhap so dong m (<=10): ";
    cin >> m;
    cout << "Nhap so cot n (<=10): ";
    cin >> n;
    
    if (m > MAX) m = MAX;
    if (n > MAX) n = MAX;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << "A[" << i << "][" << j << "] = ";
            cin >> a[i][j];
        }
    }
}

// a. Xuất ma trận
void xuatMaTran(int a[][MAX], int m, int n) {
    cout << "Ma tran A:" << endl;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << a[i][j] << "\t";
        }
        cout << endl;
    }
}

// b. Đếm số phần tử âm
int demSoAm(int a[][MAX], int m, int n) {
    int dem = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] < 0) dem++;
        }
    }
    return dem;
}

// c. Tìm giá trị lớn nhất
int timMax(int a[][MAX], int m, int n) {
    int max = a[0][0];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] > max) max = a[i][j];
        }
    }
    return max;
}

// d. Dòng có tổng lớn nhất
int dongTongMax(int a[][MAX], int m, int n) {
    int maxDong = 0;
    int maxTong = 0;
    
    for (int j = 0; j < n; j++) {
        maxTong += a[0][j];
    }
    
    for (int i = 1; i < m; i++) {
        int tong = 0;
        for (int j = 0; j < n; j++) {
            tong += a[i][j];
        }
        if (tong > maxTong) {
            maxTong = tong;
            maxDong = i;
        }
    }
    
    return maxDong;
}

// e. Sắp xếp từng dòng tăng dần
void sapXepTungDong(int a[][MAX], int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if (a[i][j] > a[i][k]) {
                    swap(a[i][j], a[i][k]);
                }
            }
        }
    }
}

// f. Sắp xếp toàn bộ ma trận giảm dần
void sapXepMaTranGiam(int a[][MAX], int m, int n) {
    int temp[MAX * MAX];
    int k = 0;
    
    // Chuyển ma trận thành mảng 1 chiều
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            temp[k++] = a[i][j];
        }
    }
    
    // Sắp xếp giảm dần
    for (int i = 0; i < k - 1; i++) {
        for (int j = i + 1; j < k; j++) {
            if (temp[i] < temp[j]) {
                swap(temp[i], temp[j]);
            }
        }
    }
    
    // Chuyển lại thành ma trận
    k = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            a[i][j] = temp[k++];
        }
    }
}

int main() {
    int a[MAX][MAX];
    int m, n, choice;
    
    nhapMaTran(a, m, n);
    xuatMaTran(a, m, n);
    
    do {
        cout << "\n===== MENU =====" << endl;
        cout << "1. Xuat ma tran" << endl;
        cout << "2. Dem so phan tu am" << endl;
        cout << "3. Tim gia tri lon nhat" << endl;
        cout << "4. Dong co tong lon nhat" << endl;
        cout << "5. Sap xep tung dong tang dan" << endl;
        cout << "6. Sap xep ma tran giam dan" << endl;
        cout << "0. Thoat" << endl;
        cout << "Chon: ";
        cin >> choice;
        
        switch(choice) {
            case 1:
                xuatMaTran(a, m, n);
                break;
            case 2:
                cout << "So phan tu am: " << demSoAm(a, m, n) << endl;
                break;
            case 3:
                cout << "Gia tri lon nhat: " << timMax(a, m, n) << endl;
                break;
            case 4:
                cout << "Dong co tong lon nhat: " << dongTongMax(a, m, n) << endl;
                break;
            case 5:
                sapXepTungDong(a, m, n);
                cout << "Da sap xep tung dong!" << endl;
                xuatMaTran(a, m, n);
                break;
            case 6:
                sapXepMaTranGiam(a, m, n);
                cout << "Da sap xep ma tran giam dan!" << endl;
                xuatMaTran(a, m, n);
                break;
        }
    } while (choice != 0);
    
    return 0;
}
