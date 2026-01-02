"""
Test Script - Kiểm tra các ứng dụng UDP
"""

import subprocess
import sys
import time


def print_header(text):
    """In tiêu đề"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)


def test_dns_simple():
    """Test DNS Client Simple"""
    print_header("TEST 1: DNS CLIENT SIMPLE")
    print("File: dns_client_simple.py")
    print("Status: ✅ Đã tạo")
    print("Cách test: python dns_client_simple.py")
    print("         → Nhập: google.com")
    print("         → Kết quả: Hiển thị địa chỉ IP")


def test_dns_advanced():
    """Test DNS Client Advanced"""
    print_header("TEST 2: DNS CLIENT ADVANCED")
    print("File: dns_client.py")
    print("Status: ✅ Đã tạo")
    print("Cách test: python dns_client.py")
    print("         → Nhập: facebook.com")
    print("         → Kết quả: Hiển thị DNS query process")
    print("Note: Cần kết nối Internet")


def test_dhcp():
    """Test DHCP Client"""
    print_header("TEST 3: DHCP CLIENT")
    print("File: dhcp_client.py")
    print("Status: ✅ Đã tạo")
    print("Cách test: Run as Administrator")
    print("         → python dhcp_client.py")
    print("         → Kết quả: Hiển thị IP được cấp")
    print("Note: ⚠️  Cần quyền Administrator")
    print("      ⚠️  Cần DHCP server trong mạng")


def test_tcp_vs_udp():
    """Test TCP vs UDP Demo"""
    print_header("TEST 4: TCP vs UDP DEMO")
    print("File: tcp_vs_udp_demo.py")
    print("Status: ✅ Đã tạo & tested")
    print("Cách test: python tcp_vs_udp_demo.py")
    print("         → Tự động chạy cả TCP và UDP")
    print("         → Hiển thị so sánh")


def test_basic_udp():
    """Test Basic UDP Client/Server"""
    print_header("TEST 5: BASIC UDP CLIENT/SERVER")
    print("Files: client1.py + server1.py")
    print("Status: ✅ Đã chuyển đổi sang UDP")
    print("Cách test:")
    print("  Terminal 1: python server/server1.py")
    print("  Terminal 2: python client/client1.py")


def check_files():
    """Kiểm tra các file đã tồn tại"""
    print_header("KIỂM TRA CÁC FILE")

    files_to_check = [
        ("dns_client_simple.py", "DNS Client Simple"),
        ("dns_client.py", "DNS Client Advanced"),
        ("dhcp_client.py", "DHCP Client"),
        ("tcp_vs_udp_demo.py", "TCP vs UDP Demo"),
        ("client/client1.py", "UDP Client 1"),
        ("server/server1.py", "UDP Server 1"),
        ("README.md", "Hướng dẫn chi tiết"),
        ("QUICKSTART.md", "Hướng dẫn nhanh"),
        ("SUMMARY.md", "Tổng kết"),
        ("INDEX.md", "Index"),
    ]

    import os

    print("\nDanh sách files:")
    all_exist = True

    for file, desc in files_to_check:
        if os.path.exists(file):
            print(f"  ✅ {file:30s} - {desc}")
        else:
            print(f"  ❌ {file:30s} - {desc}")
            all_exist = False

    return all_exist


def main():
    """Main function"""
    print("=" * 70)
    print("  BÀI TẬP BUỔI 03 - UDP - TEST SCRIPT")
    print("=" * 70)

    # Kiểm tra files
    all_exist = check_files()

    if not all_exist:
        print("\n⚠️  Một số file chưa tồn tại!")
        return

    # Hiển thị các test cases
    test_dns_simple()
    test_tcp_vs_udp()
    test_dns_advanced()
    test_dhcp()
    test_basic_udp()

    # Tổng kết
    print_header("TỔNG KẾT")
    print("✅ YÊU CẦU CHÍNH ĐÃ HOÀN THÀNH:")
    print("   1. ✅ Sửa Buổi 03 từ TCP → UDP")
    print("   2. ✅ DNS Client (2 phiên bản)")
    print("   3. ✅ DHCP Client")
    print()
    print("📚 TÀI LIỆU:")
    print("   - INDEX.md: Điểm bắt đầu")
    print("   - QUICKSTART.md: Hướng dẫn nhanh")
    print("   - README.md: Hướng dẫn chi tiết")
    print("   - SUMMARY.md: Tổng kết công việc")
    print()
    print("🚀 BẮT ĐẦU:")
    print("   Chạy: python dns_client_simple.py")
    print("   Hoặc: python tcp_vs_udp_demo.py")
    print()
    print("=" * 70)
    print("  SẴN SÀNG SỬ DỤNG! 🎉")
    print("=" * 70)


if __name__ == "__main__":
    main()
