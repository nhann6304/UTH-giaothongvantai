import asyncio
import os
import struct
from datetime import datetime

# Thư mục lưu trữ file upload
UPLOAD_DIR = "uploads"

# Tạo thư mục nếu chưa tồn tại
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


async def handle_upload(reader, writer):
    addr = writer.get_extra_info("peername")
    print(f"[*] Kết nối từ: {addr}")

    try:
        # 1. Nhận độ dài tên file (4 bytes, kiểu unsigned int)
        raw_fn_len = await reader.readexactly(4)
        fn_len = struct.unpack("!I", raw_fn_len)[0]

        # 2. Nhận tên file
        filename = (await reader.readexactly(fn_len)).decode("utf-8")

        # 3. Nhận dung lượng file (8 bytes, kiểu unsigned long long)
        raw_filesize = await reader.readexactly(8)
        filesize = struct.unpack("!Q", raw_filesize)[0]

        # 4. Tạo tên file mới với timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        save_filename = f"{timestamp}_{filename}"
        save_path = os.path.join(UPLOAD_DIR, save_filename)

        print(f"[*] Đang nhận file: {filename} ({filesize} bytes) từ {addr}")

        # 5. Nhận dữ liệu file và lưu lại
        received_bytes = 0
        with open(save_path, "wb") as f:
            while received_bytes < filesize:
                chunk_size = min(65536, filesize - received_bytes)
                data = await reader.read(chunk_size)
                if not data:
                    break
                f.write(data)
                received_bytes += len(data)

                # Hiển thị tiến trình
                percent = (received_bytes / filesize) * 100
                print(
                    f"\r[{addr}] Tiến trình: {percent:.2f}% ({received_bytes}/{filesize} bytes)",
                    end="",
                    flush=True,
                )

        print(f"\n[+] File {filename} đã được nhận thành công từ {addr}")

    except Exception as e:
        print(f"\n[!] Lỗi khi xử lý {addr}: {e}")
    finally:
        writer.close()
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_upload, "127.0.0.1", 8888)
    addr = server.sockets[0].getsockname()
    print(f"[*] Server đang chạy tại {addr}...")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[*] Server đang dừng...")
