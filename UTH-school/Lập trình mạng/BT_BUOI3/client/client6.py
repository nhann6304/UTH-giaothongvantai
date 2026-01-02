import socket
import sys

client = None

try:
    ip = input("Nhập IP server (mặc định localhost): ").strip() or "localhost"
    port_input = input("Nhập Port (mặc định 9000): ").strip()
    port = int(port_input) if port_input else 9000

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(5)  # Timeout 5 giây

    server_addr = (ip, port)

    print(f"→ UDP Client sẵn sàng gửi đến {ip}:{port}")
    print(f"✓ UDP không cần kết nối trước!")
    print("✓ Nhập message (0 để thoát, Ctrl+C để force quit)\n")

    while True:
        try:
            message = input("You: ")

            if not message.strip():
                print("⚠ Không được gửi message rỗng!")
                continue

            client.sendto(message.encode(), server_addr)

            response, addr = client.recvfrom(1024)
            print(f"Server ({addr[0]}:{addr[1]}): {response.decode()}")

            if message == "0":
                break

        except KeyboardInterrupt:
            print("\n\n✗ Đã hủy bằng Ctrl+C")
            break
        except socket.timeout:
            print("\n✗ Timeout: Không nhận được phản hồi từ server")
            retry = input("Thử lại? (y/n): ").lower()
            if retry != "y":
                break

except KeyboardInterrupt:
    print("\n\n✗ Đã hủy trong quá trình thiết lập")
except ValueError:
    print("✗ Lỗi: Port phải là số nguyên!")
except socket.gaierror:
    print("✗ Lỗi: IP không hợp lệ!")
except Exception as e:
    print(f"✗ Lỗi: {e}")
finally:
    if client:
        try:
            client.close()
            print("✓ Đã đóng socket")
        except:
            pass
