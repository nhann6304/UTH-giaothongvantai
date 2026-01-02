"""
So sánh TCP vs UDP - Demo trực quan
File này chạy cả TCP và UDP server/client để so sánh
"""

import socket
import threading
import time


# ============== TCP ==============
def tcp_server():
    """TCP Server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen(1)
    print("✅ TCP Server đang chờ kết nối trên port 5000...")

    conn, addr = server.accept()
    print(f"✅ TCP: Client {addr} đã kết nối")

    data = conn.recv(1024).decode()
    print(f"✅ TCP: Nhận được '{data}'")

    conn.send(f"TCP Server đã nhận: {data}".encode())
    print("✅ TCP: Đã gửi phản hồi")

    conn.close()
    server.close()
    print("✅ TCP: Đóng kết nối\n")


def tcp_client():
    """TCP Client"""
    time.sleep(0.5)  # Đợi server khởi động

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("📤 TCP Client: Đang kết nối...")

    client.connect(("localhost", 5000))
    print("📤 TCP Client: Đã kết nối")

    client.send("Hello TCP".encode())
    print("📤 TCP Client: Đã gửi dữ liệu")

    response = client.recv(1024).decode()
    print(f"📤 TCP Client: Nhận phản hồi '{response}'")

    client.close()
    print("📤 TCP Client: Đóng kết nối\n")


# ============== UDP ==============
def udp_server():
    """UDP Server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("localhost", 6000))
    print("✅ UDP Server đang chờ tin nhắn trên port 6000...")

    data, client_addr = server.recvfrom(1024)
    print(f"✅ UDP: Nhận từ {client_addr}: '{data.decode()}'")

    server.sendto(f"UDP Server đã nhận: {data.decode()}".encode(), client_addr)
    print("✅ UDP: Đã gửi phản hồi")

    server.close()
    print("✅ UDP: Đóng socket\n")


def udp_client():
    """UDP Client"""
    time.sleep(0.5)  # Đợi server khởi động

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("📤 UDP Client: Sẵn sàng gửi")

    client.sendto("Hello UDP".encode(), ("localhost", 6000))
    print("📤 UDP Client: Đã gửi dữ liệu (không cần connect)")

    response, server_addr = client.recvfrom(1024)
    print(f"📤 UDP Client: Nhận phản hồi từ {server_addr}: '{response.decode()}'")

    client.close()
    print("📤 UDP Client: Đóng socket\n")


def main():
    """Chương trình chính"""
    print("=" * 70)
    print("SO SÁNH TCP vs UDP")
    print("=" * 70)

    # Test TCP
    print("\n🔵 TEST TCP (SOCK_STREAM)")
    print("-" * 70)

    tcp_server_thread = threading.Thread(target=tcp_server)
    tcp_client_thread = threading.Thread(target=tcp_client)

    tcp_server_thread.start()
    tcp_client_thread.start()

    tcp_server_thread.join()
    tcp_client_thread.join()

    # Test UDP
    print("🟢 TEST UDP (SOCK_DGRAM)")
    print("-" * 70)

    udp_server_thread = threading.Thread(target=udp_server)
    udp_client_thread = threading.Thread(target=udp_client)

    udp_server_thread.start()
    udp_client_thread.start()

    udp_server_thread.join()
    udp_client_thread.join()

    # So sánh
    print("=" * 70)
    print("📊 SO SÁNH:")
    print("-" * 70)
    print("TCP (SOCK_STREAM):")
    print("  ✅ Cần connect() trước khi gửi")
    print("  ✅ Cần accept() để chấp nhận kết nối")
    print("  ✅ Đảm bảo dữ liệu đến đích")
    print("  ✅ send() / recv() sau khi kết nối")
    print("  ❌ Chậm hơn (do overhead của kết nối)")
    print()
    print("UDP (SOCK_DGRAM):")
    print("  ✅ KHÔNG cần connect()")
    print("  ✅ KHÔNG cần accept()")
    print("  ✅ Nhanh hơn (không overhead)")
    print("  ✅ sendto() / recvfrom() trực tiếp")
    print("  ❌ KHÔNG đảm bảo dữ liệu đến đích")
    print("=" * 70)


if __name__ == "__main__":
    main()
