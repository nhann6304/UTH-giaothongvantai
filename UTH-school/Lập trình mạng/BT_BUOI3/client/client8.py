import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 3000))

password = input("Nhập mật mã: ")
client.send(password.encode())

response = client.recv(1024).decode()
print(response)

if "SAI MẬT MÃ" in response:
    client.close()
else:
    while True:
        message = input("You: ")
        client.send(message.encode())

        response = client.recv(1024).decode()
        print(response)

        if message == "0":
            break

    client.close()
