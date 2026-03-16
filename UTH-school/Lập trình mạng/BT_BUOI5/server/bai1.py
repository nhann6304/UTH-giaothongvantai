import asyncio


async def handle_client(reader, writer):
    while True:
        data = await reader.read(100)
        if not data:
            break

        num = int(data.decode())
        print(f"Server nhận: {num}")

        await asyncio.sleep(num)  # Đợi num giây

        writer.write(str(num).encode())
        await writer.drain()
        print(f"Server gửi: {num}")

    writer.close()


async def start_server():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 8888)
    print("Server đang chạy port 8888")
    async with server:
        await server.serve_forever()
