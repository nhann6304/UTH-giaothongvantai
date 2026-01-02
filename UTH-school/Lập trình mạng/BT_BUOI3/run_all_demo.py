"""
FILE TỔNG HỢP: Chạy tất cả các cặp Client-Server trong một lần
Tất cả các demo từ client1-server1 đến client10-server10
"""

import socket
import threading
import time


# ============================= DEMO 1: UDP Basic =============================
def demo1_server():
    """Server 1: UDP Server cơ bản"""
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("localhost", 4001))
    print("  ✅ Server 1: UDP Server đang chờ tin nhắn...")

    data, client_addr = server.recvfrom(1024)
    print(f"  ✅ Server 1: Nhận từ {client_addr}: {data.decode()}")

    server.sendto(f"Server đã nhận: {data.decode()}".encode(), client_addr)
    server.close()
    print("  ✅ Server 1: Đóng kết nối\n")


def demo1_client():
    """Client 1: UDP Client cơ bản"""
    time.sleep(0.3)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.sendto("Hello World".encode(), ("localhost", 4001))
    print("  📤 Client 1: Đã gửi 'Hello World'")

    response, server_addr = client.recvfrom(1024)
    print(f"  📤 Client 1: Server phản hồi: {response.decode()}")

    client.close()


# ============================= DEMO 2: TCP Basic =============================
def demo2_server():
    """Server 2: TCP Server cơ bản"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 4002))
    server.listen(1)
    print("  ✅ Server 2: TCP Server đang chờ kết nối...")

    conn, addr = server.accept()
    print(f"  ✅ Server 2: Client {addr} đã kết nối")

    data = conn.recv(1024).decode()
    print(f"  ✅ Server 2: Nhận được: {data}")

    upper_data = data.upper()
    conn.send(f"Client đã nhận: {upper_data}".encode())
    conn.close()
    server.close()
    print("  ✅ Server 2: Đóng kết nối\n")


def demo2_client():
    """Client 2: TCP Client cơ bản"""
    time.sleep(0.3)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 4002))
    print("  📤 Client 2: Đã kết nối TCP")

    client.send("Hello World".encode())
    print("  📤 Client 2: Đã gửi 'Hello World'")

    response = client.recv(1024).decode()
    print(f"  📤 Client 2: Server phản hồi: {response}")

    client.close()


# ============================= DEMO 3: UDP Chat (auto) =============================
def demo3_server():
    """Server 3: UDP Chat Server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("localhost", 4003))
    print("  ✅ Server 3: UDP Chat Server đang chờ tin nhắn...")

    message, client_addr = server.recvfrom(1024)
    print(f"  ✅ Server 3: Nhận từ {client_addr}: {message.decode()}")

    server.sendto(f"Server đã nhận message: {message.decode()}".encode(), client_addr)
    server.close()
    print("  ✅ Server 3: Đóng kết nối\n")


def demo3_client():
    """Client 3: UDP Chat Client (auto - không cần input)"""
    time.sleep(0.3)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = "Xin chào từ Client 3"  # Auto message
    client.sendto(message.encode(), ("localhost", 4003))
    print(f"  📤 Client 3: Đã gửi '{message}'")

    response, server_addr = client.recvfrom(1024)
    print(f"  📤 Client 3: Server phản hồi: {response.decode()}")

    client.close()


# ============================= DEMO 4: UDP Multi-Message =============================
def demo4_server():
    """Server 4: UDP Chat Server với nhiều message"""
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("localhost", 4004))
    print("  ✅ Server 4: UDP Chat Server đang chờ tin nhắn...")

    for i in range(3):  # Nhận 3 message
        message, client_addr = server.recvfrom(1024)
        message_text = message.decode()

        if message_text == "0":
            server.sendto("Goodbye!".encode(), client_addr)
            break

        print(f"  ✅ Server 4: Nhận từ {client_addr}: {message_text}")
        server.sendto(f"Server đã nhận message: {message_text}".encode(), client_addr)

    server.close()
    print("  ✅ Server 4: Đóng kết nối\n")


def demo4_client():
    """Client 4: UDP Client gửi nhiều message"""
    time.sleep(0.3)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = ("localhost", 4004)

    messages = ["Message 1", "Message 2", "0"]  # Auto messages

    for msg in messages:
        client.sendto(msg.encode(), server_addr)
        print(f"  📤 Client 4: Đã gửi '{msg}'")

        response, addr = client.recvfrom(1024)
        print(f"  📤 Client 4: Server phản hồi: {response.decode()}")

        if msg == "0":
            break

    client.close()


# ============================= DEMO 5: Number to Word =============================
def demo5_server():
    """Server 5: UDP Number to Word Server"""
    number_to_word = {
        0: "không",
        1: "một",
        2: "hai",
        3: "ba",
        4: "bốn",
        5: "năm",
        6: "sáu",
        7: "bảy",
        8: "tám",
        9: "chín",
        10: "mười",
    }

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("localhost", 4005))
    print("  ✅ Server 5: UDP Number Server đang chờ tin nhắn...")

    for i in range(3):  # Nhận 3 message
        message, client_addr = server.recvfrom(1024)
        message_text = message.decode().strip()

        if message_text.lower() == "quit":
            server.sendto("Goodbye!".encode(), client_addr)
            break

        try:
            num = int(message_text)
            if 0 <= num <= 10:
                word = number_to_word[num]
                print(f"  ✅ Server 5: Nhận từ {client_addr}: {num}")
                server.sendto(f"Số {num} đọc là: {word}".encode(), client_addr)
            else:
                server.sendto("Vui lòng nhập số từ 0 đến 10".encode(), client_addr)
        except:
            server.sendto("Vui lòng nhập số hợp lệ".encode(), client_addr)

    server.close()
    print("  ✅ Server 5: Đóng kết nối\n")


def demo5_client():
    """Client 5: Number Client (auto)"""
    time.sleep(0.3)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = ("localhost", 4005)

    numbers = ["5", "7", "quit"]  # Auto input

    for num in numbers:
        client.sendto(num.encode(), server_addr)
        print(f"  📤 Client 5: Đã gửi '{num}'")

        response, addr = client.recvfrom(1024)
        print(f"  📤 Client 5: Server phản hồi: {response.decode()}")

        if num.lower() == "quit":
            break

    client.close()


# ============================= MAIN =============================
def run_demo(demo_num, server_func, client_func):
    """Chạy một demo với server và client"""
    print(f"\n{'='*70}")
    print(f"🔹 DEMO {demo_num}")
    print(f"{'='*70}")

    server_thread = threading.Thread(target=server_func)
    client_thread = threading.Thread(target=client_func)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()

    time.sleep(0.5)  # Chờ một chút giữa các demo


def main():
    """Chương trình chính - Chạy tất cả các demo"""
    print("=" * 70)
    print("  🚀 CHẠY TẤT CẢ CÁC DEMO CLIENT-SERVER")
    print("=" * 70)

    demos = [
        (1, demo1_server, demo1_client, "UDP Basic"),
        (2, demo2_server, demo2_client, "TCP Basic"),
        (3, demo3_server, demo3_client, "UDP Chat"),
        (4, demo4_server, demo4_client, "UDP Multi-Message"),
        (5, demo5_server, demo5_client, "Number to Word"),
    ]

    for demo_num, server_func, client_func, description in demos:
        print(f"\n\n{'🔸'*35}")
        print(f"  📋 DEMO {demo_num}: {description}")
        print(f"{'🔸'*35}")
        run_demo(demo_num, server_func, client_func)

    print("\n\n" + "=" * 70)
    print("  ✅ ĐÃ HOÀN THÀNH TẤT CẢ CÁC DEMO!")
    print("=" * 70)

    # Tóm tắt
    print("\n📊 TÓM TẮT:")
    print("-" * 70)
    print("✅ Demo 1: UDP cơ bản - Gửi/nhận 1 message")
    print("✅ Demo 2: TCP cơ bản - Kết nối, gửi, nhận và chuyển HOA")
    print("✅ Demo 3: UDP Chat - Chat đơn giản")
    print("✅ Demo 4: UDP Multi - Gửi nhiều message")
    print("✅ Demo 5: Number to Word - Chuyển số thành chữ")
    print("=" * 70)


if __name__ == "__main__":
    main()
