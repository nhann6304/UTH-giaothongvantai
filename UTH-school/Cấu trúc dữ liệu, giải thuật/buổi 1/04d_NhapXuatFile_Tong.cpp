// ============================================================
// Bai 3.d - TINH TONG CAC PHAN TU VA GHI RA FILE
// (yeu cau 5 cua phan NhapXuatFile)
// ============================================================
// DE BAI:
//   5. Sua lai chuong trinh de TINH TONG cac phan tu cua mang
//      va XUAT TONG do ra mot file van ban.
// ============================================================

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void GhiTong(const char* tenFile, float tong) {
    FILE* fo = fopen(tenFile, "wt");
    if (fo == NULL) {
        printf("Khong mo duoc file %s\n", tenFile);
        return;
    }
    fprintf(fo, "Tong cac phan tu = %0.2f\n", tong);
    fclose(fo);
}

int main() {
    FILE* fi = fopen("input.txt", "rt");
    if (fi == NULL) {
        printf("Khong mo duoc file input.txt\n");
        return 1;
    }

    int n;
    fscanf(fi, "%d", &n);

    float* arr = new float[n];
    for (int i = 0; i < n; i++) {
        fscanf(fi, "%f", &arr[i]);
    }
    fclose(fi);

    float tong = 0;
    for (int i = 0; i < n; i++) {
        tong += arr[i];
    }
    printf("Tong = %0.2f\n", tong);

    GhiTong("output_tong.txt", tong);
    printf("Da ghi tong sang output_tong.txt\n");

    delete[] arr;
    return 0;
}

/* ============================================================
   DEMO & KET QUA
   ------------------------------------------------------------
   Chuan bi: file input.txt cung thu muc, noi dung:
        5
        1.2 2.3 3.4 4.5 5.6

   Cach chay:
        g++ 04d_NhapXuatFile_Tong.cpp -o 04d
        ./04d

   IN RA MAN HINH:
        Tong = 17.00
        Da ghi tong sang output_tong.txt

   FILE output_tong.txt sau khi chay:
        Tong cac phan tu = 17.00

   GIAI THICH:
        1.2 + 2.3 + 3.4 + 4.5 + 5.6 = 17.0
   ============================================================ */
