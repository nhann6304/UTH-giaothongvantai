#include <iostream>
#include <algorithm>
using namespace std;

// Bài 10: Cho dãy số dương A bất kỳ. Hãy tìm 3 phần tử trong A sao cho tổng của chúng là lớn nhất mà không sắp xếp dãy A.
int main() {
    int n;
    cout << "Nhap so phan tu cua day: ";
    cin >> n;
    
    if (n < 3) {
        cout << "Day phai co it nhat 3 phan tu!" << endl;
        return 0;
    }
    
    int a[n];
    cout << "Nhap " << n << " phan tu duong: ";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] <= 0) {
            cout << "Cac phan tu phai la so duong!" << endl;
            return 0;
        }
    }
    
    // Tìm 3 số lớn nhất mà không sắp xếp
    int max1 = -1, max2 = -1, max3 = -1;
    int index1 = -1, index2 = -1, index3 = -1;
    
    for (int i = 0; i < n; i++) {
        if (a[i] > max1) {
            max3 = max2;
            index3 = index2;
            max2 = max1;
            index2 = index1;
            max1 = a[i];
            index1 = i;
        } else if (a[i] > max2 && a[i] != max1) {
            max3 = max2;
            index3 = index2;
            max2 = a[i];
            index2 = i;
        } else if (a[i] > max3 && a[i] != max2 && a[i] != max1) {
            max3 = a[i];
            index3 = i;
        }
    }
    
    if (max3 == -1) {
        cout << "Khong tim duoc 3 phan tu khac nhau!" << endl;
        return 0;
    }
    
    cout << "3 phan tu co tong lon nhat: " << max1 << ", " << max2 << ", " << max3 << endl;
    cout << "Tong cua chung: " << (max1 + max2 + max3) << endl;
    cout << "Vi tri cac phan tu: " << index1 << ", " << index2 << ", " << index3 << endl;
    
    return 0;
}
