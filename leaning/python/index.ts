interface DoThi {
    [dinh: string]: { [dinhKe: string]: number };
}

interface KhoangCachNganNhat {
    [dinh: string]: number;
}

interface PhanTuHangDoi {
    dinh: string;
    khoangCach: number;
}

const danhsachke: DoThi = {
    A: { B: 4, C: 2 },
    B: { A: 4, C: 1, D: 5 },
    C: { A: 2, B: 1, D: 8, E: 10 },
    D: { B: 5, C: 8, E: 2, F: 6 },
    E: { C: 10, D: 2, F: 3 },
    F: { D: 6, E: 3 },
};

function timDuongDiNganNhat(
    doThi: DoThi,
    dinhXuatPhat: string
): KhoangCachNganNhat {
    const bangKhoangCach: KhoangCachNganNhat = {};

    for (let dinh in doThi) {
        bangKhoangCach[dinh] = Infinity;
    }
    bangKhoangCach[dinhXuatPhat] = 0;

    const hangDoiUuTien: PhanTuHangDoi[] = [];

    hangDoiUuTien.push({ dinh: dinhXuatPhat, khoangCach: 0 });

    console.log(`🚀 Bắt đầu tìm đường từ đỉnh: ${dinhXuatPhat}\n`);

    while (hangDoiUuTien.length > 0) {
        hangDoiUuTien.sort((a, b) => a.khoangCach - b.khoangCach);
        console.log("Chekck khi sap xep ", hangDoiUuTien);
        const phanTuHienTai = hangDoiUuTien.shift();
        if (!phanTuHienTai) break;

        const { dinh: dinhHienTai, khoangCach: khoangCachHienTai } = phanTuHienTai;

        if (khoangCachHienTai > bangKhoangCach[dinhHienTai]) {
            console.log(`Bỏ qua ${dinhHienTai} (đã có đường ngắn hơn)`);
            continue;
        }

        console.log(
            `🔹 Đang xét đỉnh: ${dinhHienTai} (Khoảng cách: ${khoangCachHienTai})`
        );

        const cacDinhKe = doThi[dinhHienTai];

        for (const dinhKe in cacDinhKe) {
            const trongSoCanh = cacDinhKe[dinhKe];
            const khoangCachMoi = khoangCachHienTai + trongSoCanh;

            if (khoangCachMoi < bangKhoangCach[dinhKe]) {
                console.log(
                    `   ✅ Cập nhật đỉnh ${dinhKe}: ${bangKhoangCach[dinhKe]} → ${khoangCachMoi} (qua ${dinhHienTai})`
                );

                bangKhoangCach[dinhKe] = khoangCachMoi;

                hangDoiUuTien.push({
                    dinh: dinhKe,
                    khoangCach: khoangCachMoi,
                });
            } else {
                console.log(
                    `   ⏭️  Giữ nguyên đỉnh ${dinhKe}: ${bangKhoangCach[dinhKe]} (không cải thiện)`
                );
            }
        }

        console.log("");
    }

    return bangKhoangCach;
}

const ketQua = timDuongDiNganNhat(danhsachke, "A");

console.log("=".repeat(50));
console.log("🏁 KẾT QUẢ CUỐI CÙNG - ĐƯỜNG ĐI NGẮN NHẤT TỪ A:");
console.log("=".repeat(50));
console.table(ketQua);
