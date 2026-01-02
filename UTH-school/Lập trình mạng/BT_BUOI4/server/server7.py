import socket


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char
    return result


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 3000))
server.listen(1)
print("Encrypted Chat Server đang chờ kết nối...")

conn, addr = server.accept()
print(f"Client {addr} đã kết nối")

shift = 1  # Số ký tự dịch chuyển

while True:
    encrypted = conn.recv(1024).decode()

    if encrypted == "0":
        conn.send("Goodbye!".encode())
        break

    decrypted = decrypt(encrypted, shift)
    print(f"Nhận (mã hóa): {encrypted}")
    print(f"Giải mã: {decrypted}")

    response = f"Server đã nhận: {decrypted}"
    conn.send(response.encode())

conn.close()
server.close()
