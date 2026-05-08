# ============================================================
# Project 3: QUẢN LÝ CHI TIÊU CÁ NHÂN  —  BẢN KẾT QUẢ ĐẦY ĐỦ
# ------------------------------------------------------------
# File này = phiên bản "đáp án" của thư mục bai_lam/
#   - bai_lam/main.py        + giao_dien.py + ham_xu_ly.py  (skeleton để code)
#   - final.py               (gộp 1 file, đã điền đầy đủ)
#
# Chức năng theo 5 yêu cầu của đề:
#   1. Nhập thu/chi với danh mục (ăn uống, học tập, giải trí, ...)
#   2. Phân bổ ngân sách cho từng danh mục theo tháng
#   3. Cảnh báo chi vượt ngân sách
#   4. Lọc giao dịch theo tháng, danh mục
#   5. Tính tiết kiệm cộng dồn từ các tháng trước
# ============================================================


# ============================================================
# PHẦN 1: KHAI BÁO THƯ VIỆN VÀ HẰNG SỐ
# ============================================================

# Thư viện tkinter dùng để tạo cửa sổ giao diện (GUI).
# Đặt tên ngắn là "tk" để gọi cho nhanh: tk.Label, tk.Button, ...
import tkinter as tk

# messagebox: hiển thị hộp thoại thông báo (info/warning/error)
# ttk:        chứa các widget hiện đại như Combobox, Treeview
from tkinter import messagebox, ttk

# json: thư viện chuẩn của Python để đọc/ghi file JSON
import json

# os: dùng để kiểm tra file có tồn tại không (os.path.exists)
#     và lấy thời gian sửa đổi file (os.path.getmtime)
import os

# sys: lấy đường dẫn Python (sys.executable) và tham số chạy file (sys.argv)
#      dùng cho chức năng hot-reload (tự khởi động lại app khi sửa code)
import sys

# datetime: lấy ngày/giờ hiện tại để điền sẵn vào ô nhập
from datetime import datetime


# ---------- Tên 2 file lưu dữ liệu (đặt cùng folder với final.py) ----------
FILE_GD = "transactions.json"  # lưu danh sách giao dịch (thu/chi)
FILE_NS = "budgets.json"       # lưu hạn mức ngân sách theo tháng + danh mục


# ---------- Danh sách danh mục cố định ----------
# Khi chọn loại "Thu" thì hiện list này:
DANH_MUC_THU = ["Lương", "Thưởng", "Đầu tư", "Khác"]

# Khi chọn loại "Chi" thì hiện list này:
DANH_MUC_CHI = [
    "Ăn uống",
    "Học tập",
    "Giải trí",
    "Đi lại",
    "Mua sắm",
    "Hóa đơn",
    "Y tế",
    "Khác",
]


# ============================================================
# PHẦN 2: NHÓM HÀM ĐỌC / GHI FILE JSON
# ------------------------------------------------------------
# 4 hàm dưới đây làm việc với 2 file dữ liệu:
#   - transactions.json: list các giao dịch
#   - budgets.json:      dict ngân sách
# ============================================================


def doc_giao_dich():
    """Đọc danh sách giao dịch từ file JSON, trả về list."""
    # Nếu file chưa tồn tại (lần đầu chạy) thì trả về list rỗng
    # để chương trình không bị lỗi FileNotFoundError.
    if not os.path.exists(FILE_GD):
        return []

    # Mở file ở chế độ "r" (read = đọc).
    # encoding="utf-8" để đọc đúng tiếng Việt có dấu.
    # Cú pháp "with open() as f": Python tự đóng file sau khi đọc xong.
    with open(FILE_GD, "r", encoding="utf-8") as f:
        # json.load(f) đọc nội dung file và chuyển từ chuỗi JSON
        # thành đối tượng Python (ở đây là list các dict).
        return json.load(f)


def luu_giao_dich(ds):
    """Ghi danh sách giao dịch ds xuống file JSON."""
    # Mở file ở chế độ "w" (write = ghi đè). Nếu file chưa có sẽ tự tạo.
    with open(FILE_GD, "w", encoding="utf-8") as f:
        # json.dump(ds, f, ...) chuyển ds thành chuỗi JSON rồi ghi vào file.
        # ensure_ascii=False: giữ nguyên tiếng Việt, không đổi thành \uXXXX.
        # indent=2: ghi xuống dòng + thụt lề 2 dấu cách cho dễ đọc.
        json.dump(ds, f, ensure_ascii=False, indent=2)


def doc_ngan_sach():
    """Đọc dict ngân sách từ file, trả về {} nếu chưa có file."""
    if not os.path.exists(FILE_NS):
        return {}  # dict rỗng — sẵn sàng để thêm hạn mức mới
    with open(FILE_NS, "r", encoding="utf-8") as f:
        return json.load(f)


def luu_ngan_sach(ns):
    """Ghi dict ngân sách ns xuống file."""
    with open(FILE_NS, "w", encoding="utf-8") as f:
        json.dump(ns, f, ensure_ascii=False, indent=2)


# ============================================================
# PHẦN 3: NHÓM HÀM TÍNH TOÁN (xử lý nghiệp vụ)
# ------------------------------------------------------------
# Các hàm này KHÔNG đụng đến giao diện, chỉ nhận list/dict
# và trả về kết quả → dễ test và dễ tái sử dụng.
# ============================================================


def tinh_tong(ds, loai, thang):
    """
    Tính tổng số tiền của 1 LOẠI (thu hoặc chi) trong 1 THÁNG.
    Tham số:
      ds    — list giao dịch
      loai  — "thu" hoặc "chi"
      thang — chuỗi dạng "yyyy-mm" (vd "2026-05")
    """
    tong = 0  # biến đếm, khởi tạo bằng 0

    # Duyệt qua từng giao dịch trong danh sách
    for gd in ds:
        # Bỏ qua nếu loại không khớp (vd cần "thu" mà gd là "chi")
        if gd["loai"] != loai:
            continue

        # Bỏ qua nếu ngày không bắt đầu bằng tháng cần tìm.
        # Ví dụ thang="2026-05" thì "2026-05-12" hợp lệ, "2026-04-30" thì không.
        if not gd["ngay"].startswith(thang):
            continue

        # Tới đây là giao dịch hợp lệ → cộng dồn số tiền
        tong += gd["so_tien"]

    return tong


def tinh_tong_theo_danh_muc(ds, danh_muc, thang):
    """
    Tính tổng đã CHI cho 1 danh mục trong 1 tháng.
    Phục vụ yêu cầu 3: cảnh báo vượt ngân sách CHÍNH XÁC theo từng danh mục.
    """
    tong = 0
    for gd in ds:
        # Phải thỏa CẢ 3 điều kiện:
        #   - là giao dịch chi
        #   - đúng danh mục đang xét
        #   - đúng tháng đang xét
        if (
            gd["loai"] == "chi"
            and gd["danh_muc"] == danh_muc
            and gd["ngay"].startswith(thang)
        ):
            tong += gd["so_tien"]
    return tong


def loc_giao_dich(ds, thang, loai, danh_muc):
    """
    Lọc danh sách giao dịch theo: tháng + loại + danh mục.
    Quy ước: tham số nào là chuỗi rỗng "" thì KHÔNG lọc theo tiêu chí đó.
    Phục vụ yêu cầu 4 của đề: lọc theo tháng và danh mục.
    """
    ket_qua = []  # list để chứa các giao dịch thỏa điều kiện

    for gd in ds:
        # Điều kiện 1: nếu có yêu cầu lọc tháng mà ngày không khớp → bỏ
        if thang != "" and not gd["ngay"].startswith(thang):
            continue

        # Điều kiện 2: nếu có yêu cầu lọc loại mà loại không khớp → bỏ
        if loai != "" and gd["loai"] != loai:
            continue

        # Điều kiện 3: nếu có yêu cầu lọc danh mục mà không khớp → bỏ
        if danh_muc != "" and gd["danh_muc"] != danh_muc:
            continue

        # Qua hết các điều kiện thì thêm vào kết quả
        ket_qua.append(gd)

    return ket_qua


def tinh_tiet_kiem_cong_don(ds, thang):
    """
    Tính tiết kiệm CỘNG DỒN từ đầu đến hết tháng `thang`.
    - Thu thì cộng vào tổng.
    - Chi thì trừ khỏi tổng.
    Có thể trả về số âm nếu chi nhiều hơn thu.

    Đáp ứng yêu cầu 5: tính cộng dồn TỪ CÁC THÁNG TRƯỚC ĐÓ.
    """
    tong = 0

    for gd in ds:
        # gd["ngay"][:7] cắt 7 ký tự đầu của chuỗi ngày → "yyyy-mm"
        # Vd "2026-05-12"[:7] = "2026-05"
        # So sánh chuỗi: "2026-04" < "2026-05" (Python so sánh từng ký tự)
        # → lấy được tất cả giao dịch từ đầu đến hết tháng cần tính
        if gd["ngay"][:7] <= thang:
            if gd["loai"] == "thu":
                tong += gd["so_tien"]   # thu thì +
            else:
                tong -= gd["so_tien"]   # chi thì -

    return tong


# ============================================================
# PHẦN 4: NHÓM HÀM XỬ LÝ SỰ KIỆN GIAO DIỆN
# ------------------------------------------------------------
# Các hàm này được gọi khi người dùng tương tác với GUI:
# bấm nút, đổi radiobutton, gõ vào ô lọc, ...
# ============================================================


def doi_danh_muc(*args):
    """
    Khi người dùng đổi giữa "Thu" và "Chi", tự động đổi
    list trong combobox cho phù hợp.
    *args nhận tham số mặc định mà tkinter truyền vào (không dùng tới).
    """
    if var_loai.get() == "thu":
        # Đặt lại values của combobox thành list danh mục thu
        cb_danh_muc["values"] = DANH_MUC_THU
        # Chọn sẵn phần tử đầu tiên cho người dùng đỡ phải chọn
        cb_danh_muc.set(DANH_MUC_THU[0])
    else:
        cb_danh_muc["values"] = DANH_MUC_CHI
        cb_danh_muc.set(DANH_MUC_CHI[0])


def them_giao_dich():
    """
    Đáp ứng yêu cầu 1: Lưu 1 giao dịch thu hoặc chi mới
    với danh mục, số tiền, ngày, ghi chú do người dùng nhập.
    """
    # ---- Lấy giá trị từ giao diện ----
    # var_loai.get():    đọc giá trị radiobutton "thu" hay "chi"
    # cb_danh_muc.get(): đọc giá trị combobox đang chọn
    # .get().strip():    lấy nội dung Entry và xóa khoảng trắng đầu/cuối
    loai = var_loai.get()
    danh_muc = cb_danh_muc.get()
    ngay = e_ngay.get().strip()
    ghi_chu = e_ghi_chu.get().strip()

    # ---- Kiểm tra số tiền hợp lệ ----
    # .replace(",", "") xóa dấu phẩy nếu người dùng gõ "1,500,000"
    # .replace(".", "") xóa dấu chấm tương tự
    so_tien_text = e_so_tien.get().replace(",", "").replace(".", "").strip()

    # isdigit() trả về True nếu chuỗi CHỈ chứa chữ số.
    # Kết hợp kiểm tra > 0 để chặn trường hợp gõ "0" hoặc bỏ trống.
    if not so_tien_text.isdigit() or int(so_tien_text) <= 0:
        messagebox.showwarning("Lỗi", "Số tiền phải là số nguyên dương!")
        return  # thoát hàm, không lưu

    so_tien = int(so_tien_text)  # chuyển từ chuỗi sang số nguyên

    # ---- Tạo dict giao dịch mới và thêm vào danh sách ----
    ds = doc_giao_dich()  # đọc danh sách hiện có
    giao_dich = {
        "id": len(ds) + 1,   # id tự tăng theo độ dài list
        "loai": loai,
        "danh_muc": danh_muc,
        "so_tien": so_tien,
        "ngay": ngay,
        "ghi_chu": ghi_chu,
    }
    ds.append(giao_dich)   # thêm vào cuối list
    luu_giao_dich(ds)      # ghi xuống file

    # ---- Nếu là chi thì kiểm tra vượt ngân sách (yêu cầu 3) ----
    if loai == "chi":
        # ngay[:7] cắt "yyyy-mm" từ chuỗi "yyyy-mm-dd"
        canh_bao_ngan_sach(danh_muc, ngay[:7])

    # ---- Báo người dùng đã lưu thành công ----
    # Dùng toán tử ba ngôi để hiển thị "Thu" hoặc "Chi" cho thân thiện
    ten_loai = "Thu" if loai == "thu" else "Chi"
    messagebox.showinfo("Đã lưu!", f"{ten_loai} {so_tien:,} đ  —  {danh_muc}")

    # ---- Xóa các ô nhập để dễ nhập tiếp lần sau ----
    e_so_tien.delete(0, tk.END)   # xóa từ vị trí 0 đến hết
    e_ghi_chu.delete(0, tk.END)

    # Cập nhật bảng danh sách bên dưới để thấy giao dịch vừa thêm
    hien_thi_danh_sach()


def luu_ngan_sach_ui():
    """
    Đáp ứng yêu cầu 2: Lưu hạn mức ngân sách cho 1 danh mục
    trong 1 tháng cụ thể.
    """
    # Lấy giá trị từ ô nhập
    thang = e_ns_thang.get().strip()
    danh_muc = cb_ns_dm.get()
    han_muc_text = e_ns_hanmuc.get().replace(",", "").replace(".", "").strip()

    # Kiểm tra định dạng tháng "yyyy-mm":
    # - len(thang) phải bằng 7 (vd "2026-05")
    # - thang[4] phải là dấu "-"
    if len(thang) != 7 or thang[4] != "-":
        messagebox.showwarning("Lỗi", "Tháng phải dạng yyyy-mm  (ví dụ: 2026-05)")
        return

    # Kiểm tra hạn mức là số nguyên dương
    if not han_muc_text.isdigit() or int(han_muc_text) <= 0:
        messagebox.showwarning("Lỗi", "Hạn mức phải là số nguyên dương!")
        return
    han_muc = int(han_muc_text)

    # Đọc dict ngân sách hiện tại
    ns = doc_ngan_sach()
    # Cấu trúc ns: { "yyyy-mm": { "danh_muc": han_muc, ... }, ... }
    if thang not in ns:
        ns[thang] = {}              # tạo dict con nếu tháng này chưa có
    ns[thang][danh_muc] = han_muc   # gán hạn mức cho danh mục
    luu_ngan_sach(ns)               # ghi file

    messagebox.showinfo(
        "Đã lưu!", f"{danh_muc} | tháng {thang} | hạn mức: {han_muc:,} đ"
    )
    e_ns_hanmuc.delete(0, tk.END)   # xóa ô để nhập tiếp


def canh_bao_ngan_sach(danh_muc, thang):
    """
    Đáp ứng yêu cầu 3: Cảnh báo nếu chi tiêu của 1 danh mục
    đã vượt quá hạn mức ngân sách đặt cho tháng đó.
    """
    # Bước 1: Lấy hạn mức đã đặt
    ns = doc_ngan_sach()
    # ns.get(thang, {}): nếu chưa có key `thang` thì trả về {} thay vì lỗi
    # .get(danh_muc, 0): nếu chưa đặt cho danh_muc này thì lấy 0
    han_muc = ns.get(thang, {}).get(danh_muc, 0)

    # Nếu chưa đặt ngân sách (= 0) thì không cảnh báo, return luôn
    if han_muc == 0:
        return

    # Bước 2: Tính tổng đã chi cho danh mục này trong tháng (gọi hàm có sẵn)
    ds = doc_giao_dich()
    da_chi = tinh_tong_theo_danh_muc(ds, danh_muc, thang)

    # Bước 3: Nếu vượt thì hiện hộp thoại cảnh báo
    if da_chi > han_muc:
        messagebox.showwarning(
            "Vượt ngân sách!",
            # f-string với :, để format số có dấu phẩy ngăn cách hàng nghìn
            # Vd 1500000 → "1,500,000"
            f"Danh mục '{danh_muc}' tháng {thang}\n"
            f"Đã chi:   {da_chi:,} đ\n"
            f"Hạn mức:  {han_muc:,} đ\n"
            f"Vượt:     {da_chi - han_muc:,} đ",
        )


def hien_thi_danh_sach():
    """
    Đáp ứng yêu cầu 4 + 5:
    - Hiện danh sách giao dịch (đã lọc theo tháng + loại + danh mục)
    - Hiển thị thống kê: tổng thu, tổng chi, tiết kiệm tháng,
      tiết kiệm cộng dồn.
    """
    # Lấy điều kiện lọc từ ô nhập
    thang = e_loc_thang.get().strip()  # có thể rỗng = không lọc

    # Quy ước: "tat_ca" = không lọc → dùng chuỗi rỗng cho hàm lọc
    loai_loc = var_loai_loc.get()
    if loai_loc == "tat_ca":
        loai_loc = ""

    dm_loc = var_dm_loc.get()
    if dm_loc == "tat_ca":
        dm_loc = ""

    # Lấy dữ liệu và lọc
    ds = doc_giao_dich()
    ket_qua = loc_giao_dich(ds, thang, loai_loc, dm_loc)

    # ---- Sắp xếp theo ngày: mới nhất lên đầu (Bubble Sort) ----
    # Đây là thuật toán sắp xếp đơn giản nhất, phù hợp môn nhập môn.
    # Vòng for ngoài chạy len-1 lần, vòng trong so sánh từng cặp.
    # Nếu ngày của i nhỏ hơn ngày của j thì đổi chỗ → ngày lớn lên đầu.
    for i in range(len(ket_qua) - 1):
        for j in range(i + 1, len(ket_qua)):
            if ket_qua[i]["ngay"] < ket_qua[j]["ngay"]:
                # Cú pháp Python đặc biệt: gán đôi → đổi chỗ 2 phần tử
                ket_qua[i], ket_qua[j] = ket_qua[j], ket_qua[i]

    # ---- Xóa toàn bộ dòng cũ trong bảng ----
    # tree.get_children() trả về list ID của các dòng đang có
    for row in tree.get_children():
        tree.delete(row)

    # ---- Thêm từng giao dịch vào bảng Treeview ----
    for gd in ket_qua:
        # Đổi "thu"/"chi" thành "Thu"/"Chi" cho dễ nhìn
        ten_loai = "Thu" if gd["loai"] == "thu" else "Chi"
        tree.insert(
            "",        # parent rỗng = thêm ở cấp gốc (không có cấp cha)
            "end",     # vị trí: cuối bảng
            values=(   # các cột tương ứng với khai báo columns ở dưới
                gd["ngay"],
                ten_loai,
                gd["danh_muc"],
                f"{gd['so_tien']:,} đ",
                gd.get("ghi_chu", ""),  # .get để tránh lỗi nếu thiếu key
            ),
        )

    # ---- Tính các con số thống kê ----
    # Nếu người dùng không nhập tháng lọc, mặc định lấy tháng hiện tại
    thang_tk = thang if thang != "" else datetime.now().strftime("%Y-%m")

    tong_thu = tinh_tong(ds, "thu", thang_tk)
    tong_chi = tinh_tong(ds, "chi", thang_tk)
    tiet_kiem_t = tong_thu - tong_chi                         # tháng này
    tiet_kiem_cd = tinh_tiet_kiem_cong_don(ds, thang_tk)      # cộng dồn

    # Hiển thị lên nhãn ở cuối cửa sổ
    lbl_tk.config(
        text=(
            f"Tháng {thang_tk}:   "
            f"Thu {tong_thu:,} đ   |   "
            f"Chi {tong_chi:,} đ   |   "
            f"Tiết kiệm tháng: {tiet_kiem_t:,} đ   |   "
            f"Cộng dồn: {tiet_kiem_cd:,} đ"
        )
    )


def hien_tat_ca():
    """Bỏ tất cả bộ lọc rồi hiện lại toàn bộ danh sách."""
    e_loc_thang.delete(0, tk.END)  # xóa ô lọc tháng
    var_loai_loc.set("tat_ca")     # đặt lại combobox loại về "tất cả"
    var_dm_loc.set("tat_ca")       # đặt lại combobox danh mục về "tất cả"
    hien_thi_danh_sach()           # hiện lại bảng


# ============================================================
# PHẦN 5: TẠO GIAO DIỆN (GUI)
# ------------------------------------------------------------
# Tạo cửa sổ và bố trí các widget bên trong:
#   - 2 LabelFrame phía trên (thêm GD + đặt ngân sách)
#   - 1 Frame ở giữa (bộ lọc — có 3 ô: tháng, loại, danh mục)
#   - 1 Treeview (bảng danh sách)
#   - 1 Label (thống kê)
# ============================================================


# tk.Tk() tạo cửa sổ chính (root window).
# Mỗi chương trình tkinter chỉ nên có 1 root duy nhất.
root = tk.Tk()
root.title("Quản Lý Chi Tiêu Cá Nhân")  # tiêu đề trên thanh cửa sổ
root.geometry("900x650")                  # kích thước rộng x cao (px)


# ---------- Tiêu đề lớn ở trên cùng ----------
# tk.Label(...).pack(...) là cú pháp gọi method liên tiếp:
# tạo Label rồi gọi pack() để đặt nó vào cửa sổ.
# pady=8 thêm 8px khoảng cách trên/dưới.
tk.Label(
    root,
    text="QUẢN LÝ CHI TIÊU CÁ NHÂN",
    font=("Arial", 15, "bold"),
    fg="navy",  # foreground = màu chữ
).pack(pady=8)


# ---------- Frame chứa 2 khung con (cột trái & phải) ----------
# Frame là widget vô hình dùng để nhóm các widget khác.
frm_top = tk.Frame(root)
frm_top.pack(padx=10, fill="x")  # fill="x" = dãn ngang theo cửa sổ


# ============= KHUNG THÊM GIAO DỊCH (cột trái) =============
# LabelFrame giống Frame nhưng có viền và tiêu đề bên trên.
frm_nhap = tk.LabelFrame(frm_top, text="Thêm giao dịch", padx=10, pady=8)
# .grid() đặt widget theo lưới: row=0, column=0 = ô góc trái trên.
# sticky="n" = neo lên đầu (north) khi ô lớn hơn nội dung.
frm_nhap.grid(row=0, column=0, padx=5, pady=5, sticky="n")


# StringVar là biến lưu chuỗi của tkinter. Khi giá trị đổi,
# các widget liên kết với nó (radiobutton, combobox) cập nhật theo.
var_loai = tk.StringVar(value="chi")  # giá trị mặc định = "chi"

# trace_add("write", callback): mỗi khi var_loai bị ghi giá trị mới,
# tự động gọi hàm doi_danh_muc() để cập nhật combobox.
var_loai.trace_add("write", doi_danh_muc)


# Radiobutton cùng variable thì tự động loại trừ nhau (chỉ chọn được 1).
tk.Radiobutton(
    frm_nhap, text="Thu", variable=var_loai, value="thu", fg="green"
).grid(row=0, column=0)

tk.Radiobutton(
    frm_nhap, text="Chi", variable=var_loai, value="chi", fg="red"
).grid(row=0, column=1)


# ---- Hàng 1: Combobox danh mục ----
tk.Label(frm_nhap, text="Danh mục:").grid(row=1, column=0, sticky="w", pady=4)
# state="readonly": không cho gõ tay, chỉ chọn từ list.
cb_danh_muc = ttk.Combobox(frm_nhap, values=DANH_MUC_CHI, state="readonly", width=18)
cb_danh_muc.set(DANH_MUC_CHI[0])  # chọn sẵn phần tử đầu
cb_danh_muc.grid(row=1, column=1, pady=4)


# ---- Hàng 2: Số tiền ----
tk.Label(frm_nhap, text="Số tiền (đ):").grid(row=2, column=0, sticky="w", pady=4)
# Entry là ô nhập text 1 dòng.
e_so_tien = tk.Entry(frm_nhap, width=20)
e_so_tien.grid(row=2, column=1, pady=4)


# ---- Hàng 3: Ngày giao dịch (mặc định = hôm nay) ----
tk.Label(frm_nhap, text="Ngày (yyyy-mm-dd):").grid(row=3, column=0, sticky="w", pady=4)
e_ngay = tk.Entry(frm_nhap, width=20)
# datetime.now() lấy thời điểm hiện tại.
# .strftime("%Y-%m-%d") định dạng thành chuỗi "2026-05-07".
e_ngay.insert(0, datetime.now().strftime("%Y-%m-%d"))  # điền sẵn vào ô
e_ngay.grid(row=3, column=1, pady=4)


# ---- Hàng 4: Ghi chú ----
tk.Label(frm_nhap, text="Ghi chú:").grid(row=4, column=0, sticky="w", pady=4)
e_ghi_chu = tk.Entry(frm_nhap, width=20)
e_ghi_chu.grid(row=4, column=1, pady=4)


# ---- Hàng 5: Nút LƯU ----
# command=them_giao_dich: khi bấm nút sẽ gọi hàm này.
# columnspan=2 để nút trải qua cả 2 cột → cân giữa.
tk.Button(
    frm_nhap,
    text="LƯU GIAO DỊCH",
    bg="navy",   # background = màu nền
    fg="white",  # foreground = màu chữ
    width=20,
    command=them_giao_dich,
).grid(row=5, column=0, columnspan=2, pady=10)


# ============= KHUNG ĐẶT NGÂN SÁCH (cột phải) =============
frm_ns = tk.LabelFrame(frm_top, text="Đặt ngân sách tháng", padx=10, pady=8)
frm_ns.grid(row=0, column=1, padx=5, pady=5, sticky="n")


# ---- Tháng ----
tk.Label(frm_ns, text="Tháng (yyyy-mm):").grid(row=0, column=0, sticky="w", pady=4)
e_ns_thang = tk.Entry(frm_ns, width=14)
# .strftime("%Y-%m") chỉ lấy năm-tháng (vd "2026-05")
e_ns_thang.insert(0, datetime.now().strftime("%Y-%m"))
e_ns_thang.grid(row=0, column=1, pady=4)


# ---- Danh mục ----
tk.Label(frm_ns, text="Danh mục:").grid(row=1, column=0, sticky="w", pady=4)
cb_ns_dm = ttk.Combobox(frm_ns, values=DANH_MUC_CHI, state="readonly", width=14)
cb_ns_dm.set(DANH_MUC_CHI[0])
cb_ns_dm.grid(row=1, column=1, pady=4)


# ---- Hạn mức ----
tk.Label(frm_ns, text="Hạn mức (đ):").grid(row=2, column=0, sticky="w", pady=4)
e_ns_hanmuc = tk.Entry(frm_ns, width=14)
e_ns_hanmuc.grid(row=2, column=1, pady=4)


# ---- Nút LƯU NGÂN SÁCH ----
tk.Button(
    frm_ns,
    text="LƯU NGÂN SÁCH",
    bg="green",
    fg="white",
    width=18,
    command=luu_ngan_sach_ui,
).grid(row=3, column=0, columnspan=2, pady=10)


# ============= KHUNG LỌC (yêu cầu 4) =============
# Có 3 bộ lọc: tháng, loại (thu/chi), danh mục
frm_loc = tk.Frame(root)
frm_loc.pack(padx=10, pady=3, fill="x")


# ---- Lọc theo tháng ----
tk.Label(frm_loc, text="Lọc tháng (yyyy-mm):").pack(side="left", padx=4)
e_loc_thang = tk.Entry(frm_loc, width=10)
# pack(side="left") xếp các widget từ trái sang phải (thay vì xếp dọc)
e_loc_thang.pack(side="left", padx=4)


# ---- Lọc theo loại ----
tk.Label(frm_loc, text="Loại:").pack(side="left", padx=4)
var_loai_loc = tk.StringVar(value="tat_ca")
ttk.Combobox(
    frm_loc,
    textvariable=var_loai_loc,  # liên kết combobox với biến để dễ get/set
    values=["tat_ca", "thu", "chi"],
    width=8,
    state="readonly",
).pack(side="left", padx=4)


# ---- Lọc theo danh mục (yêu cầu 4 đề bắt buộc) ----
tk.Label(frm_loc, text="Danh mục:").pack(side="left", padx=4)
var_dm_loc = tk.StringVar(value="tat_ca")
# Gộp cả danh mục thu + chi vào 1 list để chọn
ttk.Combobox(
    frm_loc,
    textvariable=var_dm_loc,
    values=["tat_ca"] + DANH_MUC_THU + DANH_MUC_CHI,
    width=14,
    state="readonly",
).pack(side="left", padx=4)


# ---- Nút Lọc và Hiện tất cả ----
tk.Button(frm_loc, text="Lọc", width=6, command=hien_thi_danh_sach).pack(
    side="left", padx=4
)
tk.Button(frm_loc, text="Hiện tất cả", width=10, command=hien_tat_ca).pack(
    side="left", padx=4
)


# ============= BẢNG DANH SÁCH GIAO DỊCH (Treeview) =============
# Treeview là widget bảng có nhiều cột.
# columns=(...) khai báo TÊN của 5 cột (chưa phải tiêu đề hiển thị).
# show="headings" để chỉ hiện phần header, không hiện cột "tree" mặc định.
tree = ttk.Treeview(
    root,
    columns=("ngay", "loai", "danh_muc", "so_tien", "ghi_chu"),
    show="headings",
    height=12,  # số dòng nhìn thấy cùng lúc
)


# .heading() đặt tiêu đề chữ hiển thị trên đầu mỗi cột.
tree.heading("ngay", text="Ngày")
tree.heading("loai", text="Loại")
tree.heading("danh_muc", text="Danh mục")
tree.heading("so_tien", text="Số tiền")
tree.heading("ghi_chu", text="Ghi chú")


# .column() đặt độ rộng (px) cho từng cột.
tree.column("ngay", width=100)
tree.column("loai", width=55)
tree.column("danh_muc", width=130)
tree.column("so_tien", width=120)
tree.column("ghi_chu", width=280)


tree.pack(padx=10, pady=5, fill="x")


# ============= NHÃN THỐNG KÊ Ở DƯỚI =============
# Nhãn này hiển thị: tổng thu, tổng chi, tiết kiệm tháng, cộng dồn
# bg="#e8f4fd" là màu xanh nhạt (mã hex) làm nền cho nổi bật.
lbl_tk = tk.Label(root, text="", font=("Arial", 10, "bold"), fg="navy", bg="#e8f4fd")
lbl_tk.pack(pady=5, fill="x", padx=10)


# Khi mở app lần đầu, hiển thị danh sách + thống kê ngay
hien_thi_danh_sach()


# ============================================================
# PHẦN 6: HOT-RELOAD (tự khởi động lại khi sửa code)
# ------------------------------------------------------------
# Tiện ích phụ — không thuộc yêu cầu đề.
# Mỗi 1 giây kiểm tra xem file final.py có bị sửa không.
# Nếu có thì tự đóng app và mở lại với code mới.
# ============================================================


# os.path.getmtime(file) trả về timestamp lần cuối file được sửa.
# __file__ là tên file đang chạy (ở đây = "final.py").
# Lưu lại thời điểm app được mở để so sánh sau này.
thoi_gian_mo = os.path.getmtime(__file__)


def kiem_tra_code_moi():
    """Hàm chạy mỗi 1 giây để kiểm tra file đã đổi chưa."""
    thoi_gian_hien_tai = os.path.getmtime(__file__)

    # Nếu thời gian sửa khác lúc mở app → file đã được sửa
    if thoi_gian_hien_tai != thoi_gian_mo:
        # os.execv thay thế process Python hiện tại bằng process mới.
        # sys.executable: đường dẫn tới python.exe.
        # sys.argv: list tham số, vd ["final.py"].
        # → khởi động lại app với code mới
        os.execv(sys.executable, [sys.executable] + sys.argv)

    # root.after(1000, func): yêu cầu tkinter gọi `func` sau 1000ms (1s).
    # Cách này chạy không chặn giao diện (khác với time.sleep).
    root.after(1000, kiem_tra_code_moi)


# Lên lịch chạy lần đầu sau 1 giây kể từ khi app khởi động
root.after(1000, kiem_tra_code_moi)


# ============================================================
# PHẦN 7: CHẠY VÒNG LẶP SỰ KIỆN
# ============================================================
# mainloop() khiến cửa sổ tkinter "chạy mãi", lắng nghe các sự
# kiện chuột/bàn phím cho đến khi người dùng đóng cửa sổ.
# Đây phải là dòng cuối cùng của chương trình.
root.mainloop()
