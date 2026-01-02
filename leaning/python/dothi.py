import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 3000))
server.listen(1)
print("Server đang chờ kết nối...")

conn, addr = server.accept()
print(f"Client {addr} đã kết nối")

data = conn.recv(1024).decode()
print(f"Nhận được: {data}")

conn.send(f"Server đã nhận: {data}".encode())
conn.close()
server.close()
