import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 3000))
print("UDP Chat Server đang chờ tin nhắn...")

client_addr = None

while True:
    message, addr = server.recvfrom(1024)
    message = message.decode()
    client_addr = addr

    if message == "0":
        server.sendto("Goodbye!".encode(), client_addr)
        break

    print(f"Nhận từ {client_addr}: {message}")
    server.sendto(f"Server đã nhận message: {message}".encode(), client_addr)

server.close()
