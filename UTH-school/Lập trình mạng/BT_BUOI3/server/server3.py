import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 3000))
print("UDP Chat Server đang chờ tin nhắn...")

message, client_addr = server.recvfrom(1024)
print(f"Nhận từ {client_addr}: {message.decode()}")

server.sendto(f"Server đã nhận message: {message.decode()}".encode(), client_addr)

server.close()
