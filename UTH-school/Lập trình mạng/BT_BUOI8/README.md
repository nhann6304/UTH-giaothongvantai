# Chat Application - Python Socket

Ứng dụng chat đơn giản sử dụng Python Socket để chat real-time giữa nhiều client.

## Tính năng

- ✅ Chat real-time giữa nhiều người
- ✅ Hệ thống nickname
- ✅ Thông báo khi có người join/leave
- ✅ Đơn giản, dễ sử dụng

## Cách chạy

### Bước 1: Chạy Server

```bash
python server.py
```

Server sẽ chạy tại `localhost:5555`

### Bước 2: Chạy Client (mở nhiều terminal)

```bash
python client.py
```

Mỗi terminal là 1 người chat. Bạn có thể mở 2, 3, 4... terminal để test.

## Hướng dẫn sử dụng

1. Chạy `server.py` trước
2. Mở nhiều terminal/cmd
3. Chạy `client.py` ở mỗi terminal
4. Nhập nickname
5. Bắt đầu chat!
6. Gõ `/quit` để thoát

## Cấu trúc

```
BT_BUOI8/
├── server.py          # Chat server
├── client.py          # Chat client
└── README.md          # Hướng dẫn
```

## Công nghệ

- **Python Socket** - TCP Socket programming
- **Threading** - Xử lý nhiều client đồng thời
- **Encoding** - UTF-8 hỗ trợ tiếng Việt

## Ví dụ

### Terminal 1 (Server)

```
🚀 Chat Server đang chạy tại localhost:5555
Đang chờ client kết nối...

[SERVER] Nhan đã tham gia. Tổng: 1 người online.
[SERVER] Minh đã tham gia. Tổng: 2 người online.
```

### Terminal 2 (Client 1)

```
Nhập nickname của bạn: Nhan
✅ Đã kết nối đến server!

[HỆ THỐNG] Chào mừng Nhan đến phòng chat!
[HỆ THỐNG] Minh đã tham gia phòng chat!

[Minh] Chào Nhan!
Chào Minh, bạn khỏe không?
```

### Terminal 3 (Client 2)

```
Nhập nickname của bạn: Minh
✅ Đã kết nối đến server!

[HỆ THỐNG] Chào mừng Minh đến phòng chat!

Chào Nhan!
[Nhan] Chào Minh, bạn khỏe không?
```

## Lưu ý

- Server phải chạy trước client
- Mỗi client cần 1 terminal/cmd riêng
- Hỗ trợ tiếng Việt có dấu
- Gõ `/quit` để thoát

---

**Nhóm 3 - Môn Lập trình mạng**
