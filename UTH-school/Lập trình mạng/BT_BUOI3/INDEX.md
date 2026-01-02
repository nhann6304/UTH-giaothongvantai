# 📚 INDEX - BÀI TẬP BUỔI 03

## 🎯 BẮT ĐẦU TỪ ĐÂY

Bạn mới bắt đầu? Đọc theo thứ tự:

1. **[QUICKSTART.md](QUICKSTART.md)** ⭐⭐⭐ - Bắt đầu tại đây!
2. **[README.md](README.md)** - Hướng dẫn chi tiết
3. **[SUMMARY.md](SUMMARY.md)** - Tổng kết công việc

## 🚀 CHẠY THỰC HÀNH NGAY

### Lựa chọn 1: DNS Client Simple (Dễ nhất)

```bash
python dns_client_simple.py
```

### Lựa chọn 2: So sánh TCP vs UDP

```bash
python tcp_vs_udp_demo.py
```

### Lựa chọn 3: DNS Client Advanced

```bash
python dns_client.py
```

### Lựa chọn 4: DHCP Client (Cần Admin)

```bash
# Run as Administrator
python dhcp_client.py
```

## 📁 CẤU TRÚC DỰ ÁN

```
BT_BUOI3/
│
├── 📄 INDEX.md (File này)
├── 📄 QUICKSTART.md      ⭐ Bắt đầu tại đây
├── 📄 README.md          📚 Hướng dẫn chi tiết
├── 📄 SUMMARY.md         ✅ Tổng kết
│
├── 🌟 dns_client_simple.py    ⭐⭐⭐ DNS đơn giản
├── 🌟 dns_client.py           ⭐⭐ DNS thực tế
├── 🌟 dhcp_client.py          ⭐⭐ DHCP client
├── 🌟 tcp_vs_udp_demo.py      ⭐⭐⭐ So sánh TCP/UDP
│
├── 🔧 convert_tcp_to_udp.py   Tiện ích chuyển đổi
│
├── 📁 client/
│   ├── client1.py → client10.py
│   └── (7/10 đã chuyển UDP)
│
└── 📁 server/
    ├── server1.py → server10.py
    └── (5/10 đã chuyển UDP)
```

## 📖 HƯỚNG DẪN SỬ DỤNG

### Cho người mới học UDP:

1. Đọc [QUICKSTART.md](QUICKSTART.md)
2. Chạy `tcp_vs_udp_demo.py`
3. Chạy `dns_client_simple.py`
4. Thử `client1.py` + `server1.py`

### Cho người muốn hiểu sâu:

1. Đọc [README.md](README.md)
2. Xem code `dns_client.py`
3. Xem code `dhcp_client.py`
4. Chạy các ví dụ nâng cao (client6, client7)

### Cho giảng viên/người chấm bài:

1. Xem [SUMMARY.md](SUMMARY.md) - Tổng kết công việc
2. Test DNS Client: `python dns_client_simple.py`
3. Test TCP vs UDP: `python tcp_vs_udp_demo.py`
4. Kiểm tra các file đã chuyển đổi

## 🎓 NỘI DUNG HỌC TẬP

### Lý thuyết UDP:

- So sánh TCP vs UDP
- Khi nào dùng UDP?
- Ưu/nhược điểm UDP
  → Xem trong [README.md](README.md)

### Thực hành:

- [x] Chuyển đổi TCP → UDP
- [x] DNS Client (phân giải tên miền)
- [x] DHCP Client (xin cấp IP)
      → Hướng dẫn trong [QUICKSTART.md](QUICKSTART.md)

## 🔗 QUICK LINKS

| Nội dung           | File                                         | Độ quan trọng |
| ------------------ | -------------------------------------------- | ------------- |
| Hướng dẫn nhanh    | [QUICKSTART.md](QUICKSTART.md)               | ⭐⭐⭐        |
| DNS đơn giản       | [dns_client_simple.py](dns_client_simple.py) | ⭐⭐⭐        |
| TCP vs UDP         | [tcp_vs_udp_demo.py](tcp_vs_udp_demo.py)     | ⭐⭐⭐        |
| Hướng dẫn chi tiết | [README.md](README.md)                       | ⭐⭐          |
| DNS thực tế        | [dns_client.py](dns_client.py)               | ⭐⭐          |
| DHCP Client        | [dhcp_client.py](dhcp_client.py)             | ⭐⭐          |
| Tổng kết           | [SUMMARY.md](SUMMARY.md)                     | ⭐            |

## ❓ TRỢ GIÚP

### Tôi nên bắt đầu từ đâu?

→ Đọc [QUICKSTART.md](QUICKSTART.md)

### Tôi muốn hiểu UDP?

→ Chạy `tcp_vs_udp_demo.py`, đọc [README.md](README.md)

### Tôi muốn test DNS?

→ Chạy `dns_client_simple.py`

### Tôi muốn hiểu DNS hoạt động như thế nào?

→ Xem code trong `dns_client.py`

### Tôi muốn test DHCP?

→ Chạy với Admin: `dhcp_client.py`

### Còn file nào cần chuyển đổi?

→ Xem [SUMMARY.md](SUMMARY.md), dùng pattern trong [README.md](README.md)

## 📞 LIÊN HỆ & HỖ TRỢ

- Lỗi về DNS: Kiểm tra Internet, thử DNS khác
- Lỗi về DHCP: Cần quyền Admin, cần DHCP server
- Lỗi UDP: Xem phần Troubleshooting trong README.md

---

**Cập nhật:** 2025-12-31
**Trạng thái:** ✅ SẴN SÀNG SỬ DỤNG

Chúc bạn học tập thành công! 🎉
