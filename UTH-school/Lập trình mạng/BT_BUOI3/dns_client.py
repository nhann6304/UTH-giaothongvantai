"""
DNS Client - Phân giải tên miền thành địa chỉ IP
Sử dụng giao thức UDP để gửi query đến DNS Server (port 53)
"""

import socket
import struct


class DNSClient:
    def __init__(self, dns_server="8.8.8.8", port=53):
        """
        Khởi tạo DNS Client
        :param dns_server: Địa chỉ DNS server (mặc định: Google DNS)
        :param port: Cổng DNS (mặc định: 53)
        """
        self.dns_server = dns_server
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(5)  # Timeout 5 giây

    def build_dns_query(self, domain):
        """
        Xây dựng DNS query theo chuẩn RFC 1035
        :param domain: Tên miền cần phân giải
        :return: DNS query packet
        """
        # Transaction ID (2 bytes) - random
        transaction_id = struct.pack(">H", 0x1234)

        # Flags (2 bytes)
        # - QR: 0 (query)
        # - Opcode: 0 (standard query)
        # - RD: 1 (recursion desired)
        flags = struct.pack(">H", 0x0100)

        # Questions count (2 bytes)
        questions = struct.pack(">H", 1)

        # Answer RRs, Authority RRs, Additional RRs (6 bytes total)
        answer_rrs = struct.pack(">H", 0)
        authority_rrs = struct.pack(">H", 0)
        additional_rrs = struct.pack(">H", 0)

        # Header (12 bytes)
        header = (
            transaction_id
            + flags
            + questions
            + answer_rrs
            + authority_rrs
            + additional_rrs
        )

        # Question section
        question = b""
        for part in domain.split("."):
            length = len(part)
            question += struct.pack("B", length) + part.encode()
        question += b"\x00"  # Null terminator

        # Type A (1) và Class IN (1)
        question += struct.pack(">H", 1)  # QTYPE: A record
        question += struct.pack(">H", 1)  # QCLASS: IN (Internet)

        return header + question

    def parse_dns_response(self, response):
        """
        Phân tích DNS response
        :param response: DNS response packet
        :return: Danh sách địa chỉ IP
        """
        # Bỏ qua header (12 bytes)
        pos = 12

        # Bỏ qua question section
        while response[pos] != 0:
            pos += response[pos] + 1
        pos += 1  # Null terminator
        pos += 4  # QTYPE và QCLASS

        # Parse answer section
        ip_addresses = []

        try:
            # Đọc các answer records
            while pos < len(response):
                # Kiểm tra pointer
                if response[pos] & 0xC0 == 0xC0:
                    pos += 2  # Bỏ qua pointer
                else:
                    # Bỏ qua name
                    while response[pos] != 0:
                        pos += response[pos] + 1
                    pos += 1

                if pos + 10 > len(response):
                    break

                # Type, Class, TTL
                record_type = struct.unpack(">H", response[pos : pos + 2])[0]
                pos += 8  # Skip Type, Class, TTL

                # Data length
                data_length = struct.unpack(">H", response[pos : pos + 2])[0]
                pos += 2

                # Nếu là A record (type 1) và length = 4
                if record_type == 1 and data_length == 4:
                    ip = ".".join(str(b) for b in response[pos : pos + 4])
                    ip_addresses.append(ip)

                pos += data_length

        except Exception as e:
            print(f"Lỗi khi parse response: {e}")

        return ip_addresses

    def resolve(self, domain):
        """
        Phân giải tên miền thành địa chỉ IP
        :param domain: Tên miền cần phân giải
        :return: Danh sách địa chỉ IP hoặc None nếu lỗi
        """
        try:
            # Tạo DNS query
            query = self.build_dns_query(domain)

            # Gửi query đến DNS server
            self.sock.sendto(query, (self.dns_server, self.port))
            print(f"Đã gửi DNS query cho {domain} đến {self.dns_server}")

            # Nhận response
            response, addr = self.sock.recvfrom(1024)
            print(f"Nhận được response từ {addr}")

            # Parse response
            ip_addresses = self.parse_dns_response(response)

            return ip_addresses if ip_addresses else None

        except socket.timeout:
            print("Timeout: Không nhận được phản hồi từ DNS server")
            return None
        except Exception as e:
            print(f"Lỗi: {e}")
            return None

    def close(self):
        """Đóng socket"""
        self.sock.close()


def main():
    """Chương trình chính"""
    print("=" * 60)
    print("DNS CLIENT - PHÂN GIẢI TÊN MIỀN THÀNH ĐỊA CHỈ IP")
    print("=" * 60)

    # Tạo DNS client
    dns_client = DNSClient()

    print(f"\nSử dụng DNS Server: {dns_client.dns_server}")
    print("Nhập 'quit' để thoát\n")

    while True:
        # Nhập tên miền
        domain = input("Nhập tên miền cần phân giải: ").strip()

        if domain.lower() == "quit":
            print("Tạm biệt!")
            break

        if not domain:
            print("Vui lòng nhập tên miền hợp lệ!\n")
            continue

        print(f"\n🔍 Đang phân giải {domain}...")
        print("-" * 60)

        # Phân giải tên miền
        ip_addresses = dns_client.resolve(domain)

        if ip_addresses:
            print(f"✅ Kết quả:")
            for i, ip in enumerate(ip_addresses, 1):
                print(f"   {i}. {ip}")
        else:
            print("❌ Không thể phân giải tên miền!")

        print("-" * 60)
        print()

    # Đóng kết nối
    dns_client.close()


if __name__ == "__main__":
    main()
