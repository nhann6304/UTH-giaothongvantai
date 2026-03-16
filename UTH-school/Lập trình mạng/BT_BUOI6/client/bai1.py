import asyncio
import os
import struct
import json
import psutil  # Ensure psutil is installed: pip install psutil


async def send_stats(writer):
    print("[*] Sending system stats...")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    net = psutil.net_io_counters()

    stats = {
        "cpu": cpu,
        "ram": ram,
        "net_sent": net.bytes_sent,
        "net_recv": net.bytes_recv,
    }

    data = json.dumps(stats).encode("utf-8")

    # Header: TYPE(4) + LEN(4)
    writer.write(b"STAT")
    writer.write(struct.pack("!I", len(data)))
    writer.write(data)
    await writer.drain()
    print("[+] Stats sent.")


async def send_file(writer, filepath):
    if not os.path.exists(filepath):
        print(f"[!] File not found: {filepath}")
        return

    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)
    filename_bytes = filename.encode("utf-8")

    print(f"[*] Sending file: {filename} ({filesize} bytes)")

    # Header: TYPE(4) + FN_LEN(4) + FILENAME + FILESIZE(8)
    writer.write(b"FILE")
    writer.write(struct.pack("!I", len(filename_bytes)))
    writer.write(filename_bytes)
    writer.write(struct.pack("!Q", filesize))
    await writer.drain()

    sent = 0
    with open(filepath, "rb") as f:
        while sent < filesize:
            chunk = f.read(65536)
            if not chunk:
                break
            writer.write(chunk)
            await writer.drain()
            sent += len(chunk)
            print(f"  Progress: {(sent/filesize)*100:.2f}%", end="\r")

    print(f"\n[+] File {filename} sent.")


async def main():
    host = "127.0.0.1"
    port = 9999

    try:
        reader, writer = await asyncio.open_connection(host, port)

        while True:
            print("\n--- Bài 1: Menu ---")
            print("1. Send System Stats")
            print("2. Send File")
            print("3. Exit")
            choice = input("Select: ")

            if choice == "1":
                await send_stats(writer)
            elif choice == "2":
                filepath = input("Enter file path: ")
                await send_file(writer, filepath)
            elif choice == "3":
                break
            else:
                print("Invalid choice.")

        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print(f"[!] Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
