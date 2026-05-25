// ============================================================
// Bai 1.5.b - TINH TONG MANG SO NGUYEN (cap phat dong)
// (Cau 4 cua phan ConTroVoiMang)
// ============================================================
// DE BAI:
//   Sua lai chuong trinh ConTroVoiMang de NHAP vao mot mang so
//   nguyen va XUAT ra TONG cac so trong mang do.
// ============================================================

#include <stdio.h>

int main() {
    int n;
    printf("Nhap so luong phan tu: ");
    scanf("%d", &n);

    int* a = new int[n];
    for (int i = 0; i < n; i++) {
        printf("Nhap a[%d]: ", i);
        scanf("%d", &a[i]);
    }

    long long tong = 0;  // dung long long de tranh tran so
    for (int i = 0; i < n; i++) {
        tong += a[i];
    }

    printf("Tong cac phan tu trong mang = %lld\n", tong);

    delete[] a;
    return 0;
}

/* ============================================================
   DEMO & KET QUA
   ------------------------------------------------------------
   DEMO 1 (n=5, cac so 1 2 3 4 5):
       Nhap so luong phan tu: 5
       Nhap a[0]: 1
       Nhap a[1]: 2
       Nhap a[2]: 3
       Nhap a[3]: 4
       Nhap a[4]: 5
       Tong cac phan tu trong mang = 15

   DEMO 2 (n=4, cac so 10 -3 7 100):
       Nhap so luong phan tu: 4
       Nhap a[0]: 10
       Nhap a[1]: -3
       Nhap a[2]: 7
       Nhap a[3]: 100
       Tong cac phan tu trong mang = 114

   DEMO 3 (n=1, so 999999999):
       Nhap so luong phan tu: 1
       Nhap a[0]: 999999999
       Tong cac phan tu trong mang = 999999999
   ============================================================ */
