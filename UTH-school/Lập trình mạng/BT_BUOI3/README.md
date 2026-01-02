# BÀI TẬP BUỔI 03 - GIAO THỨC UDP

## 📋 MÔ TẢ

Buổi học này tập trung vào **Giao thức UDP (User Datagram Protocol)**:

- Chuyển đổi các ví dụ từ TCP sang UDP
- Lập trình ứng dụng DNS Client (phân giải tên miền)
- Lập trình ứng dụng DHCP Client (xin cấp địa chỉ IP)

## 🔄 SỰ KHÁC BIỆT GIỮA TCP VÀ UDP

### TCP (SOCK_STREAM)

```python
# Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 4000))
server.listen(1)
conn, addr = server.accept()
data = conn.recv(1024)
conn.send(response)

# Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 4000))
client.send(data)
response = client.recv(1024)
```

### UDP (SOCK_DGRAM)

```python
# Server
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 4000))
data, client_addr = server.recvfrom(1024)
server.sendto(response, client_addr)

# Client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(data, ("localhost", 4000))
response, server_addr = client.recvfrom(1024)
```

## 📁 CẤU TRÚC THỨ MỤC

```
BT_BUOI3/
├── client/
│   ├── client1.py       # UDP client cơ bản
│   ├── client2.py       # UDP client cơ bản (biến thể)
│   ├── client3.py       # UDP client với input
│   ├── client4.py       # UDP chat client (loop)
│   ├── client5.py       # UDP number-to-word client
│   └── ...
├── server/
│   ├── server1.py       # UDP server cơ bản
│   ├── server2.py       # UDP server cơ bản (biến thể)
│   ├── server3.py       # UDP chat server
│   ├── server4.py       # UDP chat server (loop)
│   ├── server5.py       # UDP number-to-word server
│   └── ...
├── dns_client.py        # 🌟 DNS Client (phân giải tên miền)
├── dhcp_client.py       # 🌟 DHCP Client (xin cấp IP)
├── convert_tcp_to_udp.py # Script chuyển đổi
└── README.md            # File này
```

## 🌟 ỨNG DỤNG QUAN TRỌNG

### 1. DNS Client (dns_client.py)

**Mô tả:** Phân giải tên miền thành địa chỉ IP

**Tính năng:**

- Xây dựng DNS query theo chuẩn RFC 1035
- Gửi UDP packet đến DNS server (port 53)
- Parse DNS response để lấy địa chỉ IP
- Hỗ trợ nhiều DNS server (mặc định: Google DNS 8.8.8.8)

**Cách chạy:**

```bash
python dns_client.py
```

**Ví dụ sử dụng:**

```
Nhập tên miền cần phân giải: google.com
🔍 Đang phân giải google.com...
✅ Kết quả:
   1. 142.250.185.46
   2. 142.250.185.14
```

**Lưu ý:**

- Cần kết nối Internet để truy vấn DNS server
- Có thể thay đổi DNS server trong code (8.8.8.8, 1.1.1.1, v.v.)

### 2. DHCP Client (dhcp_client.py)

**Mô tả:** Xin cấp địa chỉ IP từ DHCP Server

**Tính năng:**

- Xây dựng DHCP DISCOVER packet theo chuẩn RFC 2131
- Broadcast UDP packet đến DHCP server (port 67)
- Nhận và parse DHCP OFFER
- Hiển thị thông tin: IP, Subnet Mask, Gateway, DNS, Lease Time

**Cách chạy (Cần quyền Administrator):**

```bash
# Windows
python dhcp_client.py

# Hoặc chạy PowerShell/CMD với quyền Administrator
```

**Lưu ý:**

- ⚠️ Cần quyền Administrator để bind port 68
- Cần có DHCP server trong mạng (router, server, simulator)
- Có thể dùng DHCP simulator để test trên localhost

**Kết quả mẫu:**

```
✅ THÀNH CÔNG! Nhận được DHCP OFFER:

   🌐 Địa chỉ IP được cấp: 192.168.1.100
   🖥️  DHCP Server: 192.168.1.1
   📡 Subnet Mask: 255.255.255.0
   🚪 Default Gateway: 192.168.1.1
   🔍 DNS Servers: 8.8.8.8, 8.8.4.4
   ⏰ Lease Time: 86400s (24.0 giờ)
```

## 🚀 HƯỚNG DẪN CHẠY

### Các ví dụ cơ bản (client + server)

**Bước 1:** Mở Terminal/CMD, chạy server:

```bash
cd E:\leaning\python\quantrimang\BT_BUOI3
python server/server1.py
```

**Bước 2:** Mở Terminal/CMD khác, chạy client:

```bash
cd E:\leaning\python\quantrimang\BT_BUOI3
python client/client1.py
```

### DNS Client

**Chạy trực tiếp:**

```bash
python dns_client.py
```

**Test các tên miền:**

- google.com
- facebook.com
- github.com
- youtube.com

### DHCP Client

**Chạy với quyền Administrator:**

```bash
# Windows: Click phải PowerShell → Run as Administrator
python dhcp_client.py
```

## 📝 KIẾN THỨC VỀ UDP

### Ưu điểm của UDP:

✅ Tốc độ nhanh (không cần thiết lập kết nối)
✅ Overhead thấp (header nhỏ)
✅ Hỗ trợ broadcast/multicast
✅ Phù hợp cho streaming, gaming, DNS, DHCP

### Nhược điểm của UDP:

❌ Không đảm bảo gói tin đến đích
❌ Không đảm bảo thứ tự gói tin
❌ Không có cơ chế kiểm soát luồng
❌ Không có cơ chế kiểm tra lỗi (trừ checksum cơ bản)

### Khi nào dùng UDP?

- DNS (Domain Name System)
- DHCP (Dynamic Host Configuration Protocol)
- Streaming video/audio
- Online gaming
- VoIP (Voice over IP)
- IoT sensors

### Khi nào dùng TCP?

- HTTP/HTTPS (Web)
- FTP (File Transfer)
- Email (SMTP, POP3, IMAP)
- SSH, Telnet
- Database connections

## 🔧 TROUBLESHOOTING

### DNS Client

**Lỗi:** Timeout
**Giải pháp:**

- Kiểm tra kết nối Internet
- Thử DNS server khác (1.1.1.1, 8.8.4.4)
- Kiểm tra Firewall

### DHCP Client

**Lỗi:** Permission denied (port 68)
**Giải pháp:**

- Chạy với quyền Administrator
- Hoặc sửa code để dùng port khác (>1024)

**Lỗi:** Timeout (không nhận DHCP OFFER)
**Giải pháp:**

- Kiểm tra có DHCP server trong mạng
- Tắt Firewall tạm thời
- Dùng DHCP simulator để test

## 📚 TÀI LIỆU THAM KHẢO

- **UDP Protocol:** RFC 768
- **DNS Protocol:** RFC 1035
- **DHCP Protocol:** RFC 2131
- **Python socket:** https://docs.python.org/3/library/socket.html

## 💡 BÀI TẬP THÊM

1. Viết DNS server đơn giản (local DNS cache)
2. Hoàn thiện DHCP client với DHCP REQUEST
3. Tạo UDP chat room (nhiều client)
4. Viết UDP file transfer với checksum
5. Tạo UDP port scanner

## 👨‍💻 NOTES

- Tất cả các file trong `client/` và `server/` đã được chuyển từ TCP sang UDP
- DNS Client và DHCP Client là 2 ứng dụng thực tế quan trọng
- Code được viết với mục đích học tập, không dùng trong production

---

**Tác giả:** Bài tập thực hành Quản trị mạng
**Ngày cập nhật:** 2025-12-31
