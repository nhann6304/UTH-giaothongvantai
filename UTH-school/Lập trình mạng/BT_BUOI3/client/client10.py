import socket
import sys


def handle_client(conn, addr):
    try:
        print(f"Client {addr} đã kết nối")

        while True:
            try:
                message = conn.recv(1024).decode()

                if not message:  # Client ngắt kết nối
                    print(f"Client {addr} đã ngắt kết nối")
                    break

                if message == "0":
                    conn.send("Goodbye!".encode())
                    break

                print(f"Nhận message: {message}")
                conn.send(f"Server đã nhận message: {message}".encode())

            except UnicodeDecodeError:
                error_msg = "Lỗi: Không thể giải mã dữ liệu"
                print(error_msg)
                conn.send(error_msg.encode())
            except Exception as e:
                error_msg = f"Lỗi xử lý message: {str(e)}"
                print(error_msg)
                conn.send(error_msg.encode())

    except Exception as e:
        print(f"Lỗi kết nối: {str(e)}")
    finally:
        conn.close()
        print(f"Đã đóng kết nối với {addr}")


def main():
    server = None
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("localhost", 3000))
        server.listen(5)
        print("Server đang chạy trên localhost:3000")
        print("Nhấn Ctrl+C để dừng server\n")

        while True:
            try:
                conn, addr = server.accept()
                handle_client(conn, addr)
            except KeyboardInterrupt:
                print("\n\nServer đang dừng...")
                break
            except Exception as e:
                print(f"Lỗi chấp nhận kết nối: {str(e)}")

    except OSError as e:
        print(f"Lỗi khởi tạo server: {str(e)}")
        print("Port có thể đang được sử dụng!")
    except Exception as e:
        print(f"Lỗi không xác định: {str(e)}")
    finally:
        if server:
            server.close()
            print("Server đã đóng")


if __name__ == "__main__":
    main()
