// ============================================================
// Bai 1.5.a - CON TRO VOI MANG 1 CHIEU (CAP PHAT DONG)
// Code mau: ConTroVoiMang
// ============================================================
// DE BAI:
//   1. Bien dich doan chuong trinh mau.
//   2. Nhap mot vai mang so nguyen, nhan xet ket qua cua 2 lenh:
//          printf("a[0] = %d\n", a[0]);
//          printf("*a   = %d\n", *a);
//   3. Giai thich tai sao co the rut ra ket luan o cau 2.
//
// MUC TIEU:
//   - Cap phat mang dong bang new int[n]
//   - Hieu vi sao a[0] == *a (deu chi cung 1 o nho dau)
//   - Giai phong vung nho bang delete[]
// ============================================================

#include <stdio.h>

int main() {
    int n;
    printf("Nhap so luong phan tu: ");
    scanf("%d", &n);

    // Cap phat dong: dung bao nhieu phan tu thi xin bay nhieu
    int* a = new int[n];

    for (int i = 0; i < n; i++) {
        printf("Nhap a[%d]: ", i);
        scanf("%d", &a[i]);
    }

    // a[0] va *a tro vao cung mot o nho (phan tu dau)
    // -> luon cho ket qua bang nhau
    printf("a[0] = %d\n", a[0]);
    printf("*a   = %d\n", *a);

    printf("Mang vua nhap: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");

    delete[] a;  // tra lai vung nho cho HDH
    return 0;
}

/* ============================================================
   DEMO & KET QUA
   ------------------------------------------------------------
   Cach chay:
       g++ 02a_ConTroVoiMang_1D.cpp -o 02a
       ./02a

   DEMO 1 (n=5, cac so 10 20 30 40 50):
       Nhap so luong phan tu: 5
       Nhap a[0]: 10
       Nhap a[1]: 20
       Nhap a[2]: 30
       Nhap a[3]: 40
       Nhap a[4]: 50
       a[0] = 10
       *a   = 10
       Mang vua nhap: 10 20 30 40 50

   DEMO 2 (n=3, cac so -7 99 0):
       Nhap so luong phan tu: 3
       Nhap a[0]: -7
       Nhap a[1]: 99
       Nhap a[2]: 0
       a[0] = -7
       *a   = -7
       Mang vua nhap: -7 99 0

   NHAN XET (cau 2-3):
   - a[0] va *a luon cho ket qua bang nhau.
   - Vi: con tro 'a' tro vao o nho dau cua mang. *a doc gia tri
     o nho do, con a[0] tuong duong *(a + 0) -> cung 1 o nho.
     Tong quat: a[i] tuong duong *(a + i).
   ============================================================ */
