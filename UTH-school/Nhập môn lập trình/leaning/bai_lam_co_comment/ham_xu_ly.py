# ==============================================================
# FILE: ham_xu_ly.py
# VAI TRÒ: Tầng xử lý dữ liệu (Logic Layer)
#   - KHÔNG chứa bất kỳ giao diện nào
#   - Chỉ chứa các HÀM thuần: đọc file, ghi file, tính toán, lọc
# LÝ DO TÁCH FILE: giúp code dễ đọc, dễ sửa, dễ tái sử dụng
#   giao_dien.py chỉ cần GỌI hàm ở đây, không cần biết bên trong làm gì
# ==============================================================


# ------ IMPORT THƯ VIỆN ------

# "json" là thư viện CÓ SẴN trong Python (không cần cài thêm)
# Dùng để chuyển đổi qua lại giữa:
#   - Chuỗi/file JSON  →  object Python (list, dict)  : json.load()
#   - Object Python    →  chuỗi/file JSON              : json.dump()
import json

# "os" là thư viện CÓ SẴN trong Python
# Dùng để làm việc với hệ điều hành:
#   - os.path.exists()  : kiểm tra file/thư mục có tồn tại không
#   - os.path.dirname() : lấy tên thư mục chứa file
#   - os.path.abspath() : chuyển đường dẫn tương đối → tuyệt đối
#   - os.path.join()    : ghép các phần thành đường dẫn đúng chuẩn HĐH
import os


# ------ XÁC ĐỊNH ĐƯỜNG DẪN FILE DỮ LIỆU ------

# __file__ : biến đặc biệt của Python, chứa đường dẫn đến file này
# os.path.abspath(__file__) : chuyển thành đường dẫn TUYỆT ĐỐI
#   VD: "e:\\...\\bai_lam\\ham_xu_ly.py"
# os.path.dirname(...)      : lấy phần thư mục (bỏ tên file)
#   VD: "e:\\...\\bai_lam"
# Lý do dùng cách này thay vì viết thẳng "budgets.json":
#   → Nếu chạy từ thư mục khác, Python vẫn tìm đúng file
_DIR = os.path.dirname(os.path.abspath(__file__))

# os.path.join(_DIR, "transactions.json") ghép thành đường dẫn đầy đủ
# VD: "e:\\...\\bai_lam\\transactions.json"
# Dùng hằng số (viết HOA) vì giá trị này không thay đổi trong chương trình
FILE_GD = os.path.join(_DIR, "transactions.json")  # GD = Giao Dịch
FILE_NS = os.path.join(_DIR, "budgets.json")        # NS = Ngân Sách


# ==============================================================
# NHÓM 1: HÀM ĐỌC / GHI FILE JSON
# ==============================================================


# Dấu "# Xong Nhân" bên dưới là ghi chú của nhóm (ai code phần này)
# Xong Nhân
def doc_giao_dich():
    # Kiểm tra file có tồn tại chưa
    # Lần đầu chạy chương trình, file chưa được tạo → không kiểm tra sẽ bị lỗi
    # os.path.exists() trả về True nếu file tồn tại, False nếu chưa có
    if not os.path.exists(FILE_GD):
        # File chưa có → trả về list rỗng, chương trình vẫn chạy bình thường
        return []

    # "with open(...) as f:" : mở file và gán vào biến f
    #   - FILE_GD : đường dẫn file cần mở
    #   - "r"     : chế độ read (chỉ đọc, không ghi)
    #   - encoding="utf-8" : đọc được tiếng Việt có dấu (ă, ê, ơ, ...)
    # Dùng "with" thay vì open() thủ công vì:
    #   → File tự động ĐÓNG khi ra khỏi khối lệnh, dù có lỗi hay không
    with open(FILE_GD, "r", encoding="utf-8") as f:
        # json.load(f) : đọc toàn bộ nội dung file JSON
        # và chuyển thành kiểu dữ liệu Python tương ứng:
        #   JSON array  → Python list
        #   JSON object → Python dict
        # Kết quả trả về là list các dict, mỗi dict = 1 giao dịch
        return json.load(f)


# Xong Nhân
def luu_giao_dich(ds):
    # ds : danh sách (list) các giao dịch cần lưu xuống file
    # Mở file ở chế độ "w" (write = ghi)
    #   - Nếu file CHƯA tồn tại → tự động TẠO MỚI
    #   - Nếu file ĐÃ tồn tại   → XÓA NỘI DUNG CŨ rồi ghi đè
    with open(FILE_GD, "w", encoding="utf-8") as f:
        # json.dump(ds, f, ...) : ghi object Python ra file dạng JSON
        #   - ds              : dữ liệu cần ghi (list các dict)
        #   - f               : file đang mở để ghi vào
        #   - ensure_ascii=False : GIỮ NGUYÊN ký tự Việt có dấu
        #       (nếu True thì "Ăn uống" sẽ bị lưu thành "Ăn uống")
        #   - indent=2 : xuống dòng + thụt lề 2 khoảng trắng cho dễ đọc
        #       (nếu không có indent, toàn bộ nội dung nằm 1 dòng, rất khó đọc)
        json.dump(ds, f, ensure_ascii=False, indent=2)


# Xong Nhân
def doc_ngan_sach():
    # Tương tự doc_giao_dich nhưng dành cho file ngân sách
    # Nếu file chưa tồn tại → trả về dict rỗng {}
    # (khác với giao dịch trả về list rỗng [] vì ngân sách lưu dạng dict)
    if not os.path.exists(FILE_NS):
        return {}

    with open(FILE_NS, "r", encoding="utf-8") as f:
        # Nội dung budgets.json có cấu trúc dict lồng nhau:
        # {
        #   "2026-05": { "Ăn uống": 500000, "Học tập": 200000 },
        #   "2026-06": { "Đi lại": 300000 }
        # }
        return json.load(f)


# Xong Nhân
def luu_ngan_sach(ns):
    # ns : dict ngân sách cần lưu xuống file
    with open(FILE_NS, "w", encoding="utf-8") as f:
        json.dump(ns, f, ensure_ascii=False, indent=2)


# ==============================================================
# NHÓM 2: HÀM TÍNH TOÁN
# ==============================================================


def tinh_tong(ds, loai, thang):
    # Mục đích: tính TỔNG SỐ TIỀN của 1 loại trong 1 tháng
    # Tham số:
    #   ds    : list giao dịch (đọc từ file)
    #   loai  : "thu" hoặc "chi"
    #   thang : chuỗi "YYYY-MM", ví dụ "2026-05"

    # Khởi tạo biến tổng = 0, sẽ cộng dần vào trong vòng lặp
    tong = 0

    # Duyệt qua TỪNG giao dịch trong danh sách
    # Mỗi gd là 1 dict: {"id":1, "loai":"chi", "ngay":"2026-05-05", ...}
    for gd in ds:
        # Điều kiện 1: gd["loai"] == loai
        #   Kiểm tra loại giao dịch có khớp không ("thu" hoặc "chi")
        # Điều kiện 2: gd["ngay"][:7] == thang
        #   gd["ngay"] có dạng "2026-05-10" (10 ký tự)
        #   [:7] cắt lấy 7 ký tự đầu → "2026-05"
        #   So sánh với tham số thang để biết giao dịch có trong tháng cần tính không
        if gd["loai"] == loai and gd["ngay"][:7] == thang:
            # Cộng dồn số tiền của giao dịch này vào tổng
            # += là viết tắt của: tong = tong + gd["so_tien"]
            tong += gd["so_tien"]

    # Trả về tổng sau khi duyệt hết danh sách
    return tong


def tinh_tong_theo_danh_muc(ds, danh_muc, thang):
    # Mục đích: tính tổng CHI của 1 danh mục cụ thể trong 1 tháng
    # Dùng để kiểm tra xem có vượt ngân sách không
    # Chỉ tính loại "chi" vì ngân sách là giới hạn chi tiêu

    tong = 0
    for gd in ds:
        # Cần thoả CẢ 3 điều kiện cùng lúc (dùng "and"):
        if (
            # Điều kiện 1: giao dịch thuộc tháng cần kiểm tra
            gd["ngay"][:7] == thang
            # Điều kiện 2: chỉ tính giao dịch loại "chi" (bỏ qua "thu")
            and gd["loai"] == "chi"
            # Điều kiện 3: đúng danh mục cần kiểm tra
            # .lower() chuyển về chữ thường để so sánh KHÔNG phân biệt hoa/thường
            # VD: "Ăn uống" và "ăn uống" đều khớp nhau
            and gd["danh_muc"].lower() == danh_muc.lower()
        ):
            tong += gd["so_tien"]
    return tong


# Thời xong
def loc_giao_dich(ds, thang="", loai="", danh_muc=""):
    # Mục đích: lọc danh sách giao dịch theo các tiêu chí
    # Tham số có giá trị mặc định = "" (chuỗi rỗng)
    # Nếu tham số = "" → KHÔNG lọc theo tiêu chí đó (cho tất cả qua)
    # VD: loc_giao_dich(ds, thang="2026-05") → chỉ lọc theo tháng,
    #     bỏ qua loại và danh mục

    # List rỗng, sẽ append các giao dịch hợp lệ vào đây
    ket_qua = []

    for gd in ds:
        # Cắt lấy "YYYY-MM" từ ngày của giao dịch đang xét
        thang_gd = gd["ngay"][:7]

        # Xây dựng từng điều kiện riêng (True/False):
        # Nếu tham số == "" → True ngay (không lọc, cho qua)
        # Nếu tham số != "" → phải so khớp với giá trị của giao dịch
        dieu_kien_thang = thang == "" or thang_gd == thang

        # .lower() để so sánh không phân biệt hoa/thường
        dieu_kien_loai = loai == "" or gd["loai"].lower() == loai.lower()

        dieu_kien_danh_muc = (
            danh_muc == "" or gd["danh_muc"].lower() == danh_muc.lower()
        )

        # CHỈ thêm vào kết quả khi THOẢ CẢ 3 điều kiện
        # "and" : tất cả phải True thì mới True
        if dieu_kien_thang and dieu_kien_loai and dieu_kien_danh_muc:
            ket_qua.append(gd)  # append : thêm phần tử vào cuối list

    return ket_qua


def tinh_tiet_kiem_cong_don(ds, thang):
    # Mục đích: tính tiết kiệm TÍCH LŨY từ đầu đến hết tháng chỉ định
    # Công thức: cộng dồn (Thu - Chi) của tất cả tháng <= tháng chỉ định
    #
    # Tại sao so sánh chuỗi "YYYY-MM" được?
    # Vì định dạng ISO 8601 (YYYY-MM) có thể sắp xếp theo bảng chữ cái
    # mà vẫn đúng thứ tự thời gian:
    #   "2026-03" < "2026-05" → đúng (tháng 3 trước tháng 5)
    #   "2025-12" < "2026-01" → đúng (2025 trước 2026)

    # Biến tích lũy, bắt đầu từ 0
    tiet_kiem_cd = 0

    for gd in ds:
        # Chỉ tính những giao dịch trong tháng <= tháng cần xem
        # VD: thang = "2026-05" → tính cả tháng 3, 4, 5 (bỏ qua 6, 7, ...)
        if gd["ngay"][:7] <= thang:
            if gd["loai"] == "thu":
                # Giao dịch thu → CỘNG vào tích lũy
                tiet_kiem_cd += gd["so_tien"]
            else:
                # Giao dịch chi → TRỪ khỏi tích lũy
                # (else ở đây nghĩa là loai == "chi")
                tiet_kiem_cd -= gd["so_tien"]

    return tiet_kiem_cd
