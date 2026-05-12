# ==============================================================
# FILE: giao_dien.py
# VAI TRÒ: Tầng giao diện (UI Layer)
#   - Tạo cửa sổ và các widget (nút, ô nhập, bảng, nhãn,...)
#   - Định nghĩa các hàm xử lý sự kiện khi người dùng bấm nút
#   - Gọi sang ham_xu_ly.py để đọc/ghi file và tính toán
# ==============================================================


# ------ IMPORT THƯ VIỆN ------

# "tkinter" là thư viện CÓ SẴN trong Python để tạo GUI (giao diện đồ họa)
# Viết tắt thành "tk" để gọi ngắn hơn: tk.Label, tk.Button, tk.Entry,...
import tkinter as tk

# "ttk" (themed tkinter): bộ widget đẹp hơn bộ gốc
#   - ttk.Combobox  : ô dropdown chọn từ danh sách
#   - ttk.Treeview  : bảng dữ liệu nhiều cột
# "messagebox": tạo các hộp thoại popup
#   - messagebox.showinfo()    : popup thông báo thành công (xanh)
#   - messagebox.showwarning() : popup cảnh báo (vàng)
#   - messagebox.showerror()   : popup lỗi (đỏ)
from tkinter import ttk, messagebox

# "datetime" dùng để xử lý ngày giờ
#   - datetime.now()           : lấy thời điểm hiện tại
#   - datetime.now().strftime(): định dạng ngày thành chuỗi "YYYY-MM-DD"
#   - datetime.strptime()      : kiểm tra chuỗi có đúng định dạng ngày không
from datetime import datetime

# Import file ham_xu_ly.py và đặt bí danh "h"
# Từ đây gọi hàm bằng: h.doc_giao_dich(), h.tinh_tong(), ...
# Dùng bí danh "h" để viết ngắn hơn "ham_xu_ly.doc_giao_dich()"
import ham_xu_ly as h

# ------ HẰNG SỐ: DANH SÁCH DANH MỤC ------

# Viết HOA vì đây là hằng số (CONSTANT) - giá trị không thay đổi
# Khi người dùng chọn radio "Thu" → combobox danh mục hiện DANH_MUC_THU
# Khi người dùng chọn radio "Chi" → combobox danh mục hiện DANH_MUC_CHI
DANH_MUC_THU = ["Lương", "Thưởng", "Đầu tư", "Khác"]
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


# ==============================================================
# CÁC HÀM XỬ LÝ SỰ KIỆN (Event Handlers)
# Mỗi hàm được "gắn" vào 1 nút hoặc 1 sự kiện cụ thể
# ==============================================================


def doi_danh_muc(*args):
    # Hàm này TỰ ĐỘNG chạy mỗi khi người dùng bấm radio "Thu" hoặc "Chi"
    # Nhờ dòng: var_loai.trace_add("write", doi_danh_muc) bên dưới
    #
    # *args : nhận các tham số phụ Tkinter tự truyền vào khi trace kích hoạt
    # Ta không dùng args nhưng BẮT BUỘC khai báo, nếu không Python báo lỗi

    # Lấy giá trị hiện tại của radio button: "thu" hoặc "chi"
    loai = var_loai.get()

    if loai == "thu":
        # Cập nhật danh sách của combobox danh mục sang nhóm THU
        # config(values=...) : thay đổi thuộc tính của widget
        cb_danh_muc.config(values=DANH_MUC_THU)
        # Đặt giá trị hiển thị mặc định = phần tử đầu tiên
        # DANH_MUC_THU[0] = "Lương"
        cb_danh_muc.set(DANH_MUC_THU[0])
    else:
        # Ngược lại (loai == "chi") → hiện danh mục CHI
        cb_danh_muc.config(values=DANH_MUC_CHI)
        # DANH_MUC_CHI[0] = "Ăn uống"
        cb_danh_muc.set(DANH_MUC_CHI[0])


def them_giao_dich():
    # Hàm này chạy khi người dùng bấm nút "LƯU GIAO DỊCH"
    # Được gắn qua: command=them_giao_dich trong khai báo nút
    #
    # QUY TRÌNH 6 BƯỚC:
    # B1) Đọc giá trị từ các ô nhập trên giao diện
    # B2) Kiểm tra hợp lệ (validate): rỗng? sai số? sai ngày?
    # B3) Tạo dict giao dịch mới với id tự tăng
    # B4) Ghi vào file JSON
    # B5) Thông báo + dọn ô + vẽ lại bảng
    # B6) Nếu là Chi → kiểm tra vượt ngân sách

    # === B1: ĐỌC GIÁ TRỊ TỪ GIAO DIỆN ===

    # var_loai.get() : đọc giá trị radio đang chọn → "thu" hoặc "chi"
    loai = var_loai.get()

    # cb_danh_muc.get() : đọc lựa chọn trong combobox danh mục
    # .strip()          : xóa khoảng trắng thừa ở đầu và cuối chuỗi
    #   VD: "  Ăn uống  " → "Ăn uống"
    danh_muc = cb_danh_muc.get().strip()

    # e_so_tien.get() : đọc nội dung ô Entry số tiền (trả về chuỗi string)
    # Lưu ý: Entry luôn trả về STRING, cần convert sang int sau
    so_tien_str = e_so_tien.get().strip()

    # Tương tự cho ngày và ghi chú
    ngay = e_ngay.get().strip()
    ghi_chu = e_ghi_chu.get().strip()

    # === B2a: KIỂM TRA TRƯỜNG RỖNG ===

    # "not danh_muc" = True khi danh_muc là chuỗi rỗng ""
    # Dùng "or" → chỉ cần 1 trong 3 rỗng là hiện cảnh báo
    if not danh_muc or not so_tien_str or not ngay:
        # showwarning(tiêu_đề, nội_dung) : hiện hộp thoại màu vàng
        messagebox.showwarning(
            "Lỗi nhập liệu", "Vui lòng nhập đầy đủ Danh mục, Số tiền và Ngày!"
        )
        # "return" không có giá trị: thoát khỏi hàm ngay lập tức
        # → không thực hiện các bước tiếp theo
        return

    # === B2b: KIỂM TRA SỐ TIỀN ===

    # Dùng try/except để bắt lỗi khi chuyển đổi kiểu dữ liệu
    try:
        # int(chuỗi) : chuyển string → số nguyên
        # Sẽ ném ra ValueError nếu chuỗi không phải số nguyên hợp lệ
        # VD: int("abc") → ValueError; int("10.5") → ValueError
        so_tien = int(so_tien_str)

        # Kiểm tra thêm: số tiền phải > 0 (không chấp nhận âm hoặc bằng 0)
        if so_tien <= 0:
            messagebox.showwarning("Lỗi nhập liệu", "Số tiền phải lớn hơn 0!")
            return  # Thoát hàm, không lưu
    except ValueError:
        # Vào đây khi int() thất bại (nhập chữ, dấu phẩy, số thực,...)
        messagebox.showwarning(
            "Lỗi nhập liệu",
            "Số tiền phải là số nguyên (không chứa chữ hoặc ký tự đặc biệt)!",
        )
        return

    # === B2c: KIỂM TRA ĐỊNH DẠNG NGÀY ===

    try:
        # datetime.strptime(chuỗi, định_dạng)
        # Kiểm tra chuỗi ngày có đúng định dạng "YYYY-MM-DD" không
        # VD: "2026-05-11" → hợp lệ; "11/05/2026" → ValueError
        # Ta không dùng kết quả trả về, chỉ cần biết có lỗi hay không
        datetime.strptime(ngay, "%Y-%m-%d")
    except ValueError:
        # Vào đây khi ngày sai định dạng hoặc ngày không tồn tại
        # VD: "2026-13-01" (tháng 13 không có) cũng bị lỗi
        messagebox.showwarning(
            "Lỗi nhập liệu", "Ngày phải nhập đúng định dạng YYYY-MM-DD!"
        )
        return

    # === B3: TẠO ID MỚI VÀ DICT GIAO DỊCH ===

    # Đọc danh sách hiện có từ file để tính id mới
    ds = h.doc_giao_dich()

    # Tạo id mới = id lớn nhất hiện có + 1
    # [gd["id"] for gd in ds] : list comprehension, lấy tất cả id ra list
    #   VD: ds có 3 giao dịch id=1,2,3 → [1, 2, 3]
    # max([1,2,3]) = 3 → id_moi = 4
    # default=0 : nếu ds rỗng (list comprehension trả về []) thì max = 0
    #   → id_moi = 0 + 1 = 1 (giao dịch đầu tiên)
    id_moi = max([gd["id"] for gd in ds], default=0) + 1

    # Tạo dict chứa thông tin giao dịch mới
    # Dict là cấu trúc key-value, truy cập bằng gd["key"]
    gd_moi = {
        "id": id_moi,  # số nguyên, tự tăng
        "loai": loai,  # "thu" hoặc "chi"
        "danh_muc": danh_muc,
        "so_tien": so_tien,  # số nguyên (đã convert ở B2b)
        "ngay": ngay,  # chuỗi "YYYY-MM-DD"
        "ghi_chu": ghi_chu,  # chuỗi, có thể rỗng ""
    }

    # === B4: GHI VÀO FILE JSON ===

    # Thêm giao dịch mới vào cuối danh sách
    # append(phần_tử) : thêm vào cuối list, thay đổi list gốc trực tiếp
    ds.append(gd_moi)

    # Ghi toàn bộ danh sách (bao gồm giao dịch mới) xuống file
    h.luu_giao_dich(ds)

    # === B5: THÔNG BÁO + DỌN Ô NHẬP + VẼ LẠI BẢNG ===

    # showinfo() : popup thông báo thành công (màu xanh)
    # f"..." : f-string, cho phép nhúng biểu thức vào chuỗi bằng {}
    # loai.upper() : chuyển thành CHỮ HOA → "THU" hoặc "CHI"
    # {so_tien:,} : định dạng số có dấu phẩy phân cách hàng nghìn
    #   VD: 2500000 → "2,500,000"
    messagebox.showinfo(
        "Thành công", f"Đã lưu giao dịch:\n[{loai.upper()}] {danh_muc} - {so_tien:,} đ"
    )

    # Xóa nội dung ô nhập số tiền (giữ ngày để nhập giao dịch tiếp cho nhanh)
    # delete(0, tk.END) : xóa từ vị trí 0 đến cuối (tk.END)
    e_so_tien.delete(0, tk.END)
    e_ghi_chu.delete(0, tk.END)

    # Gọi hàm vẽ lại bảng để giao dịch mới hiện lên ngay
    hien_thi_danh_sach()

    # === B6: KIỂM TRA NGÂN SÁCH (chỉ khi là Chi) ===

    if loai == "chi":
        # Cắt lấy "YYYY-MM" từ chuỗi ngày "YYYY-MM-DD"
        # VD: "2026-05-11"[:7] = "2026-05"
        thang = ngay[:7]
        # Gọi hàm kiểm tra ngân sách với danh mục và tháng vừa nhập
        canh_bao_ngan_sach(danh_muc, thang)


def luu_ngan_sach_ui():
    # Hàm này chạy khi bấm nút "LƯU NGÂN SÁCH"
    # Lưu hạn mức chi tiêu cho 1 danh mục trong 1 tháng
    #
    # Cấu trúc lưu trong budgets.json:
    # {
    #   "2026-05": {
    #     "Ăn uống": 500000,
    #     "Học tập": 200000
    #   }
    # }

    # Đọc 3 ô nhập từ khung "Đặt ngân sách tháng"
    thang = e_ns_thang.get().strip()  # VD: "2026-05"
    danh_muc = cb_ns_dm.get().strip()  # VD: "Ăn uống"
    han_muc_str = e_ns_hanmuc.get().strip()  # VD: "500000" (string)

    # Kiểm tra có ô nào bị rỗng không
    if not thang or not danh_muc or not han_muc_str:
        messagebox.showwarning(
            "Thiếu thông tin", "Vui lòng nhập đầy đủ tháng, danh mục và hạn mức."
        )
        return

    # Kiểm tra hạn mức là số nguyên dương
    try:
        han_muc = int(han_muc_str)
        if han_muc <= 0:
            # raise ValueError : tự tạo ra lỗi ValueError để nhảy xuống except
            # Dùng cách này để xử lý chung 1 chỗ thay vì viết messagebox 2 lần
            raise ValueError
    except ValueError:
        messagebox.showerror("Lỗi", "Hạn mức phải là số nguyên dương.")
        return

    # Đọc dict ngân sách hiện có từ file
    ns = h.doc_ngan_sach()

    # Kiểm tra tháng đã có trong dict chưa
    # "thang not in ns" : True khi key "2026-05" chưa có trong ns
    if thang not in ns:
        # Tạo dict rỗng cho tháng này để có thể gán danh mục vào
        ns[thang] = {}

    # Gán hạn mức cho danh mục thuộc tháng đó
    # Nếu đã có → ghi đè; nếu chưa có → tạo mới
    ns[thang][danh_muc] = han_muc

    # Ghi dict ngân sách (đã cập nhật) xuống file
    h.luu_ngan_sach(ns)

    messagebox.showinfo(
        "Thành công", f"Đã lưu ngân sách:\n{danh_muc} | Tháng {thang}: {han_muc:,} đ"
    )

    # Ngay sau khi lưu, kiểm tra xem hiện tại đã vượt hạn mức chưa
    # (trường hợp người dùng đặt hạn mức thấp hơn số đã chi)
    canh_bao_ngan_sach(danh_muc, thang)


def canh_bao_ngan_sach(danh_muc, thang):
    # Hàm kiểm tra và hiện cảnh báo nếu CHI >= HẠN MỨC
    # Được gọi từ: them_giao_dich() và luu_ngan_sach_ui()

    # Đọc dữ liệu mới nhất từ file (để luôn có số liệu cập nhật)
    ns = h.doc_ngan_sach()
    ds = h.doc_giao_dich()

    # Kiểm tra xem có ngân sách cho tháng+danh_mục này không
    # Nếu không có → không cần cảnh báo, thoát luôn
    # "thang not in ns" : tháng chưa có trong ngân sách
    # "danh_muc not in ns[thang]" : danh mục chưa có trong tháng đó
    if thang not in ns or danh_muc not in ns[thang]:
        return  # Không có ngân sách → không cảnh báo

    # Lấy hạn mức đã đặt cho danh mục/tháng này
    han_muc = ns[thang][danh_muc]

    # Tính tổng đã chi cho danh mục này trong tháng này
    tong_chi = h.tinh_tong_theo_danh_muc(ds, danh_muc, thang)

    # So sánh: nếu đã chi >= hạn mức → hiện cảnh báo
    # Dùng >= (lớn hơn hoặc bằng) để cảnh báo ngay khi chạm hạn mức
    if tong_chi >= han_muc:
        messagebox.showwarning(
            "Cảnh báo vượt ngân sách!!!",
            # Nội dung popup gồm nhiều dòng, dùng \n để xuống dòng
            # f-string nhiều dòng: Python tự ghép lại thành 1 chuỗi
            f"Danh mục: {danh_muc}\n"
            f"Tháng: {thang}\n"
            f"Hạn mức: {han_muc:,} đ\n"
            f"Đã chi: {tong_chi:,} đ\n"
            f"Vượt: {tong_chi - han_muc:,} đ",  # có thể = 0 nếu chạm đúng hạn mức
        )


# xong Nhân
def hien_thi_danh_sach():
    # Hàm hiển thị danh sách giao dịch lên bảng Treeview
    # Được gọi khi: mở app, thêm giao dịch, bấm Lọc, bấm Hiện tất cả

    # === ĐỌC CÁC BỘ LỌC TỪ GIAO DIỆN ===

    # Lấy giá trị ô lọc tháng (có thể rỗng = không lọc theo tháng)
    thang = e_loc_thang.get().strip()

    # Lấy giá trị combobox loại lọc
    loai_loc = var_loai_loc.get()

    # Combobox lưu "tat_ca" khi chọn "tất cả"
    # Hàm loc_giao_dich() hiểu "" = không lọc → cần đổi "tat_ca" thành ""
    if loai_loc == "tat_ca":
        loai_loc = ""

    # Tương tự cho bộ lọc danh mục
    dm_loc = var_dm_loc.get()
    if dm_loc == "tat_ca":
        dm_loc = ""

    # === LỌC DỮ LIỆU ===

    # Đọc toàn bộ giao dịch từ file
    ds = h.doc_giao_dich()

    # Lọc theo các tiêu chí đã chọn
    # Nếu cả 3 tham số đều "" → trả về toàn bộ ds
    ket_qua = h.loc_giao_dich(ds, thang, loai_loc, dm_loc)

    # === SẮP XẾP GIẢM DẦN THEO NGÀY (Bubble Sort) ===
    # Mục đích: giao dịch MỚI NHẤT hiển thị ở trên cùng bảng
    #
    # Bubble Sort (sắp xếp nổi bọt):
    # Duyệt nhiều lần, mỗi lần so sánh cặp kề nhau và đổi chỗ nếu sai thứ tự
    # Sau mỗi lần duyệt, phần tử nhỏ nhất "nổi" về đúng vị trí
    #
    # Vòng ngoài: i chạy từ 0 đến len-2
    for i in range(len(ket_qua) - 1):
        # Vòng trong: j chạy từ i+1 đến cuối
        for j in range(i + 1, len(ket_qua)):
            # So sánh ngày: chuỗi "YYYY-MM-DD" có thể so sánh thẳng
            # ket_qua[i]["ngay"] < ket_qua[j]["ngay"]
            # nghĩa là: phần tử i có ngày NHỎ HƠN (cũ hơn) phần tử j
            # → cần đổi chỗ để ngày lớn hơn (mới hơn) lên trước
            if ket_qua[i]["ngay"] < ket_qua[j]["ngay"]:
                # Hoán đổi 2 phần tử bằng cú pháp Python: a, b = b, a
                ket_qua[i], ket_qua[j] = ket_qua[j], ket_qua[i]
            #
            # Nếu ngày bằng nhau → cũng đổi chỗ (đảo thứ tự cặp đó)
            if ket_qua[i]["ngay"] == ket_qua[j]["ngay"]:
                ket_qua[i], ket_qua[j] = ket_qua[j], ket_qua[i]

    # === XÓA BẢNG CŨ ===

    # tree.get_children() : trả về tuple id của tất cả dòng đang có trong bảng
    # Phải xóa hết trước khi đổ dữ liệu mới, tránh bị hiển thị trùng
    for row in tree.get_children():
        tree.delete(row)  # xóa từng dòng theo id

    # === ĐỔ DỮ LIỆU MỚI VÀO BẢNG ===

    for gd in ket_qua:
        # Chuyển "thu"/"chi" thành chữ hiển thị đẹp hơn
        # Đây là biểu thức điều kiện rút gọn (ternary):
        # ten_loai = "Thu" nếu gd["loai"] == "thu", ngược lại = "Chi"
        ten_loai = "Thu" if gd["loai"] == "thu" else "Chi"

        # tree.insert(parent, position, values=(...))
        #   - ""    : parent rỗng = thêm vào gốc (không phải con của dòng nào)
        #   - "end" : thêm vào cuối bảng
        #   - values: tuple các giá trị, mỗi phần tử = 1 cột
        tree.insert(
            "",
            "end",
            values=(
                gd["ngay"],  # cột Ngày
                ten_loai,  # cột Loại
                gd["danh_muc"],  # cột Danh mục
                f"{gd['so_tien']:,} đ",  # cột Số tiền (có dấu phẩy)
                gd.get("ghi_chu", ""),  # cột Ghi chú
                # .get("ghi_chu", "") : lấy giá trị key "ghi_chu"
                # Nếu key không tồn tại → trả về "" thay vì báo lỗi KeyError
            ),
        )

    # === CẬP NHẬT NHÃN THỐNG KÊ ===

    # Xác định tháng để tính thống kê:
    # Nếu người dùng đang lọc theo tháng cụ thể → dùng tháng đó
    # Nếu không lọc (thang == "") → mặc định lấy tháng hiện tại
    thang_tk = thang if thang != "" else datetime.now().strftime("%Y-%m")

    # Tính các số liệu thống kê bằng các hàm trong ham_xu_ly
    tong_thu = h.tinh_tong(ds, "thu", thang_tk)
    tong_chi = h.tinh_tong(ds, "chi", thang_tk)

    # Tiết kiệm tháng = Thu - Chi trong tháng đó
    tiet_kiem_t = tong_thu - tong_chi

    # Tiết kiệm cộng dồn = tích lũy từ đầu đến tháng đó
    tiet_kiem_cd = h.tinh_tiet_kiem_cong_don(ds, thang_tk)

    # Cập nhật text của nhãn lbl_tk
    # config(text=...) : thay đổi nội dung hiển thị của Label
    lbl_tk.config(
        text=(
            f"Tháng {thang_tk}:   "
            f"Thu {tong_thu:,} đ   |   "
            f"Chi {tong_chi:,} đ   |   "
            f"Tiết kiệm tháng: {tiet_kiem_t:,} đ   |   "
            f"Cộng dồn: {tiet_kiem_cd:,} đ"
        )
    )


# xong Nhân
def hien_tat_ca():
    # Hàm này chạy khi bấm nút "Hiện tất cả"
    # Mục đích: xóa hết bộ lọc và hiện lại toàn bộ giao dịch

    # Xóa nội dung ô lọc tháng (trở về rỗng = không lọc theo tháng)
    e_loc_thang.delete(0, tk.END)

    # Đặt lại combobox loại về "tat_ca" (= không lọc theo loại)
    var_loai_loc.set("tat_ca")

    # Đặt lại combobox danh mục về "tat_ca" (= không lọc theo danh mục)
    var_dm_loc.set("tat_ca")

    # Gọi hàm hiển thị lại (lúc này cả 3 bộ lọc đều = "" → hiện tất cả)
    hien_thi_danh_sach()


# ==============================================================
# TẠO CỬA SỔ CHÍNH VÀ CÁC WIDGET
# Đoạn code này chạy NGAY KHI file được import (không nằm trong hàm)
# Python thực thi từng dòng từ trên xuống dưới
# ==============================================================

# tk.Tk() : tạo cửa sổ gốc (root window) - BẮT BUỘC phải có trước mọi widget
root = tk.Tk()

# Đặt tiêu đề hiển thị trên thanh title bar của cửa sổ
root.title("Quản Lý Chi Tiêu Cá Nhân")

# Đặt kích thước cửa sổ: rộng 900px, cao 650px
root.geometry("900x650")

# Tạo Label tiêu đề to ở đầu cửa sổ
tk.Label(
    root,  # widget cha (đặt vào cửa sổ chính)
    text="QUẢN LÝ CHI TIÊU CÁ NHÂN",
    font=("Arial", 15, "bold"),  # font chữ Arial, cỡ 15, đậm
    fg="navy",  # fg = foreground = màu chữ (xanh navy)
).pack(pady=8)
# .pack() : layout manager đơn giản, tự xếp widget từ trên xuống
# pady=8 : thêm 8px khoảng cách phía trên và dưới widget

# Frame chứa 2 khung con: "Thêm giao dịch" (trái) và "Đặt ngân sách" (phải)
# tk.Frame : container vô hình để nhóm các widget lại
frm_top = tk.Frame(root)
frm_top.pack(padx=10, fill="x")  # fill="x" : kéo dài hết chiều ngang

# ------ KHUNG TRÁI: THÊM GIAO DỊCH ------

# tk.LabelFrame : giống Frame nhưng có viền và tiêu đề
frm_nhap = tk.LabelFrame(frm_top, text="Thêm giao dịch", padx=10, pady=8)
# .grid() : layout manager dạng lưới (hàng/cột)
# row=0, column=0 : đặt vào hàng 0, cột 0 của frm_top
# sticky="n" : căn lên trên (north)
frm_nhap.grid(row=0, column=0, padx=5, pady=5, sticky="n")

# tk.StringVar : biến đặc biệt của Tkinter, tự động cập nhật widget khi thay đổi
# value="chi" : giá trị mặc định khi mở app
var_loai = tk.StringVar(value="chi")

# trace_add("write", callback) : theo dõi biến
# Khi var_loai thay đổi (người dùng bấm radio khác) → tự gọi doi_danh_muc()
var_loai.trace_add("write", doi_danh_muc)

# 2 nút radio Thu/Chi, dùng chung biến var_loai
# Khi bấm "Thu" → var_loai = "thu"; Khi bấm "Chi" → var_loai = "chi"
tk.Radiobutton(frm_nhap, text="Thu", variable=var_loai, value="thu", fg="green").grid(
    row=0, column=0  # hàng 0, cột 0 trong frm_nhap
)
tk.Radiobutton(frm_nhap, text="Chi", variable=var_loai, value="chi", fg="red").grid(
    row=0, column=1  # hàng 0, cột 1 trong frm_nhap
)

# Hàng 1: nhãn + combobox danh mục
tk.Label(frm_nhap, text="Danh mục:").grid(row=1, column=0, sticky="w", pady=4)
# sticky="w" : căn trái (west)

# ttk.Combobox : dropdown list
# state="readonly" : chỉ được CHỌN từ danh sách, KHÔNG được gõ tự do
cb_danh_muc = ttk.Combobox(frm_nhap, values=DANH_MUC_CHI, state="readonly", width=18)
# Đặt giá trị mặc định = "Ăn uống" (phần tử đầu tiên của DANH_MUC_CHI)
cb_danh_muc.set(DANH_MUC_CHI[0])
cb_danh_muc.grid(row=1, column=1, pady=4)

# Hàng 2: nhãn + ô nhập số tiền
tk.Label(frm_nhap, text="Số tiền (đ):").grid(row=2, column=0, sticky="w", pady=4)
# tk.Entry : ô nhập văn bản 1 dòng
e_so_tien = tk.Entry(frm_nhap, width=20)
e_so_tien.grid(row=2, column=1, pady=4)

# Hàng 3: nhãn + ô nhập ngày
tk.Label(frm_nhap, text="Ngày (yyyy-mm-dd):").grid(row=3, column=0, sticky="w", pady=4)
e_ngay = tk.Entry(frm_nhap, width=20)
# insert(vị_trí, chuỗi) : chèn chuỗi vào ô Entry tại vị trí chỉ định
# 0 : chèn từ đầu ô
# datetime.now().strftime("%Y-%m-%d") : lấy ngày hôm nay dạng "2026-05-11"
e_ngay.insert(0, datetime.now().strftime("%Y-%m-%d"))
e_ngay.grid(row=3, column=1, pady=4)

# Hàng 4: nhãn + ô ghi chú
tk.Label(frm_nhap, text="Ghi chú:").grid(row=4, column=0, sticky="w", pady=4)
e_ghi_chu = tk.Entry(frm_nhap, width=20)
e_ghi_chu.grid(row=4, column=1, pady=4)

# Hàng 5: nút LƯU GIAO DỊCH
tk.Button(
    frm_nhap,
    text="LƯU GIAO DỊCH",
    bg="navy",  # bg = background = màu nền nút
    fg="white",  # fg = foreground = màu chữ
    width=20,
    command=them_giao_dich,  # gắn hàm: bấm nút → gọi them_giao_dich()
).grid(row=5, column=0, columnspan=2, pady=10)
# columnspan=2 : widget chiếm 2 cột (từ cột 0 đến cột 1)

# ------ KHUNG PHẢI: ĐẶT NGÂN SÁCH ------

frm_ns = tk.LabelFrame(frm_top, text="Đặt ngân sách tháng", padx=10, pady=8)
frm_ns.grid(row=0, column=1, padx=5, pady=5, sticky="n")  # cột 1 = bên phải

tk.Label(frm_ns, text="Tháng (yyyy-mm):").grid(row=0, column=0, sticky="w", pady=4)
e_ns_thang = tk.Entry(frm_ns, width=14)
# Mặc định hiển thị tháng hiện tại dạng "2026-05"
e_ns_thang.insert(0, datetime.now().strftime("%Y-%m"))
e_ns_thang.grid(row=0, column=1, pady=4)

tk.Label(frm_ns, text="Danh mục:").grid(row=1, column=0, sticky="w", pady=4)
cb_ns_dm = ttk.Combobox(frm_ns, values=DANH_MUC_CHI, state="readonly", width=14)
cb_ns_dm.set(DANH_MUC_CHI[0])
cb_ns_dm.grid(row=1, column=1, pady=4)

tk.Label(frm_ns, text="Hạn mức (đ):").grid(row=2, column=0, sticky="w", pady=4)
e_ns_hanmuc = tk.Entry(frm_ns, width=14)
e_ns_hanmuc.grid(row=2, column=1, pady=4)

tk.Button(
    frm_ns,
    text="LƯU NGÂN SÁCH",
    bg="green",
    fg="white",
    width=18,
    command=luu_ngan_sach_ui,  # bấm → gọi luu_ngan_sach_ui()
).grid(row=3, column=0, columnspan=2, pady=10)

# ------ KHUNG LỌC ------

# Frame nằm ngang chứa các bộ lọc
frm_loc = tk.Frame(root)
frm_loc.pack(padx=10, pady=3, fill="x")

# Các widget trong frm_loc dùng pack(side="left") để xếp NGANG từ trái sang phải
tk.Label(frm_loc, text="Lọc tháng (yyyy-mm):").pack(side="left", padx=4)
e_loc_thang = tk.Entry(frm_loc, width=10)
e_loc_thang.pack(side="left", padx=4)

# Gắn sự kiện: nhấn Enter trong ô lọc tháng → tự động lọc
# bind("<Return>", ...) : khi nhấn phím Enter (Return)
# lambda _: hien_thi_danh_sach() : hàm ẩn danh, bỏ qua tham số event (_)
e_loc_thang.bind("<Return>", lambda _: hien_thi_danh_sach())

tk.Label(frm_loc, text="Loại:").pack(side="left", padx=4)
# StringVar gắn với combobox loại lọc, giá trị mặc định = "tat_ca"
var_loai_loc = tk.StringVar(value="tat_ca")
ttk.Combobox(
    frm_loc,
    textvariable=var_loai_loc,  # gắn với biến → tự cập nhật
    values=["tat_ca", "thu", "chi"],  # danh sách chọn
    width=8,
    state="readonly",
).pack(side="left", padx=4)

tk.Label(frm_loc, text="Danh mục:").pack(side="left", padx=4)
var_dm_loc = tk.StringVar(value="tat_ca")
ttk.Combobox(
    frm_loc,
    textvariable=var_dm_loc,
    # Gộp "tat_ca" + cả danh mục Thu lẫn Chi vào 1 dropdown
    # Dùng toán tử + để nối 3 list: ["tat_ca"] + ["Lương",...] + ["Ăn uống",...]
    values=["tat_ca"] + DANH_MUC_THU + DANH_MUC_CHI,
    width=14,
    state="readonly",
).pack(side="left", padx=4)

# Nút Lọc: áp dụng bộ lọc đang chọn
tk.Button(frm_loc, text="Lọc", width=6, command=hien_thi_danh_sach).pack(
    side="left", padx=4
)
# Nút Hiện tất cả: xóa bộ lọc, hiện toàn bộ
tk.Button(frm_loc, text="Hiện tất cả", width=10, command=hien_tat_ca).pack(
    side="left", padx=4
)

# ------ BẢNG DANH SÁCH GIAO DỊCH (Treeview) ------

# ttk.Treeview : widget bảng nhiều cột
# columns : tuple chứa ID nội bộ của các cột (dùng để cấu hình)
# show="headings" : chỉ hiển thị hàng tiêu đề, không hiển thị cột cây gốc
# height=12 : số dòng tối đa hiển thị cùng lúc
tree = ttk.Treeview(
    root,
    columns=("ngay", "loai", "danh_muc", "so_tien", "ghi_chu"),
    show="headings",
    height=12,
)

# Đặt tiêu đề hiển thị cho từng cột (text = chữ hiển thị trên đầu cột)
tree.heading("ngay", text="Ngày")
tree.heading("loai", text="Loại")
tree.heading("danh_muc", text="Danh mục")
tree.heading("so_tien", text="Số tiền")
tree.heading("ghi_chu", text="Ghi chú")

# Đặt độ rộng (pixel) cho từng cột
tree.column("ngay", width=100)
tree.column("loai", width=55)
tree.column("danh_muc", width=130)
tree.column("so_tien", width=120)
tree.column("ghi_chu", width=280)

tree.pack(padx=10, pady=5, fill="x")

# ------ NHÃN THỐNG KÊ ------

# Label hiển thị tóm tắt Thu/Chi/Tiết kiệm ở cuối màn hình
lbl_tk = tk.Label(
    root,
    text="(Chưa có dữ liệu)",  # text mặc định trước khi load data
    font=("Arial", 10, "bold"),
    fg="navy",
    bg="#e8f4fd",  # màu nền xanh nhạt để nổi bật
)
lbl_tk.pack(pady=5, fill="x", padx=10)


# ==============================================================
# HÀM CHẠY (được gọi từ main.py)
# ==============================================================


def chay():
    # Hàm duy nhất được gọi từ bên ngoài (main.py gọi giao_dien.chay())
    # Bước 1: load dữ liệu và hiển thị bảng ngay khi mở app
    hien_thi_danh_sach()
    # Bước 2: bắt đầu vòng lặp sự kiện (event loop)
    # mainloop() : chạy mãi, lắng nghe các sự kiện (bấm nút, gõ phím,...)
    # Chỉ dừng khi người dùng đóng cửa sổ (bấm X)
    root.mainloop()
