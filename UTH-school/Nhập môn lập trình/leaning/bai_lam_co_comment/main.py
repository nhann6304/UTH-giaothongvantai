# ==============================================================
# FILE: main.py
# VAI TRÒ: Điểm khởi chạy chương trình (Entry Point)
# Đây là file Python chạy ĐẦU TIÊN khi gõ lệnh: python main.py
# Nó chỉ có 1 nhiệm vụ duy nhất: gọi hàm chay() trong giao_dien.py
# ==============================================================

# "import giao_dien" : nạp toàn bộ file giao_dien.py vào chương trình
# Khi import, Python thực thi tất cả code ở cấp module (ngoài hàm):
#   - Tạo cửa sổ root = tk.Tk()
#   - Tạo tất cả widget (Label, Entry, Button, Treeview,...)
#   - Định nghĩa tất cả hàm (them_giao_dich, hien_thi_danh_sach,...)
# Sau khi import xong, ta gọi hàm chay() để mở cửa sổ
import giao_dien

# giao_dien.chay() : gọi hàm chay() trong module giao_dien
# Hàm chay() sẽ:
#   1. Gọi hien_thi_danh_sach() để load dữ liệu lên bảng
#   2. Gọi root.mainloop() để cửa sổ hiện ra và chờ người dùng tương tác
giao_dien.chay()
