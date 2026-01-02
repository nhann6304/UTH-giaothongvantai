# BÁO CÁO BÀI TẬP BUỔI 03 - GIAO THỨC UDP

**Sinh viên:** [Tên của bạn]  
**Ngày nộp:** 31/12/2025

---

## YÊU CẦU BÀI TẬP

1. Sửa nội dung Buổi 03 từ TCP → UDP
2. Lập trình DNS Client (phân giải tên miền → IP)
3. Lập trình DHCP Client (xin cấp địa chỉ IP)

---

## CÔNG VIỆC ĐÃ HOÀN THÀNH

### ✅ 1. Chuyển đổi TCP sang UDP

- Đã sửa `client1.py` → `client7.py` (7 files)
- Đã sửa `server1.py` → `server5.py` (5 files)
- Thay đổi chính: `SOCK_STREAM` → `SOCK_DGRAM`, bỏ `connect()`, dùng `sendto()/recvfrom()`

### ✅ 2. DNS Client

- **File:** `dns_client_simple.py` - Phiên bản đơn giản
- **File:** `dns_client.py` - Implementation theo RFC 1035
- **Chức năng:** Phân giải tên miền (vd: google.com) thành địa chỉ IP

### ✅ 3. DHCP Client

- **File:** `dhcp_client.py`
- **Chức năng:** Gửi DHCP DISCOVER, nhận IP/Subnet/Gateway/DNS từ DHCP server

---

## CÁCH CHẠY

### 1. DNS Client (Đơn giản nhất)

```bash
python dns_client_simple.py
```

Nhập tên miền: `google.com` → Hiển thị địa chỉ IP

### 2. So sánh TCP vs UDP

```bash
python tcp_vs_udp_demo.py
```

Tự động chạy và so sánh 2 giao thức

### 3. UDP Client/Server cơ bản

```bash
# Terminal 1 - Server
python server/server1.py

# Terminal 2 - Client
python client/client1.py
```

### 4. DNS Client (Advanced)

```bash
python dns_client.py
```

Nhập: `facebook.com` → Xem cách build DNS packet

### 5. DHCP Client (Cần Admin)

```bash
python dhcp_client.py
```

⚠️ Chạy với quyền Administrator

---

## CẤU TRÚC DỰ ÁN

```
BT_BUOI3/
├── dns_client_simple.py    # DNS đơn giản
├── dns_client.py            # DNS theo RFC 1035
├── dhcp_client.py           # DHCP Client
├── tcp_vs_udp_demo.py       # Demo so sánh
├── client/                  # 7 UDP clients
└── server/                  # 5 UDP servers
```

---

## KẾT QUẢ THỰC HIỆN

### DNS Client

- ✅ Phân giải google.com → 142.250.199.238
- ✅ Hỗ trợ bất kỳ tên miền nào
- ✅ Sử dụng Google DNS (8.8.8.8)

### DHCP Client

- ✅ Gửi DHCP DISCOVER broadcast
- ✅ Nhận DHCP OFFER từ server
- ✅ Hiển thị đầy đủ: IP, Subnet, Gateway, DNS, Lease Time

### UDP Conversion

- ✅ Tất cả files hoạt động đúng với UDP
- ✅ Không cần thiết lập kết nối
- ✅ Sử dụng sendto()/recvfrom()

---

## GHI CHÚ

- **TCP vs UDP:** UDP nhanh hơn, không đảm bảo delivery
- **DNS:** Cần Internet để test
- **DHCP:** Cần quyền Admin + DHCP server trong mạng
- **Source code:** Có đầy đủ comments tiếng Việt

---

**Kết luận:** Đã hoàn thành đầy đủ 3 yêu cầu bài tập ✅
