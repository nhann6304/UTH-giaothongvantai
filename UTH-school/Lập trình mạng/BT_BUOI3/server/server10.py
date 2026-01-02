import socket
import sys


def main():
    client = None
    try:
        # Nhập IP và Port
        try:
            ip = input("Nhập IP server (mặc định localhost): ").strip() or "localhost"
            port_input = input("Nhập Port (mặc định 3000): ").strip()
            port = int(port_input) if port_input else 3000
        except ValueError:
            print("Lỗi: Port phải là số nguyên!")
            return

        # Kết nối đến server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(10)  # Timeout 10 giây

        print(f"Đang kết nối đến {ip}:{port}...")
        client.connect((ip, port))
        print("Kết nối thành công! (Nhấn 0 để thoát)\n")

        client.settimeout(None)  # Bỏ timeout sau khi kết nối

        while True:
            try:
                message = input("You: ")

                if not message.strip():
                    print("Lỗi: Không được gửi message rỗng!")
                    continue

                client.send(message.encode())

                try:
                    response = client.recv(1024).decode()
                    if not response:
                        print("Server đã ngắt kết nối")
                        break
                    print(f"Server: {response}")

                    if message == "0":
                        break

                except socket.timeout:
                    print("Lỗi: Không nhận được phản hồi từ server (timeout)")
                    break

            except KeyboardInterrupt:
                print("\n\nNgắt kết nối...")
                break
            except Exception as e:
                print(f"Lỗi gửi/nhận message: {str(e)}")
                break

    except socket.timeout:
        print("Lỗi: Không thể kết nối đến server (timeout)")
    except ConnectionRefusedError:
        print("Lỗi: Server từ chối kết nối. Kiểm tra server đã chạy chưa!")
    except socket.gaierror:
        print("Lỗi: Không thể phân giải địa chỉ IP")
    except Exception as e:
        print(f"Lỗi kết nối: {str(e)}")
    finally:
        if client:
            client.close()
            print("Đã đóng kết nối")


if __name__ == "__main__":
    main()
