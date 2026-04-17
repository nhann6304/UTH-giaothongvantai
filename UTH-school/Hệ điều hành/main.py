# =============================================================================
# CHƯƠNG TRÌNH MÔ PHỎNG THUẬT TOÁN LẬP LỊCH ĐỘ ƯU TIÊN (PRIORITY - NON-PREEMPTIVE)
# =============================================================================

# Thiết lập danh sách các tiến trình đầu vào.
# Cấu trúc dữ liệu: [Tên tiến trình, Thời điểm đến (Arrival), Thời gian thực thi (Burst), Độ ưu tiên]
# Quy ước: Giá trị Priority thấp tương ứng với mức độ ưu tiên cao.
processes = [["P1", 0, 5, 3], ["P2", 1, 3, 1], ["P3", 2, 2, 4], ["P4", 3, 4, 2]]

# Xác định tổng số lượng tiến trình trong hệ thống
n = len(processes)

# =============================================================================
# KHỞI TẠO CÁC BIẾN VÀ MẢNG LƯU TRỮ KẾT QUẢ
# =============================================================================

# Khởi tạo các mảng lưu trữ thông số sau khi thực thi
finish_time = [0] * n  # Thời điểm hoàn thành thực thi
tat = [0] * n  # Turnaround Time (Thời gian hoàn thành - Thời điểm đến)
wt = [0] * n  # Waiting Time (Thời gian lưu lại hệ thống - Thời gian thực thi)

# Sử dụng mảng boolean để quản lý trạng thái thực thi của từng tiến trình
is_completed = [False] * n

# Các biến điều khiển tiến độ hệ thống
current_time = 0  # Đồng hồ hệ thống (biến thời gian thực hiện tại)
completed_count = 0  # Số lượng tiến trình đã hoàn tất xử lý

# Khởi tạo dữ liệu phục vụ việc xây dựng biểu đồ Gantt
gantt_names = []
gantt_times = [0]

# =============================================================================
# THỰC THI THUẬT TOÁN (CORE LOGIC)
# =============================================================================

# Vòng lặp chính được duy trì cho đến khi tất cả tiến trình đều được xử lý thành công
while completed_count < n:

    # Bước 1: Xác định các tiến trình đã gia nhập hàng đợi sẵn sàng (Ready Queue)
    # Điều kiện: Thời điểm đến <= Thời gian hiện tại và chưa hoàn thành thực thi
    available = []
    for i in range(n):
        if processes[i][1] <= current_time and not is_completed[i]:
            available.append(i)

    # Trường hợp Ready Queue trống: CPU rơi vào trạng thái nhàn rỗi (Idle)
    # Hệ thống tự động tăng thời gian cho đến khi có tiến trình mới gia nhập
    if not available:
        current_time += 1
        continue

    # Bước 2: Lựa chọn tiến trình có độ ưu tiên cao nhất trong hàng đợi
    selected_index = available[0]
    for i in available:
        # Ưu tiên tiến trình có chỉ số Priority thấp nhất
        if processes[i][3] < processes[selected_index][3]:
            selected_index = i
        # Trường hợp đồng mức ưu tiên: Áp dụng quy tắc FCFS (Tiến trình đến trước được chọn)
        elif processes[i][3] == processes[selected_index][3]:
            if processes[i][1] < processes[selected_index][1]:
                selected_index = i

    # Truy xuất thông tin của tiến trình được lựa chọn
    name = processes[selected_index][0]
    arrival = processes[selected_index][1]
    burst = processes[selected_index][2]

    # Ghi nhận trạng thái chuyển giao quyền kiểm soát CPU
    print(f"Thời điểm T = {current_time}: Tiến trình {name} bắt đầu thực thi.")

    # Bước 3: Thực thi tiến trình theo cơ chế không độc quyền (Non-preemptive)
    # Tiến trình sẽ chiếm dụng CPU cho đến khi hoàn thành toàn bộ Burst Time
    current_time += burst

    # Cập nhật dữ liệu cho biểu đồ Gantt sau mỗi chu kỳ thực thi
    gantt_names.append(name)
    gantt_times.append(current_time)

    # Bước 4: Tính toán các thông số hiệu năng cho tiến trình vừa hoàn tất
    finish_time[selected_index] = current_time  # Thời điểm kết thúc
    tat[selected_index] = finish_time[selected_index] - arrival  # Turnaround Time
    wt[selected_index] = tat[selected_index] - burst  # Waiting Time

    # Cập nhật trạng thái hoàn thành và tăng bộ đếm hệ thống
    is_completed[selected_index] = True
    completed_count += 1

# =============================================================================
# TRÌNH BÀY KẾT QUẢ VÀ THỐNG KÊ
# =============================================================================

# Hiển thị trực quan trình tự thực thi thông qua biểu đồ Gantt
print("\n--- BIỂU ĐỒ GANTT ---")
gantt_output = str(gantt_times[0])
for i in range(len(gantt_names)):
    gantt_output += f" ---[{gantt_names[i]}]---> {gantt_times[i+1]}"
print(gantt_output)

# Xuất bảng thống kê chi tiết các chỉ số của từng tiến trình
print("\n--- BẢNG KẾT QUẢ CHI TIẾT ---")
print("Process\tArrival\tBurst\tPriority\tFinish\tTAT\tWT")
total_tat = 0
total_wt = 0

for i in range(n):
    total_tat += tat[i]
    total_wt += wt[i]
    print(
        f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{processes[i][3]}\t\t{finish_time[i]}\t{tat[i]}\t{wt[i]}"
    )

# Tổng kết các giá trị trung bình để đánh giá hiệu suất thuật toán
print("\n--- TỔNG KẾT HIỆU SUẤT HỆ THỐNG ---")
print(f"Thời gian lưu lại hệ thống trung bình (Avg TAT): {total_tat/n}")
print(f"Thời gian chờ trung bình (Avg WT): {total_wt/n}")
