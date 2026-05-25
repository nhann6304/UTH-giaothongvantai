// ============================================================
// Bai 4.c - DE QUY: TINH TONG CAC SO LE TRONG MANG
// (yeu cau 5 cua phan De quy)
// ============================================================
// DE BAI:
//   5. Sua lai chuong trinh de TINH TONG CAC SO LE co trong mang
//      bang phuong phap DE QUY.
//
// CONG THUC DE QUY:
//   - Neu a[n] le:   TongLe(a, n) = TongLe(a, n-1) + a[n]
//   - Neu a[n] chan: TongLe(a, n) = TongLe(a, n-1)
//   Dieu kien dung: n == 0  ->  tra ve a[0] neu le, nguoc lai 0.
// ============================================================

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int TongLe(int* a, int n) {
    if (n == 0) {
        return (a[0] % 2 != 0) ? a[0] : 0;
    }
    int phanConLai = TongLe(a, n - 1);
    if (a[n] % 2 != 0) {
        return phanConLai + a[n];
    }
    return phanConLai;
}

int main() {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    int* a = new int[n];
    for (int i = 0; i < n; i++) {
        printf("Nhap a[%d] = ", i);
        scanf("%d", &a[i]);
    }

    printf("Tong cac so le trong mang = %d\n", TongLe(a, n - 1));

    delete[] a;
    return 0;
}

/* ============================================================
   DEMO & KET QUA
   ------------------------------------------------------------
   Cach chay:
        g++ 06c_DeQuy_TongSoLe.cpp -o 06c
        ./06c

   DEMO 1 (n=5, mang 1 2 3 4 5):
        Nhap n: 5
        Nhap a[0] = 1
        Nhap a[1] = 2
        Nhap a[2] = 3
        Nhap a[3] = 4
        Nhap a[4] = 5
        Tong cac so le trong mang = 9      <-- 1 + 3 + 5 = 9

   DEMO 2 (n=6, mang toan so chan 2 4 6 8 10 12):
        Nhap n: 6
        Nhap a[0] = 2
        Nhap a[1] = 4
        Nhap a[2] = 6
        Nhap a[3] = 8
        Nhap a[4] = 10
        Nhap a[5] = 12
        Tong cac so le trong mang = 0      <-- khong co so le

   DEMO 3 (n=4, mang co so am le -7 -2 5 6):
        Nhap n: 4
        Nhap a[0] = -7
        Nhap a[1] = -2
        Nhap a[2] = 5
        Nhap a[3] = 6
        Tong cac so le trong mang = -2     <-- (-7) + 5 = -2

   DEMO 4 (n=1, mang 9):
        Nhap n: 1
        Nhap a[0] = 9
        Tong cac so le trong mang = 9      <-- chi co a[0] = 9 le
   ============================================================ */
