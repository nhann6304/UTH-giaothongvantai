#include <iostream>
using namespace std;

// Bài 6: Hãy trộn 2 mảng (giả sử đã sắp xếp) tăng dần thành 1 mảng sao cho mảng mới vẫn giữ nguyên tính chất sắp xếp.
int main() {
    int n, m;
    cout << "Nhap so phan tu mang thu nhat: ";
    cin >> n;
    cout << "Nhap so phan tu mang thu hai: ";
    cin >> m;
    
    int a[n], b[m];
    
    cout << "Nhap " << n << " phan tu mang thu nhat (da sap xep tang dan): ";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    cout << "Nhap " << m << " phan tu mang thu hai (da sap xep tang dan): ";
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }
    
    int c[n + m];
    int i = 0, j = 0, k = 0;
    
    // Trộn hai mảng đã sắp xếp
    while (i < n && j < m) {
        if (a[i] <= b[j]) {
            c[k++] = a[i++];
        } else {
            c[k++] = b[j++];
        }
    }
    
    // Thêm phần tử còn lại của mảng a
    while (i < n) {
        c[k++] = a[i++];
    }
    
    // Thêm phần tử còn lại của mảng b
    while (j < m) {
        c[k++] = b[j++];
    }
    
    cout << "Mang sau khi tron: ";
    for (int i = 0; i < n + m; i++) {
        cout << c[i] << " ";
    }
    cout << endl;
    
    return 0;
}
