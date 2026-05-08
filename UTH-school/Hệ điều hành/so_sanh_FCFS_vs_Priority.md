# So sánh thuật toán FCFS và Priority Scheduling (Non-Preemptive)

Tài liệu này so sánh hai thuật toán lập lịch CPU được cài đặt trong thư mục:
- `fcfs.py` — FCFS (First-Come, First-Served)
- `main.py` — Priority Scheduling (Non-Preemptive)

---

## 1. Tổng quan

| Tiêu chí | FCFS | Priority Scheduling |
|---|---|---|
| Tên đầy đủ | First-Come, First-Served | Priority Scheduling (Non-Preemptive) |
| Tiêu chí chọn tiến trình | Thời điểm đến sớm nhất (Arrival Time) | Độ ưu tiên cao nhất (Priority nhỏ nhất) |
| Dữ liệu đầu vào mỗi tiến trình | Arrival Time, Burst Time | Arrival Time, Burst Time, **Priority** |
| Chiếm quyền (Preemption) | Không | Không (phiên bản này) |
| Xử lý tie-break | Nhập trước chạy trước | Priority bằng nhau → Arrival sớm hơn chạy trước |
| Độ phức tạp cài đặt | Đơn giản nhất | Vừa phải |
| Độ phức tạp thời gian | O(n log n) (do sort) | O(n²) (quét available mỗi lần) |

---

## 2. Cách hoạt động

### 2.1. FCFS
1. Sắp xếp các tiến trình theo **Arrival Time** tăng dần.
2. Lần lượt đưa từng tiến trình vào CPU theo thứ tự đó.
3. Nếu CPU rảnh (current_time < arrival của tiến trình kế tiếp) → chèn khoảng **IDLE**.
4. Tiến trình chạy hết Burst Time mới nhả CPU (non-preemptive).

### 2.2. Priority Scheduling (Non-Preemptive)
1. Ở mỗi thời điểm T, liệt kê các tiến trình **đã tới** và **chưa hoàn thành** → tập `available`.
2. Trong `available`, chọn tiến trình có **Priority nhỏ nhất** (ưu tiên cao nhất).
3. Nếu Priority trùng nhau → chọn tiến trình có Arrival sớm hơn.
4. Tiến trình đã chọn chạy hết Burst Time (không bị ngắt).
5. Nếu tại T không có tiến trình nào sẵn sàng → tăng T lên 1, lặp lại.

---

## 3. Các công thức chung

- **Finish Time (FT)**: thời điểm tiến trình kết thúc.
- **Turn Around Time (TAT)** = Finish Time − Arrival Time
- **Waiting Time (WT)** = TAT − Burst Time
- **Avg TAT** = Σ TAT / n
- **Avg WT** = Σ WT / n

---

## 4. Ví dụ minh họa

Giả sử cùng tập dữ liệu:

| Process | Arrival | Burst | Priority |
|---|---|---|---|
| P1 | 0 | 5 | 3 |
| P2 | 1 | 3 | 1 |
| P3 | 2 | 2 | 4 |
| P4 | 3 | 4 | 2 |

### 4.1. Kết quả khi chạy FCFS (bỏ qua cột Priority)

Thứ tự thực thi theo Arrival: **P1 → P2 → P3 → P4**

Gantt: `0 ---[P1]---> 5 ---[P2]---> 8 ---[P3]---> 10 ---[P4]---> 14`

| Process | Arrival | Burst | Finish | TAT | WT |
|---|---|---|---|---|---|
| P1 | 0 | 5 | 5  | 5  | 0 |
| P2 | 1 | 3 | 8  | 7  | 4 |
| P3 | 2 | 2 | 10 | 8  | 6 |
| P4 | 3 | 4 | 14 | 11 | 7 |

- Avg TAT = (5 + 7 + 8 + 11) / 4 = **7.75**
- Avg WT  = (0 + 4 + 6 + 7) / 4  = **4.25**

### 4.2. Kết quả khi chạy Priority Scheduling

Diễn biến:
- T = 0: chỉ có P1 → chạy P1 đến T = 5.
- T = 5: có P2 (prio 1), P3 (prio 4), P4 (prio 2) → chọn **P2** (prio 1). Chạy đến T = 8.
- T = 8: có P3, P4 → chọn **P4** (prio 2 < 4). Chạy đến T = 12.
- T = 12: còn **P3**. Chạy đến T = 14.

Gantt: `0 ---[P1]---> 5 ---[P2]---> 8 ---[P4]---> 12 ---[P3]---> 14`

| Process | Arrival | Burst | Priority | Finish | TAT | WT |
|---|---|---|---|---|---|---|
| P1 | 0 | 5 | 3 | 5  | 5  | 0  |
| P2 | 1 | 3 | 1 | 8  | 7  | 4  |
| P3 | 2 | 2 | 4 | 14 | 12 | 10 |
| P4 | 3 | 4 | 2 | 12 | 9  | 5  |

- Avg TAT = (5 + 7 + 12 + 9) / 4 = **8.25**
- Avg WT  = (0 + 4 + 10 + 5) / 4 = **4.75**

### 4.3. Nhận xét từ ví dụ

- Với dữ liệu cụ thể này, **FCFS cho Avg TAT/WT tốt hơn** một chút, nhưng đây là ngẫu nhiên.
- Nếu một tiến trình ngắn đến muộn hơn nhưng ưu tiên cao (Priority = 1), Priority Scheduling sẽ thể hiện lợi thế.
- P3 có Priority thấp nhất (= 4) nên bị đẩy xuống cuối → bị **đói tương đối** (WT cao nhất = 10).

---

## 5. Ưu — Nhược điểm

### 5.1. FCFS
**Ưu điểm**
- Cực kỳ đơn giản, dễ cài đặt và dễ hiểu.
- Công bằng theo thứ tự đến — không có tiến trình nào bị bỏ qua.
- Không có hiện tượng **starvation** (đói CPU).

**Nhược điểm**
- **Convoy Effect**: một tiến trình Burst dài đến trước sẽ làm tất cả tiến trình ngắn đến sau bị chờ lâu → Avg WT cao.
- Không phản ánh được mức độ quan trọng (ưu tiên) của tiến trình.
- Không phù hợp cho hệ thống tương tác (interactive) hoặc real-time.

### 5.2. Priority Scheduling
**Ưu điểm**
- Phản ánh được **mức độ quan trọng** của từng tiến trình (system task, user task…).
- Linh hoạt, phù hợp hệ thống có yêu cầu QoS khác nhau.
- Thường cho Avg TAT/WT tốt hơn FCFS khi dữ liệu có priority phân hóa rõ.

**Nhược điểm**
- **Starvation**: tiến trình có priority thấp có thể không bao giờ được chạy nếu liên tục có tiến trình priority cao hơn đến.
  - Giải pháp: **Aging** — tăng dần priority theo thời gian chờ.
- Phải duy trì giá trị priority cho mỗi tiến trình → phức tạp hơn.
- Phiên bản non-preemptive vẫn có thể bị một tiến trình priority thấp "giữ" CPU khi đến trước (T = 0 ví dụ trên: P1 priority 3 chạy toàn bộ dù P2 priority 1 đến ngay sau đó).

---

## 6. Khi nào dùng thuật toán nào?

| Tình huống | Thuật toán phù hợp |
|---|---|
| Hệ thống batch đơn giản, các job tương đối đồng đều | FCFS |
| Không cần phân biệt quan trọng giữa các job | FCFS |
| Giảng dạy / minh họa khái niệm cơ bản nhất | FCFS |
| Hệ thống đa người dùng có task hệ thống + task user | Priority |
| Có job cần SLA cao hơn (vd: giao dịch ngân hàng, task admin) | Priority |
| Muốn giảm Avg WT tổng thể khi priority phản ánh đúng độ ngắn/quan trọng của job | Priority |

---

## 7. Bảng so sánh tổng hợp

| Tiêu chí | FCFS | Priority (Non-Preemptive) |
|---|---|---|
| Đầu vào | Arrival, Burst | Arrival, Burst, Priority |
| Thứ tự chạy | Theo Arrival | Theo Priority, tie-break bằng Arrival |
| Preemption | Không | Không |
| Starvation | Không có | **Có thể xảy ra** |
| Cần cơ chế Aging | Không | Có (để chống starvation) |
| Công bằng | Công bằng theo thời gian đến | Không công bằng với priority thấp |
| Avg WT | Thường cao khi có job dài đến trước | Thường thấp hơn nếu priority được gán hợp lý |
| Độ phức tạp cài đặt | O(n log n) | O(n²) trong cài đặt trực quan |
| Ứng dụng thực tế | Batch system cơ bản | Hệ điều hành đa nhiệm, real-time soft |

---

## 8. Cách chạy thử

```bash
# Chạy Priority Scheduling (main.py)
python main.py

# Chạy FCFS
python fcfs.py
```

Cả hai chương trình đều cho phép **nhập trực tiếp từng tiến trình** từ bàn phím:
1. Số lượng tiến trình `n`.
2. Với mỗi P: Arrival Time, Burst Time (và Priority cho `main.py`).

Để so sánh công bằng, hãy nhập **cùng một tập dữ liệu** (Arrival + Burst giống nhau) vào cả hai chương trình, rồi đối chiếu Gantt Chart / Avg TAT / Avg WT.
