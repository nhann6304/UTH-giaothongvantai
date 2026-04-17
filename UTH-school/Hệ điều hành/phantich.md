# PRIORITY SCHEDULING (KHÔNG NGẮT)

---

## 1. Khái niệm

- Lập lịch CPU dựa trên độ ưu tiên
- Số ưu tiên càng nhỏ thì càng quan trọng
- Không ngắt: tiến trình chạy đến hết mới chuyển sang tiến trình khác

---

## 3. Công thức

- Thời gian hoàn tất = thời điểm hoàn thành - thời gian đến
- Thời gian chờ = thời gian hoàn tất - thời gian thực thi

---

## 4. Nguyên tắc

1. Xét các tiến trình đã đến
2. Chọn tiến trình có độ ưu tiên cao nhất
3. Nếu bằng nhau thì chọn tiến trình đến trước
4. Cho chạy đến hết
5. Lặp lại

---

## 5. Dữ liệu

| Tiến trình | Thời gian đến | Thời gian thực thi | Độ ưu tiên |
| ---------- | ------------- | ------------------ | ---------- |
| P1         | 0             | 5                  | 3          |
| P2         | 1             | 3                  | 1          |
| P3         | 2             | 2                  | 4          |
| P4         | 3             | 4                  | 2          |

---

## 6. Cách tính từng bước

Thời điểm 0:

- Chỉ có P1 → chạy từ 0 đến 5 → hoàn thành = 5

Thời điểm 5:

- Có P2, P3, P4 → chọn P2 → chạy từ 5 đến 8 → hoàn thành = 8

Thời điểm 8:

- Có P3, P4 → chọn P4 → chạy từ 8 đến 12 → hoàn thành = 12

Thời điểm 12:

- Còn P3 → chạy từ 12 đến 14 → hoàn thành = 14

---

## 7. Kết quả

| Tiến trình | Hoàn thành | Hoàn tất | Chờ |
| ---------- | ---------- | -------- | --- |
| P1         | 5          | 5        | 0   |
| P2         | 8          | 7        | 4   |
| P3         | 14         | 12       | 10  |
| P4         | 12         | 9        | 5   |

---

## 8. Trung bình

- Thời gian hoàn tất trung bình = (5 + 7 + 12 + 9) / 4 = 8.25
- Thời gian chờ trung bình = (0 + 4 + 10 + 5) / 4 = 4.75

---

## 9. Kết luận

- Luôn chọn tiến trình có độ ưu tiên cao nhất
- Không bị ngắt
- Làm bài theo thứ tự:
  1. Xác định thứ tự chạy
  2. Tính thời điểm hoàn thành
  3. Tính thời gian hoàn tất
  4. Tính thời gian chờ
