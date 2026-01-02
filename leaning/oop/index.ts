interface INhanvienFactory {
    createNhanvien(
        maso: string,
        hoten: string,
        luongCB: number,
        loai: string
    ): Nhanvien;
    createNhanvien(loai: string): Nhanvien;
}

interface ITienthuong {
    tinhTienThuong(luongCB: number): number;
}

abstract class Nhanvien {
    protected maso: string;
    protected hoten: string;
    protected luongCB: number;
    protected phuongThucTinhThuong!: ITienthuong;

    constructor(maso: string, hoten: string, luongCB: number) {
        this.maso = maso;
        this.hoten = hoten;
        this.luongCB = luongCB;
    }

    abstract NhanvienInit(maso: string, hoten: string, luongCB: number): void;

    public getMaso(): string {
        return this.maso;
    }

    public getHoten(): string {
        return this.hoten;
    }

    public getLuongCB(): number {
        return this.luongCB;
    }

    public getPhuongThucTinhThuong(): ITienthuong {
        return this.phuongThucTinhThuong;
    }

    public setMaso(maso: string): void {
        this.maso = maso;
    }

    public setHoten(hoten: string): void {
        this.hoten = hoten;
    }

    public setLuongCB(luongCB: number): void {
        this.luongCB = luongCB;
    }

    public setPhuongThucTinhThuong(iTienthuong: ITienthuong): void {
        this.phuongThucTinhThuong = iTienthuong;
    }

    // Concrete methods
    public toString(): string {
        return `Mã: ${this.maso}, Họ tên: ${this.hoten}, Lương CB: ${this.luongCB}`;
    }

    public tinhTienThuong(): number {
        if (!this.phuongThucTinhThuong) {
            throw new Error("Chưa thiết lập phương thức tính tiền thưởng");
        }
        return this.phuongThucTinhThuong.tinhTienThuong(this.luongCB);
    }
}

class Laptrinhvien extends Nhanvien {
    constructor(maso: string, hoten: string, luongCB: number) {
        super(maso, hoten, luongCB);
    }

    public NhanvienInit(maso: string, hoten: string, luongCB: number): void {
        this.maso = maso;
        this.hoten = hoten;
        this.luongCB = luongCB;
    }

    public LaptrinhvienInit(maso: string, hoten: string, luongCB: number): void {
        this.NhanvienInit(maso, hoten, luongCB);
    }
}

class Kiemthu extends Nhanvien {
    constructor(maso: string, hoten: string, luongCB: number) {
        super(maso, hoten, luongCB);
    }

    // Implement abstract method
    public NhanvienInit(maso: string, hoten: string, luongCB: number): void {
        this.maso = maso;
        this.hoten = hoten;
        this.luongCB = luongCB;
    }

    public KiemthuInit(): void { } // Chưa cần
}

class ChuyenvienPhanTich extends Nhanvien {
    constructor(maso: string, hoten: string, luongCB: number) {
        super(maso, hoten, luongCB);
    }

    public NhanvienInit(maso: string, hoten: string, luongCB: number): void {
        this.maso = maso;
        this.hoten = hoten;
        this.luongCB = luongCB;
    }

    // public ChuyenvienPhanTichInit(): void { }
}

class Ketoanvien extends Nhanvien {
    constructor(maso: string, hoten: string, luongCB: number) {
        super(maso, hoten, luongCB);
    }

    public NhanvienInit(maso: string, hoten: string, luongCB: number): void {
        this.maso = maso;
        this.hoten = hoten;
        this.luongCB = luongCB;
    }

    // Method riêng
    public KetoanvienInit(maso: string, hoten: string, luongCB: number): void {
        this.NhanvienInit(maso, hoten, luongCB);
    }
}

class TienthuongThongthuong implements ITienthuong {
    public tinhTienThuong(luongCB: number): number {
        return luongCB * 0.02;
    }
}

class TienthuongNgoaigio implements ITienthuong {
    public tinhTienThuong(luongCB: number): number {
        return luongCB * 0.1;
    }
}

class TienthuongNgoaitinh implements ITienthuong {
    public tinhTienThuong(luongCB: number): number {
        return luongCB * 0.15;
    }
}

class NhanvienFactory implements INhanvienFactory {
    createNhanvien(
        maso: string,
        hoten: string,
        luongCB: number,
        loai: string
    ): Nhanvien;
    createNhanvien(loai: string): Nhanvien;

    createNhanvien(
        param1: string,
        param2?: string,
        param3?: number,
        param4?: string
    ): Nhanvien {
        if (arguments.length === 1) {
            const loai = param1.toLowerCase().trim();
            return this.createNhanvienByType(loai, "", "", 0);
        }

        const maso = param1;
        const hoten = param2 || "";
        const luongCB = param3 || 0;
        const loai = (param4 || "").toLowerCase().trim();

        return this.createNhanvienByType(loai, maso, hoten, luongCB);
    }

    private createNhanvienByType(
        loai: string,
        maso: string,
        hoten: string,
        luongCB: number
    ): Nhanvien {
        switch (loai) {
            case "laptrinhvien":
                return new Laptrinhvien(maso, hoten, luongCB);

            case "kiemthu":
                return new Kiemthu(maso, hoten, luongCB);

            case "chuyenvienphanntich":
                return new ChuyenvienPhanTich(maso, hoten, luongCB);

            case "ketoanvien":
                return new Ketoanvien(maso, hoten, luongCB);

            default:
                throw new Error("Loại nhân viên không hợp lệ");
        }
    }
}
