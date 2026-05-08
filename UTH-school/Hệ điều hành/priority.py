def nhap_tien_trinh():
    while True:
        try:
            n = int(input("Nhập số lượng tiến trình: "))
            if n <= 0:
                print("Số tiến trình phải lớn hơn 0. Vui lòng nhập lại.\n")
                continue
            break
        except ValueError:
            print("Giá trị không hợp lệ, vui lòng nhập số nguyên.\n")

    processes = []

    for i in range(n):
        print(f"\n--- Nhập thông tin cho tiến trình P{i+1} ---")
        while True:
            try:
                arrival = int(input(f"  Thời điểm đến (Arrival Time) của P{i+1}: "))
                burst = int(input(f"  Thời gian thực thi (Burst Time) của P{i+1}: "))
                priority = int(
                    input(f"  Độ ưu tiên (Priority, số nhỏ = ưu tiên cao) của P{i+1}: ")
                )

                if burst <= 0 or arrival < 0:
                    print("  Arrival >= 0 và Burst > 0. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("  Giá trị không hợp lệ, vui lòng nhập số nguyên.")

        processes.append([f"P{i+1}", arrival, burst, priority])

    return processes


def chay_priority_scheduling(processes):
    n = len(processes)

    finish_time = [0] * n
    tat = [0] * n
    wt = [0] * n

    is_completed = [False] * n

    current_time = 0
    completed_count = 0

    gantt_names = []
    gantt_times = [0]

    while completed_count < n:

        available = []
        for i in range(n):
            if processes[i][1] <= current_time and not is_completed[i]:
                available.append(i)

        if not available:
            current_time += 1
            continue

        selected_index = available[0]
        for i in available:
            if processes[i][3] < processes[selected_index][3]:
                selected_index = i
            elif processes[i][3] == processes[selected_index][3]:
                if processes[i][1] < processes[selected_index][1]:
                    selected_index = i

        name = processes[selected_index][0]
        arrival = processes[selected_index][1]
        burst = processes[selected_index][2]

        print(f"Thời điểm T = {current_time}: Tiến trình {name} bắt đầu thực thi.")

        current_time += burst

        gantt_names.append(name)
        gantt_times.append(current_time)

        finish_time[selected_index] = current_time
        tat[selected_index] = finish_time[selected_index] - arrival
        wt[selected_index] = tat[selected_index] - burst

        is_completed[selected_index] = True
        completed_count += 1

    return finish_time, tat, wt, gantt_names, gantt_times


def in_ket_qua(processes, finish_time, tat, wt, gantt_names, gantt_times):
    n = len(processes)

    print("\n--- BIỂU ĐỒ GANTT ---")

    gantt_output = str(gantt_times[0])

    for i in range(len(gantt_names)):
        gantt_output += f" ---[{gantt_names[i]}]---> {gantt_times[i+1]}"
    print(gantt_output)

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

    print("\n--- TỔNG KẾT HIỆU SUẤT HỆ THỐNG ---")
    print(f"Thời gian lưu lại hệ thống trung bình (Avg TAT): {total_tat/n}")
    print(f"Thời gian chờ trung bình (Avg WT): {total_wt/n}")


if __name__ == "__main__":
    print("=== THUẬT TOÁN PRIORITY SCHEDULING (Non-Preemptive) ===\n")

    processes = nhap_tien_trinh()

    finish_time, tat, wt, gantt_names, gantt_times = chay_priority_scheduling(processes)

    in_ket_qua(processes, finish_time, tat, wt, gantt_names, gantt_times)
