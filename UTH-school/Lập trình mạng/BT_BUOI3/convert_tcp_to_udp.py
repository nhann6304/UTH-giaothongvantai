"""
Script chuyển đổi tự động các file còn lại từ TCP sang UDP
"""

import os
import re


def convert_tcp_to_udp(file_path):
    """Chuyển đổi file từ TCP sang UDP"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Thay đổi SOCK_STREAM thành SOCK_DGRAM
    content = content.replace("SOCK_STREAM", "SOCK_DGRAM")

    # Loại bỏ các dòng listen và accept (server)
    content = re.sub(r".*\.listen\(.*\)\s*\n", "", content)
    content = re.sub(r"conn,\s*addr\s*=\s*.*\.accept\(\)\s*\n", "", content)
    content = re.sub(r"print\(.*kết nối.*\)\s*\n", "", content)

    # Thay client.connect thành comment
    content = re.sub(r"client\.connect\(.*\)\s*\n", "", content)

    # Ghi chú: File này cần được chỉnh sửa thủ công để hoàn thiện
    # vì mỗi file có logic riêng

    return content


# Danh sách các file cần xử lý
files_to_convert = [
    "client6.py",
    "client7.py",
    "client8.py",
    "client9.py",
    "client10.py",
    "server6.py",
    "server7.py",
    "server8.py",
    "server9.py",
    "server10.py",
]

print("⚠️  Script này chỉ thực hiện chuyển đổi cơ bản.")
print("Bạn cần chỉnh sửa thủ công các file sau khi chạy script!")
print("\nCác file cần xem xét thủ công:", ", ".join(files_to_convert))
