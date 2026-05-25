// ============================================================
// Bai 4.a - DE QUY: TINH TONG CAC PHAN TU TRONG MANG
// Code mau: DeQuy
// ============================================================
// DE BAI:
//   1. Bien dich doan chuong trinh mau ben duoi.
//   2. Cho biet doan chuong trinh tren thuc hien tac vu gi?
//   3. Viet cong thuc de quy va dieu kien dung. Neu chuong trinh
//      de quy KHONG co dieu kien dung thi dieu gi xay ra?
//
// CONG THUC DE QUY:
//   Tong(a, n) = Tong(a, n-1) + a[n]
//   Dieu kien dung: n == 0  ->  Tong = a[0]
// Y nghia: ham Tong(a, n) tra ve tong cua a[0..n].
//
// Neu KHONG co dieu kien dung: ham se goi lai chinh no vo han,
// dan toi STACK OVERFLOW (tran bo nho stack) va chuong trinh CRASH.
// ============================================================

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int Tong(int* a, int n) {
    if (n == 0) {
        return a[0];               // dieu kien dung
    }
    return Tong(a, n - 1) + a[n];  // cong thuc de quy
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

    printf("Tong cac phan tu = %d\n", Tong(a, n - 1));

    delete[] a;
    return 0;
}

/* ============================================================
   DEMO & KET QUA
   ------------------------------------------------------------
   Cach chay:
        g++ 06a_DeQuy_TongMang.cpp -o 06a
        ./06a

   DEMO 1 (n=5, mang 1 2 3 4 5):
        Nhap n: 5
        Nhap a[0] = 1
        Nhap a[1] = 2
        Nhap a[2] = 3
        Nhap a[3] = 4
        Nhap a[4] = 5
        Tong cac phan tu = 15

   DEMO 2 (n=4, mang 10 -3 7 100):
        Nhap n: 4
        Nhap a[0] = 10
        Nhap a[1] = -3
        Nhap a[2] = 7
        Nhap a[3] = 100
        Tong cac phan tu = 114

   DEMO 3 (n=1, mang 42):
        Nhap n: 1
        Nhap a[0] = 42
        Tong cac phan tu = 42       <-- chi co a[0], dieu kien dung

   GIAI THICH (cau 2-3):
   - Cau 2: chuong trinh tinh TONG cac phan tu mang nguyen bang
     phuong phap DE QUY.
   - Cau 3: Cong thuc Tong(a, n) = Tong(a, n-1) + a[n].
     Dieu kien dung: n == 0 -> tra ve a[0].
     Neu khong co dieu kien dung, ham tu goi vo han lan -> stack
     overflow -> chuong trinh crash.
   ============================================================ */
