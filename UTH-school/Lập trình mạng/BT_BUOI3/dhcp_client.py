"""
DHCP Client - Xin cấp địa chỉ IP từ DHCP Server
Sử dụng giao thức UDP (port 67 cho server, port 68 cho client)
"""

import socket
import struct
import random
import uuid


class DHCPClient:
    def __init__(self):
        """Khởi tạo DHCP Client"""
        self.server_port = 67
        self.client_port = 68
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.settimeout(5)

        # Tạo transaction ID ngẫu nhiên
        self.transaction_id = random.randint(0, 0xFFFFFFFF)

        # Lấy MAC address của máy
        self.mac_address = self.get_mac_address()

    def get_mac_address(self):
        """
        Lấy MAC address của máy
        :return: MAC address dạng bytes (6 bytes)
        """
        # Lấy MAC address từ uuid
        mac = uuid.getnode()
        mac_bytes = mac.to_bytes(6, "big")
        return mac_bytes

    def build_dhcp_discover(self):
        """
        Xây dựng DHCP DISCOVER packet
        :return: DHCP DISCOVER packet
        """
        # Message type: BOOTREQUEST (1)
        message_type = struct.pack("B", 1)

        # Hardware type: Ethernet (1)
        hardware_type = struct.pack("B", 1)

        # Hardware address length: 6 bytes
        hw_addr_len = struct.pack("B", 6)

        # Hops: 0
        hops = struct.pack("B", 0)

        # Transaction ID (4 bytes)
        transaction_id = struct.pack(">I", self.transaction_id)

        # Seconds elapsed: 0
        secs = struct.pack(">H", 0)

        # Flags: 0x8000 (Broadcast)
        flags = struct.pack(">H", 0x8000)

        # Client IP address: 0.0.0.0
        ciaddr = struct.pack("!4B", 0, 0, 0, 0)

        # Your IP address: 0.0.0.0
        yiaddr = struct.pack("!4B", 0, 0, 0, 0)

        # Server IP address: 0.0.0.0
        siaddr = struct.pack("!4B", 0, 0, 0, 0)

        # Gateway IP address: 0.0.0.0
        giaddr = struct.pack("!4B", 0, 0, 0, 0)

        # Client hardware address (MAC) + padding
        chaddr = self.mac_address + b"\x00" * 10

        # Server host name (64 bytes)
        sname = b"\x00" * 64

        # Boot file name (128 bytes)
        file = b"\x00" * 128

        # Magic cookie: 0x63825363
        magic_cookie = struct.pack("!4B", 0x63, 0x82, 0x53, 0x63)

        # DHCP Options
        options = b""

        # Option 53: DHCP Message Type = DISCOVER (1)
        options += struct.pack("BBB", 53, 1, 1)

        # Option 55: Parameter Request List
        # 1=Subnet Mask, 3=Router, 6=DNS, 15=Domain Name
        options += struct.pack("BBBBBB", 55, 4, 1, 3, 6, 15)

        # Option 255: End
        options += struct.pack("B", 255)

        # Tạo packet hoàn chỉnh
        packet = (
            message_type
            + hardware_type
            + hw_addr_len
            + hops
            + transaction_id
            + secs
            + flags
            + ciaddr
            + yiaddr
            + siaddr
            + giaddr
            + chaddr
            + sname
            + file
            + magic_cookie
            + options
        )

        return packet

    def parse_dhcp_offer(self, packet):
        """
        Phân tích DHCP OFFER packet
        :param packet: DHCP OFFER packet
        :return: Dictionary chứa thông tin IP được offer
        """
        try:
            # Kiểm tra transaction ID
            trans_id = struct.unpack(">I", packet[4:8])[0]
            if trans_id != self.transaction_id:
                print("Transaction ID không khớp!")
                return None

            # Your IP Address (offset 16-20)
            offered_ip = ".".join(str(b) for b in packet[16:20])

            # Server IP Address (offset 20-24)
            server_ip = ".".join(str(b) for b in packet[20:24])

            # Parse options (bắt đầu từ byte 240)
            pos = 240

            dhcp_info = {
                "offered_ip": offered_ip,
                "server_ip": server_ip,
                "subnet_mask": None,
                "router": None,
                "dns": [],
                "lease_time": None,
            }

            while pos < len(packet):
                option_code = packet[pos]

                if option_code == 255:  # End option
                    break

                if option_code == 0:  # Pad option
                    pos += 1
                    continue

                option_len = packet[pos + 1]
                option_data = packet[pos + 2 : pos + 2 + option_len]

                # Subnet Mask (option 1)
                if option_code == 1:
                    dhcp_info["subnet_mask"] = ".".join(str(b) for b in option_data)

                # Router (option 3)
                elif option_code == 3:
                    dhcp_info["router"] = ".".join(str(b) for b in option_data[:4])

                # DNS Server (option 6)
                elif option_code == 6:
                    for i in range(0, len(option_data), 4):
                        dns = ".".join(str(b) for b in option_data[i : i + 4])
                        dhcp_info["dns"].append(dns)

                # Lease Time (option 51)
                elif option_code == 51:
                    dhcp_info["lease_time"] = struct.unpack(">I", option_data)[0]

                # DHCP Message Type (option 53)
                elif option_code == 53:
                    msg_type = option_data[0]
                    if msg_type != 2:  # 2 = OFFER
                        print(f"Nhận được message type {msg_type}, không phải OFFER")
                        return None

                pos += 2 + option_len

            return dhcp_info

        except Exception as e:
            print(f"Lỗi khi parse DHCP OFFER: {e}")
            return None

    def discover(self):
        """
        Gửi DHCP DISCOVER và nhận DHCP OFFER
        :return: Thông tin IP được offer hoặc None
        """
        try:
            # Bind socket
            try:
                self.sock.bind(("", self.client_port))
            except OSError as e:
                print(f"⚠️  Không thể bind port {self.client_port}: {e}")
                print("💡 Chạy với quyền Administrator hoặc sử dụng port khác")
                return None

            # Tạo DHCP DISCOVER packet
            discover_packet = self.build_dhcp_discover()

            # Gửi broadcast
            print(f"📤 Gửi DHCP DISCOVER...")
            print(f"   Transaction ID: 0x{self.transaction_id:08X}")
            print(f"   MAC Address: {':'.join(f'{b:02X}' for b in self.mac_address)}")

            self.sock.sendto(discover_packet, ("255.255.255.255", self.server_port))

            # Nhận DHCP OFFER
            print(f"\n⏳ Đang chờ DHCP OFFER...")

            try:
                data, addr = self.sock.recvfrom(1024)
                print(f"📥 Nhận được phản hồi từ {addr[0]}:{addr[1]}")

                # Parse DHCP OFFER
                dhcp_info = self.parse_dhcp_offer(data)

                return dhcp_info

            except socket.timeout:
                print("⏱️  Timeout: Không nhận được DHCP OFFER")
                print("💡 Đảm bảo có DHCP server trong mạng hoặc chạy DHCP simulator")
                return None

        except Exception as e:
            print(f"❌ Lỗi: {e}")
            return None

    def close(self):
        """Đóng socket"""
        self.sock.close()


def main():
    """Chương trình chính"""
    print("=" * 70)
    print("DHCP CLIENT - XIN CẤP ĐỊA CHỈ IP")
    print("=" * 70)

    print("\n⚠️  LƯU Ý:")
    print("- DHCP Client cần quyền Administrator để bind port 68")
    print("- Cần có DHCP Server trong mạng để nhận IP")
    print("- Hoặc sử dụng DHCP simulator để test\n")

    input("Nhấn Enter để bắt đầu DHCP Discovery...")

    # Tạo DHCP client
    dhcp_client = DHCPClient()

    print("\n" + "-" * 70)

    # Thực hiện DHCP Discovery
    dhcp_info = dhcp_client.discover()

    print("-" * 70)

    if dhcp_info:
        print("\n✅ THÀNH CÔNG! Nhận được DHCP OFFER:")
        print(f"\n   🌐 Địa chỉ IP được cấp: {dhcp_info['offered_ip']}")
        print(f"   🖥️  DHCP Server: {dhcp_info['server_ip']}")

        if dhcp_info["subnet_mask"]:
            print(f"   📡 Subnet Mask: {dhcp_info['subnet_mask']}")

        if dhcp_info["router"]:
            print(f"   🚪 Default Gateway: {dhcp_info['router']}")

        if dhcp_info["dns"]:
            print(f"   🔍 DNS Servers: {', '.join(dhcp_info['dns'])}")

        if dhcp_info["lease_time"]:
            lease_hours = dhcp_info["lease_time"] / 3600
            print(
                f"   ⏰ Lease Time: {dhcp_info['lease_time']}s ({lease_hours:.1f} giờ)"
            )

        print("\n💡 Lưu ý: Đây chỉ là OFFER, cần gửi REQUEST để xác nhận nhận IP")
    else:
        print("\n❌ KHÔNG THÀNH CÔNG!")
        print("\n📝 Các nguyên nhân có thể:")
        print("   1. Không có DHCP server trong mạng")
        print("   2. Cần quyền Administrator")
        print("   3. Port 68 đang bị sử dụng")
        print("   4. Firewall chặn gói tin DHCP")

    print("\n" + "=" * 70)

    # Đóng kết nối
    dhcp_client.close()


if __name__ == "__main__":
    main()
