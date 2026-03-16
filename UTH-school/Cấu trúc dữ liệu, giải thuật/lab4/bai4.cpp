#include <iostream>
using namespace std;

// Bài 4: Cho dãy số nguyên a. Hãy tìm dãy con dài nhất trong a được sắp theo thứ tự tăng dần. (dãy con của a phải chứa các phần tử liên tục nhau của a).
int main() {
    int n;
    cout << "Nhap so phan tu cua day: ";
    cin >> n;
    
    int a[n];
    cout << "Nhap " << n << " phan tu: ";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    int maxLength = 1;
    int currentLength = 1;
    int startIndex = 0;
    int bestStart = 0;
    
    for (int i = 1; i < n; i++) {
        if (a[i] > a[i-1]) {
            currentLength++;
        } else {
            if (currentLength > maxLength) {
                maxLength = currentLength;
                bestStart = startIndex;
            }
            currentLength = 1;
            startIndex = i;
        }
    }
    
    // Kiểm tra dãy cuối cùng
    if (currentLength > maxLength) {
        maxLength = currentLength;
        bestStart = startIndex;
    }
    
    cout << "Day con tang dan dai nhat co do dai: " << maxLength << endl;
    cout << "Cac phan tu: ";
    for (int i = bestStart; i < bestStart + maxLength; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
    
    return 0;
}
