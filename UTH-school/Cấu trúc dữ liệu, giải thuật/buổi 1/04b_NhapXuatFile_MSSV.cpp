// ============================================================
// Bai 3.b - DOC TU MSSV.txt, GHI RA out_MSSV.txt
// (yeu cau 2-3 cua phan NhapXuatFile)
// ============================================================
// DE BAI:
//   2. Tao tap tin du lieu moi "MSSV.txt" thay cho "input.txt".
//      Nhap du lieu cho file MSSV.txt va chay chuong trinh.
//   3. Xuat ra file "out_MSSV.txt" thay cho "output.txt". Them
//      file output vao project de xem ket qua tu Visual Studio
//      thay vi phai dung Windows Explorer + Notepad.
//
//   MSSV.txt co dinh dang giong input.txt:
//      Dong 1: n
//      Dong 2: n so thuc
//   Trong project that, sinh vien doi ten "MSSV" thanh ma so cua minh.
// ============================================================

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void XuatFile(const char* tenFile, float* arr, int n) {
    FILE* fo = fopen(tenFile, "wt");
    if (fo == NULL) {
        printf("Khong mo duoc file %s\n", tenFile);
        return;
    }
    for (int i = 0; i < n; i++) {
        fprintf(fo, "%0.1f ", arr[i]);
    }
    fclose(fo);
}

int main() {
    const char* tenFileVao = "MSSV.txt";
    const char* tenFileRa  = "out_MSSV.txt";

    FILE* fi = fopen(tenFileVao, "rt");
    if (fi == NULL) {
        printf("Khong mo duoc file %s\n", tenFileVao);
        return 1;
    }

    int n;
    fscanf(fi, "%d", &n);

    float* arr = new float[n];
    for (int i = 0; i < n; i++) {
        fscanf(fi, "%f", &arr[i]);
    }
    fclose(fi);

    printf("Du lieu doc tu %s (%d phan tu):\n", tenFileVao, n);
    for (int i = 0; i < n; i++) {
        printf("%0.1f ", arr[i]);
    }
    printf("\n");

    XuatFile(tenFileRa, arr, n);
    printf("Da ghi ket qua sang %s\n", tenFileRa);

    delete[] arr;
    return 0;
}

/* ============================================================
   DEMO & KET QUA
   ------------------------------------------------------------
   Chuan bi: file MSSV.txt cung thu muc, noi dung:
        6
        7.5 8.0 9.25 10.5 11.75 12.0

   Cach chay:
        g++ 04b_NhapXuatFile_MSSV.cpp -o 04b
        ./04b

   IN RA MAN HINH:
        Du lieu doc tu MSSV.txt (6 phan tu):
        7.5 8.0 9.3 10.5 11.8 12.0
        Da ghi ket qua sang out_MSSV.txt

   FILE out_MSSV.txt sau khi chay (1 dong):
        7.5 8.0 9.3 10.5 11.8 12.0

   GHI CHU: dinh dang in la "%0.1f" nen 9.25 lam tron thanh 9.3,
            11.75 lam tron thanh 11.8 (lam tron banker / nearest).
   ============================================================ */
