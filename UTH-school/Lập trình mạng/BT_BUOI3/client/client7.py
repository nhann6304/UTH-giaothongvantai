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


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("localhost", 3000)
print("UDP Caesar Cipher Client sẵn sàng! (Nhấn 0 để thoát)")

shift = 1  # Số ký tự dịch chuyển

while True:
    message = input("You: ")

    if message == "0":
        client.sendto(message.encode(), server_addr)
        response, addr = client.recvfrom(1024)
        print(response.decode())
        break

    encrypted = encrypt(message, shift)
    print(f"Gửi (mã hóa): {encrypted}")
    client.sendto(encrypted.encode(), server_addr)

    response, addr = client.recvfrom(1024)
    print(response.decode())

client.close()
