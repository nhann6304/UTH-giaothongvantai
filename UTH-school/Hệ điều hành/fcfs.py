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
                if burst <= 0 or arrival < 0:
                    print("  Arrival >= 0 và Burst > 0. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("  Giá trị không hợp lệ, vui lòng nhập số nguyên.")

        processes.append([f"P{i+1}", arrival, burst])

    return processes


def chay_fcfs(processes):
    n = len(processes)

    order = sorted(range(n), key=lambda i: (processes[i][1], i))

    finish_time = [0] * n
    tat = [0] * n
    wt = [0] * n

    current_time = 0
    gantt_names = []
    gantt_times = [0]

    for idx in order:
        name = processes[idx][0]
        arrival = processes[idx][1]
        burst = processes[idx][2]

        if current_time < arrival:
            print(f"Thời điểm T = {current_time}: CPU rảnh (IDLE) đến T = {arrival}.")
            gantt_names.append("IDLE")
            gantt_times.append(arrival)
            current_time = arrival

        print(f"Thời điểm T = {current_time}: Tiến trình {name} bắt đầu thực thi.")

        current_time += burst
        gantt_names.append(name)
        gantt_times.append(current_time)

        finish_time[idx] = current_time
        tat[idx] = finish_time[idx] - arrival
        wt[idx] = tat[idx] - burst

    return finish_time, tat, wt, gantt_names, gantt_times


def in_ket_qua(processes, finish_time, tat, wt, gantt_names, gantt_times):
    n = len(processes)

    print("\n--- BIỂU ĐỒ GANTT ---")
    gantt_output = str(gantt_times[0])
    for i in range(len(gantt_names)):
        gantt_output += f" ---[{gantt_names[i]}]---> {gantt_times[i+1]}"
    print(gantt_output)

    print("\n--- BẢNG KẾT QUẢ CHI TIẾT ---")
    print("Process\tArrival\tBurst\tFinish\tTAT\tWT")
    total_tat = 0
    total_wt = 0

    for i in range(n):
        total_tat += tat[i]
        total_wt += wt[i]
        print(
            f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{finish_time[i]}\t{tat[i]}\t{wt[i]}"
        )

    print("\n--- TỔNG KẾT HIỆU SUẤT HỆ THỐNG ---")
    print(f"Thời gian lưu lại hệ thống trung bình (Avg TAT): {total_tat/n}")
    print(f"Thời gian chờ trung bình (Avg WT): {total_wt/n}")


if __name__ == "__main__":
    print("=== THUẬT TOÁN FCFS (First-Come, First-Served) ===\n")
    processes = nhap_tien_trinh()
    finish_time, tat, wt, gantt_names, gantt_times = chay_fcfs(processes)
    in_ket_qua(processes, finish_time, tat, wt, gantt_names, gantt_times)
