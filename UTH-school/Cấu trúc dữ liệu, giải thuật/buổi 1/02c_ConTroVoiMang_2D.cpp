// ============================================================
// Bai 1.5.c - MANG 2 CHIEU (CAP PHAT DONG)
// (Cau 5 cua phan ConTroVoiMang)
// ============================================================
// DE BAI:
//   Viet chuong trinh cho phep NHAP vao mot mang 2 chieu cac
//   so nguyen dung CAP PHAT DONG.
//   Goi y:
//      int** b = new int*[m];
//      moi b[i] (kieu int*) la mang 1 chieu n so nguyen
//      b[i]   = new int[n];
//   Khi giai phong: delete tung hang truoc, roi delete b.
// ============================================================

#include <stdio.h>

int main() {
    int m, n;
    printf("Nhap so dong m: ");
    scanf("%d", &m);
    printf("Nhap so cot n: ");
    scanf("%d", &n);

    // 1) Cap phat
    int** b = new int*[m];
    for (int i = 0; i < m; i++) {
        b[i] = new int[n];
    }

    // 2) Nhap du lieu
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("Nhap b[%d][%d]: ", i, j);
            scanf("%d", &b[i][j]);
        }
    }

    // 3) Xuat du lieu duoi dang ma tran
    printf("\nMa tran b (%d x %d):\n", m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%5d ", b[i][j]);
        }
        printf("\n");
    }

    // 4) Giai phong vung nho theo dung thu tu
    for (int i = 0; i < m; i++) {
        delete[] b[i];   // huy tung hang
    }
    delete[] b;          // huy mang con tro hang

    return 0;
}

/* ============================================================
   DEMO & KET QUA
   ------------------------------------------------------------
   DEMO 1 (m=2, n=3, cac so 1 2 3 / 4 5 6):
       Nhap so dong m: 2
       Nhap so cot n: 3
       Nhap b[0][0]: 1
       Nhap b[0][1]: 2
       Nhap b[0][2]: 3
       Nhap b[1][0]: 4
       Nhap b[1][1]: 5
       Nhap b[1][2]: 6

       Ma tran b (2 x 3):
           1     2     3
           4     5     6

   DEMO 2 (m=3, n=3, ma tran don vi):
       Nhap so dong m: 3
       Nhap so cot n: 3
       Nhap b[0][0]: 1   Nhap b[0][1]: 0   Nhap b[0][2]: 0
       Nhap b[1][0]: 0   Nhap b[1][1]: 1   Nhap b[1][2]: 0
       Nhap b[2][0]: 0   Nhap b[2][1]: 0   Nhap b[2][2]: 1

       Ma tran b (3 x 3):
           1     0     0
           0     1     0
           0     0     1
   ============================================================ */
