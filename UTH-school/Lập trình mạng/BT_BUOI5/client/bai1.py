import asyncio
import time


# SERVER
async def handle_client(reader, writer):
    while True:
        data = await reader.read(100)
        if not data:
            break

        num = int(data.decode())
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] SERVER nhận: {num}")

        await asyncio.sleep(num)

        writer.write(str(num).encode())
        await writer.drain()
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] SERVER gửi: {num}")

    writer.close()


# CLIENT
async def send_number(num):
    reader, writer = await asyncio.open_connection("127.0.0.1", 8888)

    timestamp = time.strftime("%H:%M:%S")
    print(f"[{timestamp}] CLIENT gửi: {num} ( gửi sau  {num} giây)")
    writer.write(str(num).encode())
    await writer.drain()

    data = await reader.read(100)
    result = int(data.decode())
    timestamp = time.strftime("%H:%M:%S")
    print(f"[{timestamp}] CLIENT nhận: {result} (sau {num} giây)")

    writer.close()
    return result


async def run_client():
    await asyncio.sleep(1)

    results = await asyncio.gather(send_number(10), send_number(5))


#
async def start_server():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 8888)
    async with server:
        await server.serve_forever()


# MAIN
async def main():
    server_task = asyncio.create_task(start_server())
    await run_client()
    server_task.cancel()


asyncio.run(main())
