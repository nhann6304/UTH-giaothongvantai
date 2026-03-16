#include <iostream>
#include <cstring>
#include <cctype>
using namespace std;

const int MAX = 50;

// Hàm nhập mảng họ tên
void nhapHoTen(char fullName[][100], int &n) {
    cout << "Nhap so luong sinh vien (<50): ";
    cin >> n;
    if (n > MAX) n = MAX;
    cin.ignore();
    
    for (int i = 0; i < n; i++) {
        cout << "Nhap ho ten sinh vien " << (i + 1) << ": ";
        cin.getline(fullName[i], 100);
    }
}

// Hàm xuất mảng họ tên
void xuatHoTen(char fullName[][100], int n) {
    cout << "\nDanh sach sinh vien:" << endl;
    for (int i = 0; i < n; i++) {
        cout << (i + 1) << ". " << fullName[i] << endl;
    }
}

// a. Tách họ (phần đầu tiên)
void tachHo(char fullName[][100], int n, char firstName[][100]) {
    for (int i = 0; i < n; i++) {
        int j = 0;
        while (fullName[i][j] != ' ' && fullName[i][j] != '\0') {
            firstName[i][j] = fullName[i][j];
            j++;
        }
        firstName[i][j] = '\0';
    }
}

// b. Tách tên (phần cuối cùng)
void tachTen(char fullName[][100], int n, char lastName[][100]) {
    for (int i = 0; i < n; i++) {
        int len = strlen(fullName[i]);
        int j = len - 1;
        
        // Tìm khoảng trắng cuối cùng
        while (j >= 0 && fullName[i][j] != ' ') {
            j--;
        }
        
        // Sao chép tên
        strcpy(lastName[i], &fullName[i][j + 1]);
    }
}

// c. Sắp xếp theo tên
void sapXepTheoTen(char fullName[][100], int n) {
    char lastName[MAX][100];
    tachTen(fullName, n, lastName);
    
    // Sắp xếp bubble sort
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (strcmp(lastName[i], lastName[j]) > 0) {
                // Swap fullName
                char temp[100];
                strcpy(temp, fullName[i]);
                strcpy(fullName[i], fullName[j]);
                strcpy(fullName[j], temp);
                
                // Swap lastName
                strcpy(temp, lastName[i]);
                strcpy(lastName[i], lastName[j]);
                strcpy(lastName[j], temp);
            }
        }
    }
}

int main() {
    char fullName[MAX][100];
    char firstName[MAX][100];
    char lastName[MAX][100];
    int n, choice;
    
    nhapHoTen(fullName, n);
    xuatHoTen(fullName, n);
    
    do {
        cout << "\n===== MENU =====" << endl;
        cout << "1. Hien thi danh sach" << endl;
        cout << "2. Tach ho (firstName)" << endl;
        cout << "3. Tach ten (lastName)" << endl;
        cout << "4. Sap xep theo ten" << endl;
        cout << "0. Thoat" << endl;
        cout << "Chon: ";
        cin >> choice;
        
        switch(choice) {
            case 1:
                xuatHoTen(fullName, n);
                break;
            case 2:
                tachHo(fullName, n, firstName);
                cout << "\nDanh sach ho:" << endl;
                for (int i = 0; i < n; i++) {
                    cout << (i + 1) << ". " << firstName[i] << endl;
                }
                break;
            case 3:
                tachTen(fullName, n, lastName);
                cout << "\nDanh sach ten:" << endl;
                for (int i = 0; i < n; i++) {
                    cout << (i + 1) << ". " << lastName[i] << endl;
                }
                break;
            case 4:
                sapXepTheoTen(fullName, n);
                cout << "Da sap xep theo ten!" << endl;
                xuatHoTen(fullName, n);
                break;
        }
    } while (choice != 0);
    
    return 0;
}
