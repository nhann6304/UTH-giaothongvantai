import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Nhập message: ")
client.sendto(message.encode(), ("localhost", 3000))

response, server_addr = client.recvfrom(1024)
print(f"Server phản hồi: {response.decode()}")

client.close()
