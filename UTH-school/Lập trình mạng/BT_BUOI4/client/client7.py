import socket


def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 3000))
print("Kết nối thành công! (Nhấn 0 để thoát)")

shift = 1  # Số ký tự dịch chuyển

while True:
    message = input("You: ")

    if message == "0":
        client.send(message.encode())
        response = client.recv(1024).decode()
        print(response)
        break

    encrypted = encrypt(message, shift)
    print(f"Gửi (mã hóa): {encrypted}")
    client.send(encrypted.encode())

    response = client.recv(1024).decode()
    print(response)

client.close()
