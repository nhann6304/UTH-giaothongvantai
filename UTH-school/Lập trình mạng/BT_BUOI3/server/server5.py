import socket

number_to_word = {
    0: "không",
    1: "một",
    2: "hai",
    3: "ba",
    4: "bốn",
    5: "năm",
    6: "sáu",
    7: "bảy",
    8: "tám",
    9: "chín",
    10: "mười",
}

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 3000))
print("UDP Number Server đang chờ tin nhắn...")

while True:
    message, client_addr = server.recvfrom(1024)
    message = message.decode().strip()

    if message.lower() == "quit":
        server.sendto("Goodbye!".encode(), client_addr)
        break

    try:
        num = int(message)
        if 0 <= num <= 10:
            word = number_to_word[num]
            print(f"Nhận từ {client_addr}: {num}")
            server.sendto(f"Số {num} đọc là: {word}".encode(), client_addr)
        else:
            server.sendto("Vui lòng nhập số từ 0 đến 10".encode(), client_addr)
    except:
        server.sendto("Vui lòng nhập số hợp lệ".encode(), client_addr)

server.close()
