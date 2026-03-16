#include <iostream>
#include <string.h>
using namespace std;

// Bài 5: Cho chuỗi s là họ và tên đầy đủ của 1 người. Hãy tách phần tên của người đó.
int main() {
    char s[100];
    cout << "Nhap ho va ten day du: ";
    cin.getline(s, 100);
    
    int length = strlen(s);
    int lastSpace = -1;
    
    // Tìm vị trí khoảng trắng cuối cùng
    for (int i = length - 1; i >= 0; i--) {
        if (s[i] == ' ') {
            lastSpace = i;
            break;
        }
    }
    
    if (lastSpace == -1) {
        cout << "Ten: " << s << endl;
    } else {
        cout << "Ten: ";
        for (int i = lastSpace + 1; i < length; i++) {
            cout << s[i];
        }
        cout << endl;
    }
    
    return 0;
}
