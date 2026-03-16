import asyncio
import os
import struct
import sys


async def upload_file(host, port, filepath):
    if not os.path.exists(filepath):
        print(f"[!] File không tồn tại: {filepath}")
        return

    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    try:
        reader, writer = await asyncio.open_connection(host, port)
        print(f"[*] Bắt đầu upload: {filename} ({filesize} bytes)")

        # 1. Gửi độ dài tên file
        filename_bytes = filename.encode("utf-8")
        writer.write(struct.pack("!I", len(filename_bytes)))

        # 2. Gửi tên file
        writer.write(filename_bytes)

        # 3. Gửi dung lượng file
        writer.write(struct.pack("!Q", filesize))
        await writer.drain()

        # 4. Gửi dữ liệu file theo từng block
        sent_bytes = 0
        with open(filepath, "rb") as f:
            while sent_bytes < filesize:
                chunk = f.read(65536)
                if not chunk:
                    break
                writer.write(chunk)
                await writer.drain()
                sent_bytes += len(chunk)

                # Hiển thị tiến trình
                percent = (sent_bytes / filesize) * 100
                print(f"[{filename}] Tiến trình: {percent:.2f}%", end="\r")

        print(f"\n[+] Upload thành công: {filename}")

    except Exception as e:
        print(f"\n[!] Lỗi khi upload {filename}: {e}")
    finally:
        writer.close()
        await writer.wait_closed()


async def main():
    # Danh sách file cần upload (Lấy từ tham số dòng lệnh)
    if len(sys.argv) < 2:
        print("Sử dụng: python client_upload.py file1.mp3 file2.mp4 ...")
        return

    files_to_upload = sys.argv[1:]
    host = "127.0.0.1"
    port = 8888

    # Sử dụng asyncio.gather để upload đồng thời
    tasks = [upload_file(host, port, f) for f in files_to_upload]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[*] Đã dừng client.")
