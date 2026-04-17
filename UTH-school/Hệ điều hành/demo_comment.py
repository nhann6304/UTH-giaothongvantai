# =============================================================================
# CHƯƠNG TRÌNH MÔ PHỎNG THUẬT TOÁN LẬP LỊCH ĐỘ ƯU TIÊN (PRIORITY - NON-PREEMPTIVE)
# =============================================================================

# Bước 1: Thiết lập dữ liệu đầu vào (Input Data)
# Mỗi danh sách con bao gồm: [Tên tiến trình, Thời điểm đến, Thời gian thực thi, Độ ưu tiên]
# Quy tắc vàng: Số Priority nhỏ hơn đồng nghĩa với việc "ưu tiên cao hơn".
processes = [["P1", 0, 5, 3], ["P2", 1, 3, 1], ["P3", 2, 2, 4], ["P4", 3, 4, 2]]

# Lưu lại số lượng tiến trình để kiểm soát vòng lặp (trong bài này n = 4)
n = len(processes)

# ==========================================
# GIAI ĐOẠN 1: KHỞI TẠO CÁC CẤU TRÚC DỮ LIỆU
# ==========================================

# Chúng ta cần các mảng (máy tính gọi là List) để ghi chép lại kết quả tính toán cho từng tiến trình
finish_time = [0] * n  # Ghi lại: "Lúc nào thì anh xong việc?"
tat = [0] * n  # Turnaround Time: "Anh đã ở trong hệ thống tổng cộng bao lâu?"
wt = [0] * n  # Waiting Time: "Thực tế anh đã phải đứng đợi mất bao lâu?"

# Mảng cờ hiệu (is_completed): Để đánh dấu những ai đã được CPU xử lý xong, tránh chạy lại.
is_completed = [False] * n

# Biến điều phối hệ thống quan trọng nhất:
current_time = 0  # Đây là "kim đồng hồ" của CPU, bắt đầu từ giây thứ 0.
completed_count = (
    0  # Bộ đếm tiến độ: Khi nào hoàn thành đủ n tiến trình thì dừng chương trình.
)

# Các biến hỗ trợ việc vẽ biểu đồ Gantt sau này
gantt_names = []  # Lưu tên các tiến trình theo thứ tự được chọn chạy
gantt_times = [0]  # Lưu các mốc thời gian chuyển đổi trên biểu đồ

# ==========================================
# GIAI ĐOẠN 2: TIẾN TRÌNH XỬ LÝ CHÍNH
# ==========================================

# Vòng lặp sẽ chạy liên tục cho đến khi mọi tiến trình đều được đánh dấu là 'True' trong is_completed
while completed_count < n:

    # 2.1. Lọc danh sách tiến trình đang chờ (Ready Queue)
    # Tại thời điểm hiện tại (current_time), những ai đã đến nơi và chưa được chạy?
    available = []
    for i in range(n):
        if processes[i][1] <= current_time and not is_completed[i]:
            available.append(i)

    # Nếu tại thời điểm này chưa có ai đến, CPU sẽ "ngồi không" (Idle)
    # Chúng ta phải tăng đồng hồ lên để chờ người tiếp theo đến.
    if not available:
        current_time += 1
        continue

    # 2.2. Chiến lược lựa chọn (Selection Strategy)
    # Trong các tiến trình đang chờ (available), ta tìm người có Priority nhỏ nhất.
    selected_index = available[0]
    for i in available:
        # So sánh Priority: Số nhỏ hơn thắng.
        if processes[i][3] < processes[selected_index][3]:
            selected_index = i
        # Trường hợp "Hòa" độ ưu tiên: Ai đến trước (Arrival Time nhỏ hơn) thì ưu tiên trước.
        elif processes[i][3] == processes[selected_index][3]:
            if processes[i][1] < processes[selected_index][1]:
                selected_index = i

    # Lấy thông tin của người "thắng cuộc" để bắt đầu thực thi
    name = processes[selected_index][0]
    arrival = processes[selected_index][1]
    burst = processes[selected_index][2]

    # Thông báo trạng thái hoạt động của CPU
    print(f"Tại T = {current_time} -> Xếp {name} vào chạy...")

    # 2.3. Chiếm dụng CPU (Execution)
    # Vì là "Độc quyền", CPU sẽ tập trung chạy hết thời gian Burst Time mà không bị ngắt quãng.
    current_time += (
        burst  # Cập nhật kim đồng hồ nhảy đến thời điểm kết thúc của tiến trình này.
    )

    # Ghi nhận dữ liệu để vẽ biểu đồ Gantt
    gantt_names.append(name)
    gantt_times.append(current_time)

    # 2.4. Tính toán các chỉ số thống kê (Calculation)
    finish_time[selected_index] = current_time  # Thời điểm hoàn tất
    tat[selected_index] = (
        finish_time[selected_index] - arrival
    )  # Công thức TAT = Finish - Arrival
    wt[selected_index] = tat[selected_index] - burst  # Công thức WT = TAT - Burst

    # Cuối cùng, đánh dấu hoàn tất và tăng bộ đếm tổng
    is_completed[selected_index] = True
    completed_count += 1

# ==========================================
# GIAI ĐOẠN 3: XUẤT KẾT QUẢ VÀ TỔNG KẾT
# ==========================================

# Vẽ biểu đồ Gantt trực quan để người xem dễ hình dung dòng thời gian
print("\n--- BIỂU ĐỒ GANTT ---")
gantt_string = str(gantt_times[0])
for i in range(len(gantt_names)):
    gantt_string += f" ---[{gantt_names[i]}]---> {gantt_times[i+1]}"
print(gantt_string)

# In bảng kết quả chi tiết từng tiến trình
print("\n--- BẢNG KẾT QUẢ ---")
print("Process\tArrival\tBurst\tPriority\tFinish\tTAT\tWT")
total_tat = 0
total_wt = 0

for i in range(n):
    total_tat += tat[i]
    total_wt += wt[i]
    print(
        f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{processes[i][3]}\t\t{finish_time[i]}\t{tat[i]}\t{wt[i]}"
    )

# Tính toán hiệu suất trung bình của hệ thống
print("\n--- TỔNG KẾT HIỆU SUẤT ---")
print(f"Avg TAT (Thời gian lưu hệ thống trung bình): {total_tat/n}")
print(f"Avg WT (Thời gian chờ trung bình): {total_wt/n}")
