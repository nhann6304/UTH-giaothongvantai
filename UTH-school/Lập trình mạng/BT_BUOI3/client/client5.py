import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("localhost", 3000)
print("Kết nối thành công! (Gõ 'quit' để thoát)")

while True:
    number = input("Nhập số (0-10): ")
    client.sendto(number.encode(), server_addr)

    response, addr = client.recvfrom(1024)
    print(response.decode())

    if number.lower() == "quit":
        break

client.close()
