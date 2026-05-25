// ============================================================
// Bai 3.e - DOC FILE KHI KHONG BIET TRUOC SO LUONG PHAN TU
// (so sanh DocHetFile1 va DocHetFile2)
// ============================================================
// DE BAI:
//   Cho input2.txt va input3.txt deu chua day so:
//        1.2 2.3 3.4 4.5 5.6
//   Su khac biet: input3.txt co MOT KHOANG TRANG o cuoi file.
//
//   1. Bien dich doan chuong trinh mau (chi goi DocHetFile1).
//   2. Nhan xet 2 dong ket qua xuat ra (cho input2 va input3).
//      2 dong co GIONG nhau khong?
//   3. Neu KHONG giong, giai thich tai sao cung 1 day so ma ket
//      qua khac nhau? -> goi y: file input3 co khoang trang du
//      o cuoi nen sau khi doc 5.6 thi !feof(fi) van TRUE.
//   4. Sua 2 dong goi sang DocHetFile2(...) va chay lai. Nhan xet
//      ket qua, rut ra ket luan ham nao doc HET FILE chinh xac hon.
//
// TOM TAT:
//   - DocHetFile1: chi dung !feof(fi).
//     feof() chi tra ve true SAU khi mot lan doc that bai
//     => neu file co khoang trang thua o cuoi, vong lap se in
//     gia tri cuoi cung 2 lan (vi temp khong duoc cap nhat).
//
//   - DocHetFile2: vua dung !feof(fi), vua kiem tra fscanf() > 0.
//     An toan hon: neu lan doc khong thanh cong, break ngay.
// ============================================================

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void DocHetFile1(const char* tenFile) {
    FILE* fi = fopen(tenFile, "rt");
    if (fi == NULL) {
        printf("Khong mo duoc %s\n", tenFile);
        return;
    }
    float temp = 0;
    while (!feof(fi)) {
        fscanf(fi, "%f", &temp);  // KHONG kiem tra ket qua doc
        printf("%0.1f ", temp);
    }
    printf("\n");
    fclose(fi);
}

void DocHetFile2(const char* tenFile) {
    FILE* fi = fopen(tenFile, "rt");
    if (fi == NULL) {
        printf("Khong mo duoc %s\n", tenFile);
        return;
    }
    float temp = 0;
    while (!feof(fi)) {
        if (fscanf(fi, "%f", &temp) > 0) {  // chi in khi doc thanh cong
            printf("%0.1f ", temp);
        } else {
            break;
        }
    }
    printf("\n");
    fclose(fi);
}

int main() {
    printf("=== DocHetFile1 (KHONG kiem tra fscanf) ===\n");
    printf("input2.txt: ");
    DocHetFile1("input2.txt");
    printf("input3.txt: ");
    DocHetFile1("input3.txt");

    printf("\n=== DocHetFile2 (CO kiem tra fscanf > 0) ===\n");
    printf("input2.txt: ");
    DocHetFile2("input2.txt");
    printf("input3.txt: ");
    DocHetFile2("input3.txt");

    // Ket luan: DocHetFile2 chinh xac hon vi tranh duoc loi
    //          "in trung phan tu cuoi" khi file co khoang trang thua o cuoi.
    return 0;
}

/* ============================================================
   DEMO & KET QUA
   ------------------------------------------------------------
   Chuan bi 2 file cung thu muc:
        input2.txt:  '1.2 2.3 3.4 4.5 5.6'             (KHONG co space cuoi)
        input3.txt:  '1.2 2.3 3.4 4.5 5.6 '            (CO 1 space cuoi)

   Cach chay:
        g++ 05_DocHetFile.cpp -o 05
        ./05

   IN RA MAN HINH:
        === DocHetFile1 (KHONG kiem tra fscanf) ===
        input2.txt: 1.2 2.3 3.4 4.5 5.6
        input3.txt: 1.2 2.3 3.4 4.5 5.6 5.6      <-- 5.6 BI IN 2 LAN

        === DocHetFile2 (CO kiem tra fscanf > 0) ===
        input2.txt: 1.2 2.3 3.4 4.5 5.6
        input3.txt: 1.2 2.3 3.4 4.5 5.6          <-- DUNG

   GIAI THICH (cau 2-3-4):
   - Cau 2: 2 dong KHAC nhau. Voi input2 ket qua dung; voi input3
     so 5.6 bi IN 2 LAN.
   - Cau 3: feof() chi true SAU khi co 1 lan doc bi loi (cham EOF).
     Sau khi doc 5.6 trong input3, con trang trong + ki tu xuong
     dong/EOF chua duoc tieu thu => !feof(fi) van TRUE => vong lap
     chay them 1 vong, fscanf khong doc duoc gia tri moi nhung
     'temp' khong bi reset => 5.6 in lai 1 lan nua.
   - Cau 4: DocHetFile2 in dung 5 so cho ca 2 file. Vi co
     'if (fscanf(...) > 0)': khi lan doc cuoi cung KHONG thanh cong,
     ham break ngay -> tranh duoc loi in lap.
     => DocHetFile2 doc HET FILE chinh xac hon DocHetFile1.
   ============================================================ */
