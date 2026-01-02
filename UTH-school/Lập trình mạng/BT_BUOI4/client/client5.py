import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 3000))
print("Kết nối thành công! (Gõ 'quit' để thoát)")

while True:
    number = input("Nhập số (0-10): ")
    client.send(number.encode())

    response = client.recv(1024).decode()
    print(response)

    if number.lower() == "quit":
        break

client.close()
