import subprocess
import pyautogui
import time
import pygetwindow as gw
from pywinauto import Desktop

path = r"C:\Users\Public\Desktop\Rise of Kingdoms.lnk"


def open_game_and_start():
    try:
        # --- BƯỚC 1 & 2: Mở và nhấn Yes UAC ---
        print("Đang khởi động Launcher...")
        subprocess.Popen(f'start "" "{path}"', shell=True)
        time.sleep(4)

        print("Đang xử lý UAC (Nhấn Alt+Tab và Enter)...")
        pyautogui.hotkey("alt", "tab")
        time.sleep(1)
        pyautogui.press("left")
        pyautogui.press("enter")

        # --- BƯỚC 3: TÌM CỬA SỔ BẰNG CÔNG NGHỆ UIA ---
        launcher_win = None
        print("Đang tìm cửa sổ bằng cách quét chiều sâu...")

        # --- BƯỚC 3: TÌM CỬA SỔ (LỌC LOẠI TRỪ VS CODE) ---

        for i in range(20):
            windows = Desktop(backend="uia").windows()
            for w in windows:
                info = w.window_text()
                rect = w.rectangle()
                width = rect.width()
                height = rect.height()

                # ĐIỀU KIỆN LỌC MỚI:
                # 1. To (width > 1000)
                # 2. Không chứa các từ khóa của phần mềm lập trình
                # 3. Quan trọng: Launcher thường có title trống '' hoặc 'Rise of Kingdoms'
                blacklist = [
                    "VS CODE",
                    "ANTIGRAVITY",
                    "MAIN.PY",
                    "TERMINAL",
                    "PROGRAM MANAGER",
                ]
                is_blacklisted = any(x in info.upper() for x in blacklist)

                if width > 1000 and height > 500 and not is_blacklisted:
                    # In ra để mình kiểm tra xem đúng là game chưa
                    print(
                        f"==> ĐÃ TÌM THẤY ĐỐI TƯỢNG: '{info}' | Size: {width}x{height}"
                    )
                    w.set_focus()
                    launcher_win = w
                    break

        if not launcher_win:
            print(
                "LỖI: Game đã mở nhưng hệ thống bảo mật Windows chặn không cho Script nhìn thấy."
            )
            print("Hãy chắc chắn bạn đã chạy VS Code bằng quyền ADMIN!")
            return

        # --- BƯỚC 4: CLICK START (Dùng tọa độ của pywinauto) ---
        time.sleep(2)
        rect = launcher_win.rectangle()

        # Tính toán tọa độ tỉ lệ từ khung hình của pywinauto
        target_x = rect.left + int(rect.width() * 0.82)
        target_y = rect.top + int(rect.height() * 0.78)

        print(f"Click vào tọa độ: {target_x}, {target_y}")
        pyautogui.click(target_x, target_y)
        print("--- NGON LÀNH ---")

    except Exception as e:
        print(f"Lỗi: {e}")


if __name__ == "__main__":
    open_game_and_start()
