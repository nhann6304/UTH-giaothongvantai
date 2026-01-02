import socket
import sys

client = None

try:
    ip = input("Nhập IP server (mặc định localhost): ").strip() or "localhost"
    port_input = input("Nhập Port (mặc định 9000): ").strip()
    port = int(port_input) if port_input else 9000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)  # Timeout 5 giây

    print(f"→ Đang kết nối đến {ip}:{port}...")
    client.connect((ip, port))
    client.settimeout(None)  # Bỏ timeout

    print(f"✓ Kết nối thành công!")
    print("✓ Nhập message (0 để thoát, Ctrl+C để force quit)\n")

    while True:
        try:
            message = input("You: ")

            if not message.strip():
                print("⚠ Không được gửi message rỗng!")
                continue

            client.send(message.encode())

            response = client.recv(1024).decode()
            print(f"Server: {response}")

            if message == "0":
                break

        except KeyboardInterrupt:
            print("\n\n✗ Đã hủy bằng Ctrl+C")
            break
        except BrokenPipeError:
            print("\n✗ Server đã đóng kết nối")
            break
        except ConnectionResetError:
            print("\n✗ Server đã reset kết nối")
            break

except KeyboardInterrupt:
    print("\n\n✗ Đã hủy trong quá trình kết nối")
except socket.timeout:
    print("✗ Lỗi: Không thể kết nối đến server (timeout 5s)")
    print("  Kiểm tra server đã chạy chưa!")
except ConnectionRefusedError:
    print("✗ Lỗi: Server từ chối kết nối")
    print("  Server chưa chạy hoặc sai IP/Port!")
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
            print("✓ Đã đóng kết nối")
        except:
            pass
