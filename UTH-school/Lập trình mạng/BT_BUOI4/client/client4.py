import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 3000))
print("Kết nối thành công! (Nhấn 0 để thoát)")

while True:
    message = input("You: ")
    client.send(message.encode())

    response = client.recv(1024).decode()
    print(response)

    if message == "0":
        break

client.close()
