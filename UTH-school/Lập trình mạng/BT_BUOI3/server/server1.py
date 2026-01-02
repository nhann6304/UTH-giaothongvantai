import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 4000))
print("UDP Server đang chờ tin nhắn...")

# Nhận dữ liệu từ client
data, client_addr = server.recvfrom(1024)
print(f"Nhận từ {client_addr}: {data.decode()}")

# Gửi phản hồi
server.sendto(f"Server đã nhận: {data.decode()}".encode(), client_addr)

server.close()
