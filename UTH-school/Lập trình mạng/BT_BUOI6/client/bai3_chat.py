import socket
import threading
import sys

# BROADCAST SETTINGS
BROADCAST_IP = "255.255.255.255"
CHAT_PORT = 12345


def receiver(sock):
    """Function to receive broadcast messages."""
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            message = data.decode("utf-8")
            # Don't print own messages if we want to filter (optional)
            # if addr[0] != socket.gethostbyname(socket.gethostname()):
            print(f"\n[{addr[0]}] : {message}")
            print("Chat > ", end="", flush=True)
        except Exception as e:
            print(f"Error receiving: {e}")
            break


def sender(sock, name):
    """Function to send broadcast messages."""
    print(f"Welcome {name}! Type your message and press Enter.")
    while True:
        try:
            msg = input("Chat > ")
            if msg.lower() == "exit":
                break

            full_msg = f"{name}: {msg}"
            sock.sendto(full_msg.encode("utf-8"), (BROADCAST_IP, CHAT_PORT))
        except Exception as e:
            print(f"Error sending: {e}")
            break


def main():
    name = input("Enter your chat name: ")

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Reuse address to allow multiple instances on same machine for testing
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to all interfaces
    sock.bind(("", CHAT_PORT))

    # Start receiver thread
    recv_thread = threading.Thread(target=receiver, args=(sock,), daemon=True)
    recv_thread.start()

    # Start sender (main thread)
    sender(sock, name)

    sock.close()
    print("Chat closed.")


if __name__ == "__main__":
    main()
