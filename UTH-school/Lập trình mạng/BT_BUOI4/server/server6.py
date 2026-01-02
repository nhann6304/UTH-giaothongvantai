import socket
import sys

try:
    ip = input("Nhập IP (mặc định localhost): ").strip() or "localhost"
    port = int(input("Nhập Port (mặc định 9000): ").strip() or 9000)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen(5)
    print(f"✓ Server đang chạy tại {ip}:{port}")
    print("✓ Nhấn Ctrl+C để dừng server\n")

    while True:
        try:
            conn, addr = server.accept()
            print(f"→ Client {addr} đã kết nối")

            while True:
                try:
                    message = conn.recv(1024).decode()

                    # Kiểm tra nếu client ngắt kết nối
                    if not message:
                        print(f"✗ Client {addr} đã ngắt kết nối")
                        break

                    if message == "0":
                        conn.send("Goodbye!".encode())
                        print(f"✓ Client {addr} đã thoát")
                        break

                    print(f"← Nhận: {message}")
                    conn.send(f"Server đã nhận: {message}".encode())

                except ConnectionAbortedError:
                    print(f"✗ Client {addr} đã ngắt kết nối đột ngột (Ctrl+C)")
                    break
                except ConnectionResetError:
                    print(f"✗ Client {addr} đã reset kết nối")
                    break
                except Exception as e:
                    print(f"✗ Lỗi nhận dữ liệu: {e}")
                    break

            conn.close()
            print(f"✓ Đã đóng kết nối với {addr}\n")

        except KeyboardInterrupt:
            print("\n\n✗ Nhận Ctrl+C, đang dừng server...")
            break

except KeyboardInterrupt:
    print("\n\n✗ Server đang dừng...")
except ValueError:
    print("✗ Lỗi: Port phải là số nguyên!")
except OSError as e:
    if e.errno == 10048:
        print(f"✗ Lỗi: Port {port} đang được sử dụng!")
        print("  Hãy thử port khác hoặc tắt chương trình đang dùng port này")
    else:
        print(f"✗ Lỗi hệ thống: {e}")
except Exception as e:
    print(f"✗ Lỗi không xác định: {e}")
finally:
    try:
        server.close()
        print("✓ Server đã đóng")
    except:
        pass
