#include <iostream>
using namespace std;

// Bài 7: Hãy trộn 2 mảng bất kỳ thành 1 mảng sao cho mảng mới không chứa phần tử chung nào cùng xuất hiện ở 2 mảng gốc.
int main() {
    int n, m;
    cout << "Nhap so phan tu mang thu nhat: ";
    cin >> n;
    cout << "Nhap so phan tu mang thu hai: ";
    cin >> m;
    
    int a[n], b[m];
    
    cout << "Nhap " << n << " phan tu mang thu nhat: ";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    cout << "Nhap " << m << " phan tu mang thu hai: ";
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }
    
    // Tìm các phần tử chung
    int maxCommon = min(n, m);
    int common[maxCommon];
    int commonCount = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i] == b[j]) {
                // Kiểm tra đã có trong common chưa
                bool exists = false;
                for (int k = 0; k < commonCount; k++) {
                    if (common[k] == a[i]) {
                        exists = true;
                        break;
                    }
                }
                if (!exists) {
                    common[commonCount++] = a[i];
                }
                break;
            }
        }
    }
    
    // Tạo mảng kết quả (không chứa phần tử chung)
    int result[n + m];
    int resultCount = 0;
    
    // Thêm các phần tử từ mảng a không có trong common
    for (int i = 0; i < n; i++) {
        bool isCommon = false;
        for (int j = 0; j < commonCount; j++) {
            if (a[i] == common[j]) {
                isCommon = true;
                break;
            }
        }
        if (!isCommon) {
            result[resultCount++] = a[i];
        }
    }
    
    // Thêm các phần tử từ mảng b không có trong common
    for (int i = 0; i < m; i++) {
        bool isCommon = false;
        for (int j = 0; j < commonCount; j++) {
            if (b[i] == common[j]) {
                isCommon = true;
                break;
            }
        }
        if (!isCommon) {
            result[resultCount++] = b[i];
        }
    }
    
    cout << "Mang sau khi tron (khong co phan tu chung): ";
    for (int i = 0; i < resultCount; i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    
    return 0;
}
