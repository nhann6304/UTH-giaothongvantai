import socket

PASSWORD = "laptrinhmang"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 3000))
server.listen(1)
print("Authenticated Chat Server đang chờ kết nối...")

conn, addr = server.accept()
print(f"Client {addr} đã kết nối")

# Xác thực
password = conn.recv(1024).decode()
if password != PASSWORD:
    conn.send("SAI MẬT MÃ! Kết nối bị từ chối.".encode())
    conn.close()
    server.close()
    print("Client nhập sai mật mã")
else:
    conn.send("XÁC THỰC THÀNH CÔNG! Bắt đầu chat (0 để thoát)".encode())
    print("Client xác thực thành công")

    while True:
        message = conn.recv(1024).decode()

        if message == "0":
            conn.send("Goodbye!".encode())
            break

        print(f"Nhận message: {message}")
        conn.send(f"Server đã nhận message: {message}".encode())

conn.close()
server.close()
