// ============================================================
// Bai 3.c - GHI RA FILE CHI CAC PHAN TU CO CHI SO LE
// (yeu cau 4 cua phan NhapXuatFile)
// ============================================================
// DE BAI:
//   4. Sua lai chuong trinh de chi xuat ra file cac phan tu co
//      CHI SO LE cua mang (chi in arr[1], arr[3], arr[5], ...).
// ============================================================

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void XuatFile_ChiSoLe(const char* tenFile, float* arr, int n) {
    FILE* fo = fopen(tenFile, "wt");
    if (fo == NULL) {
        printf("Khong mo duoc file %s\n", tenFile);
        return;
    }
    for (int i = 1; i < n; i += 2) {   // bat dau tu i = 1, buoc nhay 2
        fprintf(fo, "%0.1f ", arr[i]);
    }
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

    printf("Mang da doc: ");
    for (int i = 0; i < n; i++) {
        printf("%0.1f ", arr[i]);
    }
    printf("\n");

    XuatFile_ChiSoLe("output_chiSoLe.txt", arr, n);
    printf("Da ghi cac phan tu o chi so le sang output_chiSoLe.txt\n");

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
        g++ 04c_NhapXuatFile_ChiSoLe.cpp -o 04c
        ./04c

   IN RA MAN HINH:
        Mang da doc: 1.2 2.3 3.4 4.5 5.6
        Da ghi cac phan tu o chi so le sang output_chiSoLe.txt

   FILE output_chiSoLe.txt sau khi chay (chi co arr[1], arr[3]):
        2.3 4.5

   GIAI THICH:
        n = 5, vong lap i = 1, 3 (i < 5, +2).
        i = 5 vuot qua nen khong in arr[5] (cung khong ton tai).
   ============================================================ */
