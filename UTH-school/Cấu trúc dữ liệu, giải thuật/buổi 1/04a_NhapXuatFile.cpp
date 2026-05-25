// ============================================================
// Bai 3.a - DOC/GHI FILE VAN BAN  (code mau: NhapXuatFile)
// ============================================================
// DE BAI:
//   Doc tu file "input.txt" mang 1 chieu cac so thuc:
//      Dong 1: 1 so nguyen n (so luong phan tu)
//      Dong 2: n so thuc cach nhau boi khoang trang
//   Vi du noi dung input.txt:
//        5
//        1.2 2.3 3.4 4.5 5.6
//   Sau do in ra man hinh va GHI lai sang file "output.txt".
//
//   1. Bien dich doan chuong trinh mau.
// ============================================================

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void XuatFile(const char* tenFile, float* arr, int n) {
    FILE* fo = fopen(tenFile, "wt");
    if (fo == NULL) {
        printf("Khong mo duoc file %s de ghi\n", tenFile);
        return;
    }
    for (int i = 0; i < n; i++) {
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

    // In ra man hinh de kiem tra
    printf("Du lieu doc tu input.txt (%d phan tu):\n", n);
    for (int i = 0; i < n; i++) {
        printf("%0.1f ", arr[i]);
    }
    printf("\n");

    // Ghi lai sang output.txt
    XuatFile("output.txt", arr, n);
    printf("Da ghi ket qua sang output.txt\n");

    delete[] arr;
    return 0;
}

/* ============================================================
   DEMO & KET QUA
   ------------------------------------------------------------
   Chuan bi: file input.txt nam cung thu muc, noi dung:
        5
        1.2 2.3 3.4 4.5 5.6

   Cach chay:
        g++ 04a_NhapXuatFile.cpp -o 04a
        ./04a

   IN RA MAN HINH:
        Du lieu doc tu input.txt (5 phan tu):
        1.2 2.3 3.4 4.5 5.6
        Da ghi ket qua sang output.txt

   FILE output.txt sau khi chay (mot dong, cach nhau bang space):
        1.2 2.3 3.4 4.5 5.6
   ============================================================ */
