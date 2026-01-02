import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 3000))

client.send("Hello World".encode())
response = client.recv(1024).decode()
print(response)

client.close()
