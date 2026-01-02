import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Gửi dữ liệu qua UDP (không cần connect)
client.sendto("Hello World".encode(), ("localhost", 4000))

# Nhận phản hồi
response, server_addr = client.recvfrom(1024)
print(f"Server phản hồi: {response.decode()}")

client.close()
