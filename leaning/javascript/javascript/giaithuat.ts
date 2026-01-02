// 1. XÁC ĐỊNH LOẠI TAM GIÁC
function xacDinhTamGiac(a: number, b: number, c: number): string {
    if (a <= 0 || b <= 0 || c <= 0) {
        return "Các cạnh phải là số dương";
    }

    if (a + b <= c || a + c <= b || b + c <= a) {
        return "Không phải tam giác";
    }

    if (a === b && b === c) {
        return "Tam giác đều";
    }

    const sides = [a, b, c].sort((x, y) => x - y);
    const isVuong =
        Math.abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 0.0001;

    const isCan = a === b || b === c || a === c;

    if (isVuong && isCan) {
        return "Tam giác vuông cân";
    }

    if (isVuong) {
        return "Tam giác vuông";
    }

    if (isCan) {
        return "Tam giác cân";
    }

    return "Tam giác thường";
}

// 2. GIẢI PHƯƠNG TRÌNH BẬC NHẤT: ax + b = 0

interface IPhuongTrinhResult {
    nghiem?: number;
    message: string;
}

function giaiPhuongTrinhBacNhat(a: number, b: number): IPhuongTrinhResult {
    if (a === 0) {
        if (b === 0) {
            return {
                message: "Phương trình vô số nghiệm",
            };
        } else {
            return {
                message: "Phương trình vô nghiệm",
            };
        }
    }

    const nghiem = -b / a;
    return {
        nghiem: nghiem,
        message: `Phương trình có nghiệm x = ${nghiem}`,
    };
}

// 3. ĐẾM SỐ CHẴN/LẺ TRONG MẢNG

function demSoChanLe(mang: number[]) {
    let soChan = 0;
    let soLe = 0;
    const mangChan: number[] = [];
    const mangLe: number[] = [];

    for (const so of mang) {
        if (so % 2 === 0) {
            soChan++;
            mangChan.push(so);
        } else {
            soLe++;
            mangLe.push(so);
        }
    }

    return {
        soChan,
        soLe,
    };
}

// 4. TÍNH GIAI THỪA BẰNG ĐỆ QUY (n!)

function giaiThua(n: number): number {
    if (n === 0 || n === 1) {
        return 1;
    }

    // Đệ quy
    return n * giaiThua(n - 1);
}

// 5. TÌM SỐ LỚN NHẤT TRONG 3 SỐ

function timSoLonNhat(a: number, b: number, c: number): string {
    let max = a;

    if (b > max) {
        max = b;
    }

    if (c > max) {
        max = c;
    }

    return `Số lớn nhất là số ${max}`;
}

// Sẻ ra tam giác đều
console.log(xacDinhTamGiac(3, 3, 3));

// 2x +  4y = 0
console.log(giaiPhuongTrinhBacNhat(2, 4));

// 2 Số chẵn 2 số lẻ
console.log(demSoChanLe([1, 2, 3, 4]));

//giaiThua
console.log(giaiThua(5));

// Số 3 lớn nhất
console.log(timSoLonNhat(1, 2, 3));
