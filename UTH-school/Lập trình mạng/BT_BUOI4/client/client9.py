import socket
import time

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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 3000))
server.listen(1)
print("Delay Number Server đang chờ kết nối...")

conn, addr = server.accept()
print(f"Client {addr} đã kết nối")

while True:
    message = conn.recv(1024).decode().strip()

    if message.lower() == "quit":
        conn.send("Goodbye!".encode())
        break

    try:
        num = int(message)
        if 0 <= num <= 10:
            print(f"Nhận số: {num}, đợi {num} giây...")
            time.sleep(num)  # Delay theo số giây

            word = number_to_word[num]
            conn.send(f"Số {num} đọc là: {word}".encode())
        else:
            conn.send("Vui lòng nhập số từ 0 đến 10".encode())
    except:
        conn.send("Vui lòng nhập số hợp lệ".encode())

conn.close()
server.close()
