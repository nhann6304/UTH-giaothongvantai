#include <iostream>
#include <string>
#include <iomanip>
#include <cstdlib>

using namespace std;

struct SinhVien {
    int id;
    string ten;
    int tuoi;
    double diemTB;
};

// Nhap thong tin sinh vien
void inputSV(SinhVien* s, int n) {
    for (int i = 0; i < n; i++) {
        cout << "\n--- Sinh vien thu " << i + 1 << " ---\n";
        cout << "Nhap ID: ";
        cin >> s[i].id;
        cin.ignore();
        cout << "Nhap ten: ";
        getline(cin, s[i].ten);
        cout << "Nhap tuoi: ";
        cin >> s[i].tuoi;
        cout << "Nhap diem trung binh: ";
        cin >> s[i].diemTB;
    }
}

// Hien thi 1 sinh vien
void displayOneSV(SinhVien s) {
    cout << "| " << setw(6) << s.id
         << " | " << setw(25) << left << s.ten << right
         << " | " << setw(5) << s.tuoi
         << " | " << setw(8) << fixed << setprecision(2) << s.diemTB
         << " |" << endl;
}

// Hien thi header bang
void displayHeader() {
    cout << "+--------+---------------------------+-------+----------+" << endl;
    cout << "|   ID   | Ten                       | Tuoi  | Diem TB  |" << endl;
    cout << "+--------+---------------------------+-------+----------+" << endl;
}

void displayFooter() {
    cout << "+--------+---------------------------+-------+----------+" << endl;
}

// Hien thi tat ca sinh vien
void displayAllSV(SinhVien* s, int n) {
    if (n == 0) {
        cout << "Chua co sinh vien nao!\n";
        return;
    }
    displayHeader();
    for (int i = 0; i < n; i++) {
        displayOneSV(s[i]);
    }
    displayFooter();
}

// Tinh diem trung binh cua lop
double diemTBLop(SinhVien* s, int n) {
    if (n == 0) return 0;
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += s[i].diemTB;
    }
    return sum / n;
}

// Tim sinh vien co diem cao nhat
int indexMax(SinhVien* s, int n) {
    int idx = 0;
    for (int i = 1; i < n; i++) {
        if (s[i].diemTB > s[idx].diemTB) idx = i;
    }
    return idx;
}

// Tim sinh vien co diem thap nhat
int indexMin(SinhVien* s, int n) {
    int idx = 0;
    for (int i = 1; i < n; i++) {
        if (s[i].diemTB < s[idx].diemTB) idx = i;
    }
    return idx;
}

// Tim sinh vien theo ID
int findByID(SinhVien* s, int n, int id) {
    for (int i = 0; i < n; i++) {
        if (s[i].id == id) return i;
    }
    return -1;
}

// Sap xep theo diem TB (tang dan) - Bubble Sort
void sortByDiem(SinhVien* s, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (s[j].diemTB > s[j + 1].diemTB) {
                SinhVien temp = s[j];
                s[j] = s[j + 1];
                s[j + 1] = temp;
            }
        }
    }
}

int main() {
    SinhVien* dsSV = nullptr;
    int soSV = 0;
    int choice;

    do {
        cout << "\n==============================MENU============================\n";
        cout << "1. Nhap thong tin sinh vien lop hoc\n";
        cout << "2. Hien thi tat ca sinh vien\n";
        cout << "3. Tinh diem trung binh cua lop hoc\n";
        cout << "4. Hien thi sinh vien co tong diem cao nhat\n";
        cout << "5. Hien thi sinh vien co tong diem thap nhat\n";
        cout << "6. Tim sinh vien boi ID\n";
        cout << "7. Sap xep cac ban ghi boi tong diem thi cua sinh vien\n";
        cout << "0. Thoat\n";
        cout << "==============================================================\n";
        cout << "Nhap lua chon: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                cout << "Nhap so luong sinh vien: ";
                cin >> soSV;
                if (dsSV != nullptr) delete[] dsSV;
                dsSV = new SinhVien[soSV];
                inputSV(dsSV, soSV);
                cout << "\nDa nhap " << soSV << " sinh vien thanh cong!\n";
                break;
            }
            case 2:
                displayAllSV(dsSV, soSV);
                break;
            case 3:
                if (soSV == 0) {
                    cout << "Chua co sinh vien!\n";
                } else {
                    cout << "Diem trung binh cua lop: " << fixed << setprecision(2) << diemTBLop(dsSV, soSV) << endl;
                }
                break;
            case 4:
                if (soSV == 0) {
                    cout << "Chua co sinh vien!\n";
                } else {
                    int idx = indexMax(dsSV, soSV);
                    cout << "Sinh vien co diem cao nhat:\n";
                    displayHeader();
                    displayOneSV(dsSV[idx]);
                    displayFooter();
                }
                break;
            case 5:
                if (soSV == 0) {
                    cout << "Chua co sinh vien!\n";
                } else {
                    int idx = indexMin(dsSV, soSV);
                    cout << "Sinh vien co diem thap nhat:\n";
                    displayHeader();
                    displayOneSV(dsSV[idx]);
                    displayFooter();
                }
                break;
            case 6: {
                if (soSV == 0) {
                    cout << "Chua co sinh vien!\n";
                } else {
                    int id;
                    cout << "Nhap ID can tim: ";
                    cin >> id;
                    int idx = findByID(dsSV, soSV, id);
                    if (idx == -1) {
                        cout << "Khong tim thay sinh vien co ID = " << id << endl;
                    } else {
                        cout << "Tim thay:\n";
                        displayHeader();
                        displayOneSV(dsSV[idx]);
                        displayFooter();
                    }
                }
                break;
            }
            case 7:
                if (soSV == 0) {
                    cout << "Chua co sinh vien!\n";
                } else {
                    sortByDiem(dsSV, soSV);
                    cout << "Da sap xep theo diem trung binh (tang dan):\n";
                    displayAllSV(dsSV, soSV);
                }
                break;
            case 0:
                cout << "Thoat chuong trinh.\n";
                break;
            default:
                cout << "Lua chon khong hop le!\n";
        }
    } while (choice != 0);

    if (dsSV != nullptr) delete[] dsSV;
    return 0;
}
