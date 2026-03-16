#include <iostream>
#include <string.h>
using namespace std;

// Bài 11: Kiểm tra xem 1 chuỗi S bất kỳ có chứa trong nó chuỗi "Lap Trinh" hay không?
int main() {
    char S[1000];
    char pattern[] = "Lap Trinh";
    int patternLength = 10; // strlen("Lap Trinh") = 10
    
    cout << "Nhap chuoi S: ";
    cin.getline(S, 1000);
    
    int textLength = strlen(S);
    bool found = false;
    int position = -1;
    
    // Tìm chuỗi "Lap Trinh" trong S
    for (int i = 0; i <= textLength - patternLength; i++) {
        bool match = true;
        
        // Kiểm tra từng ký tự
        for (int j = 0; j < patternLength; j++) {
            if (S[i + j] != pattern[j]) {
                match = false;
                break;
            }
        }
        
        if (match) {
            found = true;
            position = i;
            break;
        }
    }
    
    if (found) {
        cout << "Chuoi S chua chuoi 'Lap Trinh' tai vi tri: " << position << endl;
    } else {
        cout << "Chuoi S KHONG chua chuoi 'Lap Trinh'" << endl;
    }
    
    return 0;
}
