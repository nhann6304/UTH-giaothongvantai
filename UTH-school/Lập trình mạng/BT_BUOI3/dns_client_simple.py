"""
DNS Client Đơn Giản - Sử dụng thư viện socket có sẵn
Đây là phiên bản đơn giản hơn, dễ hiểu hơn cho người mới
"""

import socket


def dns_lookup_simple(domain):
    """
    Phân giải tên miền sử dụng hàm có sẵn của Python
    :param domain: Tên miền cần phân giải
    """
    try:
        print(f"🔍 Đang phân giải {domain}...")

        # Sử dụng socket.gethostbyname() - cách đơn giản nhất
        ip_address = socket.gethostbyname(domain)
        print(f"✅ Kết quả: {domain} → {ip_address}")

        # Hoặc dùng socket.getaddrinfo() - chi tiết hơn
        print(f"\n📋 Thông tin chi tiết:")
        addr_info = socket.getaddrinfo(domain, None)

        for i, info in enumerate(addr_info, 1):
            family, socktype, proto, canonname, sockaddr = info
            ip = sockaddr[0]

            family_name = "IPv4" if family == socket.AF_INET else "IPv6"
            socktype_name = "TCP" if socktype == socket.SOCK_STREAM else "UDP"

            print(f"   {i}. {ip} ({family_name}, {socktype_name})")

        return True

    except socket.gaierror as e:
        print(f"❌ Lỗi: Không thể phân giải tên miền - {e}")
        return False
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False


def main():
    """Chương trình chính"""
    print("=" * 60)
    print("DNS CLIENT ĐỎN GIẢN - PHÂN GIẢI TÊN MIỀN")
    print("=" * 60)
    print("\n💡 Phiên bản này dùng socket.gethostbyname() có sẵn")
    print("   Để xem implementation thực tế, dùng dns_client.py\n")
    print("Nhập 'quit' để thoát\n")

    while True:
        domain = input("Nhập tên miền: ").strip()

        if domain.lower() == "quit":
            print("Tạm biệt!")
            break

        if not domain:
            print("⚠️  Vui lòng nhập tên miền hợp lệ!\n")
            continue

        print("-" * 60)
        dns_lookup_simple(domain)
        print("-" * 60)
        print()


if __name__ == "__main__":
    main()
