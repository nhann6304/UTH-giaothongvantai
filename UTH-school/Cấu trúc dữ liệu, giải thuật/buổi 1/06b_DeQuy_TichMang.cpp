// ============================================================
// Bai 4.b - DE QUY: TINH TICH CAC PHAN TU TRONG MANG
// (yeu cau 4 cua phan De quy)
// ============================================================
// DE BAI:
//   4. Sua lai chuong trinh de TINH TICH cac phan tu cua mot day
//      so nguyen bang phuong phap DE QUY.
//
// CONG THUC DE QUY:
//   Tich(a, n) = Tich(a, n-1) * a[n]
//   Dieu kien dung: n == 0  ->  Tich = a[0]
// ============================================================

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long long Tich(int* a, int n) {
    if (n == 0) {
        return a[0];
    }
    return Tich(a, n - 1) * (long long)a[n];
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

    printf("Tich cac phan tu = %lld\n", Tich(a, n - 1));

    delete[] a;
    return 0;
}

/* ============================================================
   DEMO & KET QUA
   ------------------------------------------------------------
   Cach chay:
        g++ 06b_DeQuy_TichMang.cpp -o 06b
        ./06b

   DEMO 1 (n=5, mang 1 2 3 4 5):
        Nhap n: 5
        Nhap a[0] = 1
        Nhap a[1] = 2
        Nhap a[2] = 3
        Nhap a[3] = 4
        Nhap a[4] = 5
        Tich cac phan tu = 120         <-- 5! = 120

   DEMO 2 (n=3, mang 10 20 30):
        Nhap n: 3
        Nhap a[0] = 10
        Nhap a[1] = 20
        Nhap a[2] = 30
        Tich cac phan tu = 6000

   DEMO 3 (n=4, mang co so 0):
        Nhap n: 4
        Nhap a[0] = 7
        Nhap a[1] = 0
        Nhap a[2] = 9
        Nhap a[3] = 11
        Tich cac phan tu = 0           <-- bat ki phan tu = 0 -> tich = 0

   DEMO 4 (n=4, mang co so am, kiem tra dau):
        Nhap n: 4
        Nhap a[0] = -2
        Nhap a[1] = 3
        Nhap a[2] = -5
        Nhap a[3] = 1
        Tich cac phan tu = 30          <-- (-2)*3*(-5)*1 = 30
   ============================================================ */
