#include <iostream>
#include <cstring>
#include <cctype>
using namespace std;

// a. Xuất chuỗi ngược lại
void xuatChuoiNguoc(char s[]) {
    int len = strlen(s);
    cout << "Chuoi nguoc: ";
    for (int i = len - 1; i >= 0; i--) {
        cout << s[i];
    }
    cout << endl;
}

// b. Đếm chữ cái và chữ số
void demKyTu(char s[]) {
    int demChuCai = 0, demChuSo = 0;
    
    for (int i = 0; s[i] != '\0'; i++) {
        if (isalpha(s[i])) demChuCai++;
        else if (isdigit(s[i])) demChuSo++;
    }
    
    cout << "So ky tu chu cai: " << demChuCai << endl;
    cout << "So ky tu chu so: " << demChuSo << endl;
}

// c. Định dạng chuỗi
void dinhDangChuoi(char s[]) {
    int len = strlen(s);
    char temp[1000];
    int j = 0;
    
    // Bỏ khoảng trắng đầu
    int i = 0;
    while (s[i] == ' ') i++;
    
    // Xử lý chuỗi
    bool dauTu = true;
    while (i < len) {
        if (s[i] != ' ') {
            if (dauTu) {
                temp[j++] = toupper(s[i]);
                dauTu = false;
            } else {
                temp[j++] = tolower(s[i]);
            }
            i++;
        } else {
            // Bỏ khoảng trắng thừa
            while (s[i] == ' ') i++;
            if (i < len) {
                temp[j++] = ' ';
                dauTu = true;
            }
        }
    }
    
    temp[j] = '\0';
    strcpy(s, temp);
}

// d. Kiểm tra chuỗi
bool kiemTraChuoi(char s[]) {
    char chuoiMau[] = "Ngon ngu lap trinh C++ 2015";
    return strcmp(s, chuoiMau) == 0;
}

// e. Xóa ký tự không phải chữ cái
void xoaKhongChuCai(char s[]) {
    char temp[1000];
    int j = 0;
    
    for (int i = 0; s[i] != '\0'; i++) {
        if (isalpha(s[i]) || s[i] == ' ') {
            temp[j++] = s[i];
        }
    }
    
    temp[j] = '\0';
    strcpy(s, temp);
}

// f. Thay chữ in hoa bằng *
void thayInHoaBangSao(char s[]) {
    for (int i = 0; s[i] != '\0'; i++) {
        if (isupper(s[i])) {
            s[i] = '*';
        }
    }
}

// g. Thêm "Hello" vào cuối
void themHello(char s[]) {
    strcat(s, "Hello");
}

int main() {
    char s[1000];
    int choice;
    
    cout << "Nhap chuoi S: ";
    cin.getline(s, 1000);
    
    do {
        cout << "\n===== MENU =====" << endl;
        cout << "1. Xuat chuoi nguoc" << endl;
        cout << "2. Dem chu cai va chu so" << endl;
        cout << "3. Dinh dang chuoi" << endl;
        cout << "4. Kiem tra chuoi" << endl;
        cout << "5. Xoa ky tu khong phai chu cai" << endl;
        cout << "6. Thay chu in hoa bang *" << endl;
        cout << "7. Them 'Hello' vao cuoi" << endl;
        cout << "8. Hien thi chuoi hien tai" << endl;
        cout << "0. Thoat" << endl;
        cout << "Chon: ";
        cin >> choice;
        cin.ignore();
        
        switch(choice) {
            case 1:
                xuatChuoiNguoc(s);
                break;
            case 2:
                demKyTu(s);
                break;
            case 3:
                dinhDangChuoi(s);
                cout << "Da dinh dang!" << endl;
                cout << "Chuoi moi: " << s << endl;
                break;
            case 4:
                if (kiemTraChuoi(s)) {
                    cout << "Chuoi la 'Ngon ngu lap trinh C++ 2015'" << endl;
                } else {
                    cout << "Chuoi KHONG phai la 'Ngon ngu lap trinh C++ 2015'" << endl;
                }
                break;
            case 5:
                xoaKhongChuCai(s);
                cout << "Da xoa!" << endl;
                cout << "Chuoi moi: " << s << endl;
                break;
            case 6:
                thayInHoaBangSao(s);
                cout << "Da thay the!" << endl;
                cout << "Chuoi moi: " << s << endl;
                break;
            case 7:
                themHello(s);
                cout << "Da them!" << endl;
                cout << "Chuoi moi: " << s << endl;
                break;
            case 8:
                cout << "Chuoi hien tai: " << s << endl;
                break;
        }
    } while (choice != 0);
    
    return 0;
}
