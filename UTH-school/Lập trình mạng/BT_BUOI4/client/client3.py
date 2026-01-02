import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 3000))

message = input("Nhập message: ")
client.send(message.encode())

response = client.recv(1024).decode()
print(response)

client.close()
