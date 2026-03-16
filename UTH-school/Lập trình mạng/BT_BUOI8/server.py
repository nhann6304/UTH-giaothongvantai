"""
Chat Server - Máy chủ chat đơn giản sử dụng Socket
Hỗ trợ nhiều client kết nối và chat với nhau
"""

import socket
import threading


class ChatServer:
    def __init__(self, host="localhost", port=5555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []  # Danh sách các client đang kết nối
        self.nicknames = []  # Danh sách nickname của các client

    def broadcast(self, message, sender_socket=None):
        """Gửi tin nhắn đến tất cả client (trừ người gửi)"""
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message)
                except:
                    self.remove_client(client)

    def handle_client(self, client_socket):
        """Xử lý tin nhắn từ một client"""
        while True:
            try:
                message = client_socket.recv(1024)
                if message:
                    self.broadcast(message, client_socket)
                else:
                    self.remove_client(client_socket)
                    break
            except:
                self.remove_client(client_socket)
                break

    def remove_client(self, client_socket):
        """Xóa client khỏi danh sách"""
        if client_socket in self.clients:
            index = self.clients.index(client_socket)
            nickname = self.nicknames[index]

            leave_message = f"\n[HỆ THỐNG] {nickname} đã rời khỏi phòng chat.\n".encode(
                "utf-8"
            )
            self.broadcast(leave_message)

            self.clients.remove(client_socket)
            self.nicknames.remove(nickname)
            client_socket.close()

            print(
                f"[SERVER] {nickname} đã ngắt kết nối. Còn {len(self.clients)} người online."
            )

    def start(self):
        """Khởi động server"""
        self.server.bind((self.host, self.port))
        self.server.listen()

        print("=" * 50)
        print(f"🚀 Chat Server đang chạy tại {self.host}:{self.port}")
        print("=" * 50)
        print("Đang chờ client kết nối...\n")

        while True:
            try:
                client_socket, address = self.server.accept()
                print(f"[SERVER] Kết nối mới từ {address}")

                client_socket.send("NICKNAME".encode("utf-8"))
                nickname = client_socket.recv(1024).decode("utf-8")

                self.clients.append(client_socket)
                self.nicknames.append(nickname)

                print(
                    f"[SERVER] {nickname} đã tham gia. Tổng: {len(self.clients)} người online."
                )

                join_message = (
                    f"\n[HỆ THỐNG] {nickname} đã tham gia phòng chat!\n".encode("utf-8")
                )
                self.broadcast(join_message)

                welcome_message = (
                    f"\n[HỆ THỐNG] Chào mừng {nickname} đến phòng chat!\n".encode(
                        "utf-8"
                    )
                )
                client_socket.send(welcome_message)

                thread = threading.Thread(
                    target=self.handle_client, args=(client_socket,)
                )
                thread.daemon = True
                thread.start()

            except KeyboardInterrupt:
                print("\n[SERVER] Đang tắt server...")
                break
            except Exception as e:
                print(f"[SERVER] Lỗi: {e}")

        self.server.close()


if __name__ == "__main__":
    server = ChatServer()
    server.start()
