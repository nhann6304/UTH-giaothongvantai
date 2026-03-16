"""
Chat Client - Ứng dụng chat client sử dụng Socket
Kết nối đến server và chat với các client khác
"""

import socket
import threading
import os


class ChatClient:
    def __init__(self, host="localhost", port=5555):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nickname = ""

    def receive_messages(self):
        """Nhận tin nhắn từ server"""
        while True:
            try:
                message = self.client.recv(1024).decode("utf-8")

                if message == "NICKNAME":
                    self.client.send(self.nickname.encode("utf-8"))
                else:
                    print(message)
            except:
                print("\n[LỖI] Mất kết nối với server!")
                self.client.close()
                break

    def send_messages(self):
        """Gửi tin nhắn đến server"""
        while True:
            try:
                message = input()
                if message.lower() == "/quit":
                    print("\n[HỆ THỐNG] Đang thoát...")
                    self.client.close()
                    os._exit(0)
                else:
                    full_message = f"[{self.nickname}] {message}"
                    self.client.send(full_message.encode("utf-8"))
            except:
                break

    def start(self):
        """Khởi động client"""
        try:
            self.client.connect((self.host, self.port))

            print("=" * 50)
            print("🎮 CHAT APPLICATION")
            print("=" * 50)
            self.nickname = input("Nhập nickname của bạn: ").strip()

            if not self.nickname:
                self.nickname = "Anonymous"

            print(f"\n✅ Đã kết nối đến server!")
            print(f"📝 Nickname: {self.nickname}")
            print("-" * 50)
            print("Gõ tin nhắn và Enter để gửi")
            print("Gõ '/quit' để thoát")
            print("-" * 50)
            print()

            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()

            self.send_messages()

        except ConnectionRefusedError:
            print("\n[LỖI] Không thể kết nối đến server!")
            print("Hãy chắc chắn server đang chạy.")
        except Exception as e:
            print(f"\n[LỖI] {e}")
        finally:
            self.client.close()


if __name__ == "__main__":
    client = ChatClient()
    client.start()
