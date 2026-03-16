import asyncio
import os
import struct
import json

UPLOAD_DIR = "uploads_bai1"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


async def handle_client(reader, writer):
    addr = writer.get_extra_info("peername")
    print(f"[*] Connection from {addr}")

    try:
        while True:
            # Read type: 4 bytes (STAT or FILE)
            header_type_raw = await reader.read(4)
            if not header_type_raw:
                break

            header_type = header_type_raw.decode("utf-8").strip()

            if header_type == "STAT":
                # Read data length: 4 bytes
                data_len_raw = await reader.readexactly(4)
                data_len = struct.unpack("!I", data_len_raw)[0]

                # Read JSON data
                data_raw = await reader.readexactly(data_len)
                stats = json.loads(data_raw.decode("utf-8"))

                print(f"\n[STATS from {addr}]")
                print(f"  CPU Usage: {stats['cpu']}%")
                print(f"  RAM Usage: {stats['ram']}%")
                print(f"  Network Sent: {stats['net_sent']} bytes")
                print(f"  Network Recv: {stats['net_recv']} bytes")

            elif header_type == "FILE":
                # Read filename length: 4 bytes
                fn_len_raw = await reader.readexactly(4)
                fn_len = struct.unpack("!I", fn_len_raw)[0]

                # Read filename
                filename = (await reader.readexactly(fn_len)).decode("utf-8")

                # Read filesize: 8 bytes
                filesize_raw = await reader.readexactly(8)
                filesize = struct.unpack("!Q", filesize_raw)[0]

                print(f"[*] Receiving file: {filename} ({filesize} bytes)")

                save_path = os.path.join(UPLOAD_DIR, filename)
                received = 0
                with open(save_path, "wb") as f:
                    while received < filesize:
                        chunk = await reader.read(min(65536, filesize - received))
                        if not chunk:
                            break
                        f.write(chunk)
                        received += len(chunk)

                print(f"[+] File {filename} saved successfully.")

            else:
                print(f"[!] Unknown header type: {header_type}")
                break

    except Exception as e:
        print(f"[!] Error handling client {addr}: {e}")
    finally:
        print(f"[*] Connection closed from {addr}")
        writer.close()
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 9999)
    print(f"[*] Bài 1 Server running on 127.0.0.1:9999")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
