import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 3000))
server.listen(1)
print("Chat Server đang chờ kết nối...")

conn, addr = server.accept()
print(f"Client {addr} đã kết nối")

message = conn.recv(1024).decode()
print(f"Nhận message: {message}")

conn.send(f"Server đã nhận message: {message}".encode())
conn.close()
server.close()
