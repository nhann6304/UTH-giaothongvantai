import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("localhost", 3000)
print("Kết nối UDP thành công! (Nhấn 0 để thoát)")

while True:
    message = input("You: ")
    client.sendto(message.encode(), server_addr)

    response, addr = client.recvfrom(1024)
    print(f"Server: {response.decode()}")

    if message == "0":
        break

client.close()
