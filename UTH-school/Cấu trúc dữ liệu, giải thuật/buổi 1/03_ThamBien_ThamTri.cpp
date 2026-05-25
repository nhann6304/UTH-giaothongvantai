// ============================================================
// Bai 2 - TRUYEN THAM BIEN vs TRUYEN THAM TRI
// Code mau: ThamBien_ThamTri
// ============================================================
// DE BAI:
//   1. Bien dich doan chuong trinh mau ben duoi.
//   2. Cho biet ket qua cua 2 lenh:
//          printf("a sau ham TruyenThamTri  = %d\n", a);
//          printf("a sau ham TruyenThamBien = %d\n", a);
//   3. Cho biet ket qua cua:
//          printf("d2 sau khi goi ham ThamTriConTro: (%d,%d)\n",
//                 d2->x, d2->y);
//      Nhan xet d2->x, d2->y co bi thay doi khong? Vi sao mac
//      du khai bao 'void ThamTriConTro(DIEM* d)' (KHONG co &)
//      ma noi dung d2 van bi sua?  -> goi y: d la kieu CON TRO.
//   4. Cho biet ket qua cua:
//          printf("d2 sau khi goi ham ThamBienConTro: (%d,%d)\n",
//                 d2->x, d2->y);
//      Nhan xet d2->x, d2->y co bi thay doi khong? Vi sao khai
//      bao 'void ThamBienConTro(DIEM* &d, DIEM* p)' la THAM BIEN
//      ma d2 cua minh nhin tu ngoai LAI khong giu lai sua doi?
//      -> goi y: thu doi d1->x, d1->y sang gia tri khac (vd 99,88)
//      roi quan sat.
//
// TOM TAT KIEN THUC:
//   - Tham tri: ham nhan ban sao gia tri  -> sua khong anh huong
//   - Tham bien (T&): ham nhan dia chi bien goc -> sua co anh huong
//   - Voi con tro DIEM*:
//       + Tham tri (DIEM* d): d la BAN SAO con tro, *d van la cung
//         o nho => sua *d (vd d->x = ...) van anh huong bien goc.
//       + Tham bien (DIEM* &d): co the doi LUON con tro d sang
//         tro vao 1 vung nho khac (d = p) -> sau ham, d2 cung
//         tro vao p luon.
// ============================================================

#include <stdio.h>

struct DIEM {
    int x, y;
};

void TruyenThamTri(int a) {
    a = a * 10;     // chi sua ban sao
}

void TruyenThamBien(int& a) {
    a = a * 10;     // sua truc tiep bien goc
}

void ThamTriConTro(DIEM* d) {
    // d la ban sao con tro, nhung *d van la o nho cua bien goc
    d->x = d->x * 10;
    d->y = d->y * 10;
}

void ThamBienConTro(DIEM* &d, DIEM* p) {
    // Buoc 1: thay doi noi dung o nho ma d dang tro toi
    d->x = d->x * 10;
    d->y = d->y * 10;
    // Buoc 2: doi LUON con tro d sang tro vao p
    // -> ben ngoai ham, bien d goc cung tro vao p (vi truyen tham bien)
    d = p;
}

int main() {
    // Phan 1: voi kieu int
    int a = 1;
    printf("a = %d\n", a);

    TruyenThamTri(a);
    printf("a sau ham TruyenThamTri  = %d  (khong doi)\n", a);

    TruyenThamBien(a);
    printf("a sau ham TruyenThamBien = %d  (bi nhan 10)\n", a);

    // Phan 2: voi con tro DIEM*
    DIEM* d2 = new DIEM;
    d2->x = 5; d2->y = 5;
    printf("\nDiem d2 ban dau: (%d, %d)\n", d2->x, d2->y);

    ThamTriConTro(d2);
    // Mac du d duoc truyen tham tri, nhung *d van la cung 1 o nho cua d2
    // nen d->x, d->y bi sua = bien doi tren chinh d2
    printf("d2 sau ham ThamTriConTro: (%d, %d)\n", d2->x, d2->y);

    // Reset gia tri d2 va tao d1
    DIEM* d1 = new DIEM;
    d1->x = 99; d1->y = 88;
    d2->x = 5;  d2->y = 5;

    printf("\nTruoc khi goi ThamBienConTro:\n");
    printf("  d2 = (%d, %d)\n", d2->x, d2->y);
    printf("  d1 = (%d, %d)\n", d1->x, d1->y);

    ThamBienConTro(d2, d1);
    // Sau ham:
    //   - Vung nho cu cua d2 da bi nhan 10 -> (50, 50)
    //   - Nhung con tro d2 (truyen tham bien) da bi reassign sang tro vao d1
    //   - Do do d2->x, d2->y bay gio tra ve gia tri cua d1 -> (99, 88)
    printf("d2 sau ham ThamBienConTro: (%d, %d)  (= du lieu cua d1)\n",
           d2->x, d2->y);

    // Luu y: vung nho cu cua d2 (da bi nhan 10) bay gio bi mat con tro
    //         -> day la mot vi du ve memory leak. Trong code that nen luu lai
    //         con tro cu de delete truoc khi reassign.
    delete d1;  // d2 hien dang tro vao d1, nen ta chi delete 1 lan
    return 0;
}

/* ============================================================
   DEMO & KET QUA
   ------------------------------------------------------------
   Cach chay (khong can nhap lieu):
       g++ 03_ThamBien_ThamTri.cpp -o 03
       ./03

   KET QUA MAU:
       a = 1
       a sau ham TruyenThamTri  = 1  (khong doi)
       a sau ham TruyenThamBien = 10  (bi nhan 10)

       Diem d2 ban dau: (5, 5)
       d2 sau ham ThamTriConTro: (50, 50)

       Truoc khi goi ThamBienConTro:
         d2 = (5, 5)
         d1 = (99, 88)
       d2 sau ham ThamBienConTro: (99, 88)  (= du lieu cua d1)

   GIAI THICH (cau 2-3-4):
   - Cau 2: a sau ThamTriConTro/ TruyenThamTri = 1 (khong doi vi
     ham chi nhan ban sao). a sau TruyenThamBien = 10 vi & truyen
     dia chi bien goc, sua a trong ham = sua a ben ngoai.
   - Cau 3: d2 sau ThamTriConTro = (50,50). DU 'd' truyen THAM TRI
     (ban sao con tro), nhung 2 con tro - cua ham va cua main -
     deu cung tro vao 1 vung nho cua d2. Sua *d (d->x, d->y) tuc
     la sua o nho cua d2 -> ben ngoai d2 cung doi.
   - Cau 4: d2 sau ThamBienConTro = (99,88). Ben trong ham, ta:
       (a) sua noi dung cu cua d2 thanh (50,50).
       (b) gan d = p  -> bien con tro d (THAM BIEN) tro sang d1.
     Vi truyen tham bien nen d2 ben ngoai cung tro sang d1
     -> d2->x, d2->y la (99,88) cua d1, KHONG phai (50,50) cu nua.
   ============================================================ */
