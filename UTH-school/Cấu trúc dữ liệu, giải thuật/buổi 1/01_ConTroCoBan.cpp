// ============================================================
// Bai 1.1 - CON TRO CO BAN  (code mau: ConTroCoBan)
// Lab 01 - On tap KTLT - Cau truc du lieu & Giai thuat
// ============================================================
// DE BAI:
//   1. Bien dich doan chuong trinh mau (xem main() ben duoi).
//   2. Neu doi 'int a = 1;' thanh 'int a = 10;' thi *pa = ?
//   3. Neu sua 'int *pa = &a;' thanh 'int *pa;' thi luc bien dich
//      va luc thuc thi co loi gi? Tai sao?
//   4. Neu truoc dong 'printf("Gia tri a: %d\n", *pa);' ta them
//      '*pb = 2;' thi *pa in ra bao nhieu? Vi sao?
//
// MUC TIEU:
//   - Khai bao bien con tro
//   - Toan tu & lay dia chi, * truy xuat gia tri qua con tro
//   - Toan tu -> truy xuat thanh phan struct qua con tro
//   - Hieu hien tuong "alias": 2 con tro cung tro vao 1 o nho
// ============================================================

#include <stdio.h>

struct DIEM {
    int hoanhDo, tungDo;
};

int main() {
    // 1) Khoi tao cac bien gia tri
    int a = 1;
    DIEM d;
    d.hoanhDo = 1;
    d.tungDo = 2;

    // 2) Khai bao cac bien con tro
    int* pa = &a;     // pa tro vao o nho cua a
    int* pb = pa;     // pb cung tro vao o nho cua a (alias)
    DIEM* pd = &d;    // pd tro vao o nho cua d

    // 3) Toan tu & lay dia chi
    printf("Dia chi o nho cua a: %p\n", (void*)&a);

    // 4) Toan tu * truy xuat gia tri qua con tro
    printf("Gia tri a   = %d\n", *pa);

    // 5) Truy xuat thanh phan struct
    printf("Diem D (qua bien)    : (%d,%d)\n", d.hoanhDo, d.tungDo);   // bien gia tri dung .
    printf("Diem D (qua con tro) : (%d,%d)\n", pd->hoanhDo, pd->tungDo); // con tro dung ->

    // 6) Quan sat hien tuong alias
    *pb = 2;  // sua noi dung qua pb -> a thay doi vi pb cung tro vao o nho cua a
    printf("Sau *pb = 2 -> a = %d, *pa = %d\n", a, *pa);

    // 7) Khong dung delete cho pa, pb, pd vi chung tro vao bien stack
    //    (delete chi dung cho vung nho cap phat boi new)
    return 0;
}

/* ============================================================
   DEMO & KET QUA
   ------------------------------------------------------------
   Cach chay (Visual Studio 2022 / g++):
       g++ 01_ConTroCoBan.cpp -o 01_ConTroCoBan
       ./01_ConTroCoBan
   Chuong trinh khong can nhap lieu.

   KET QUA MAU (dia chi tuy may):
       Dia chi o nho cua a: 0x7ffeefbff5ac
       Gia tri a   = 1
       Diem D (qua bien)    : (1,2)
       Diem D (qua con tro) : (1,2)
       Sau *pb = 2 -> a = 2, *pa = 2

   GIAI THICH CAC CAU HOI:
   - Cau 2: Doi a = 10  =>  *pa = 10  (vi pa van tro vao o nho cua a).
   - Cau 3: Neu khai bao 'int *pa;' (khong khoi tao):
       + Bien dich VAN PASS (chi co warning).
       + Khi thuc thi, *pa truy xuat o nho rac
         => CRASH (segmentation fault / access violation).
   - Cau 4: Truoc khi in *pa, neu them '*pb = 2;' thi *pa in ra 2.
       Vi pb va pa cung tro vao 1 o nho cua a, sua qua pb tuc la
       sua ngay o nho cua a -> *pa cung doi theo.
   ============================================================ */
