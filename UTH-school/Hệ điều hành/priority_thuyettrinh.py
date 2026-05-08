# =============================================================================
# CHƯƠNG TRÌNH MÔ PHỎNG THUẬT TOÁN PRIORITY SCHEDULING (NON-PREEMPTIVE)
# Phiên bản có chú thích chi tiết — dùng để THUYẾT TRÌNH
# Mỗi dòng comment được viết như văn nói, đọc lên là trở thành lời thuyết trình
# =============================================================================


# Kính thưa thầy cô và các bạn, hôm nay nhóm em xin trình bày chương trình
# mô phỏng thuật toán lập lịch CPU theo độ ưu tiên không chiếm quyền,
# tên tiếng Anh là Priority Scheduling Non-Preemptive.
# Chương trình được chia thành ba hàm chính: hàm nhập dữ liệu, hàm chạy thuật toán,
# và hàm in báo cáo kết quả. Em xin bắt đầu với hàm thứ nhất.


# =============================================================================
# HÀM 1: NHẬP DỮ LIỆU TIẾN TRÌNH TỪ BÀN PHÍM
# =============================================================================
# Hàm nhap_tien_trinh có nhiệm vụ hỏi người dùng nhập số lượng tiến trình,
# sau đó nhập thông tin chi tiết cho từng tiến trình một cách lần lượt.
def nhap_tien_trinh():
    # Em sử dụng vòng lặp while True để đảm bảo người dùng phải nhập đúng định dạng,
    # nếu nhập sai chương trình sẽ hỏi lại liên tục cho đến khi hợp lệ thì thôi.
    while True:
        # Khối try-except dùng để bắt lỗi khi người dùng gõ chữ thay vì số nguyên.
        try:
            # Hàm input trả về một chuỗi ký tự, em dùng hàm int để chuyển nó thành số nguyên.
            # Đây chính là số lượng tiến trình mà người dùng muốn mô phỏng trong lần chạy này.
            n = int(input("Nhập số lượng tiến trình: "))
            # Em kiểm tra số tiến trình phải lớn hơn 0, vì không thể có 0 hoặc âm tiến trình.
            if n <= 0:
                # Nếu nhập sai, em in thông báo lỗi và dùng continue để hỏi lại.
                print("Số tiến trình phải lớn hơn 0. Vui lòng nhập lại.\n")
                continue
            # Khi nhập hợp lệ rồi, em dùng break để thoát khỏi vòng lặp này.
            break
        except ValueError:
            # ValueError xảy ra khi người dùng gõ ký tự không phải số, ví dụ chữ "abc".
            # Em bắt lỗi này để chương trình không bị dừng đột ngột giữa chừng.
            print("Giá trị không hợp lệ, vui lòng nhập số nguyên.\n")

    # Em khởi tạo một danh sách rỗng để chứa toàn bộ các tiến trình sắp được nhập.
    processes = []

    # Bây giờ em dùng vòng lặp for để hỏi thông tin cho từng tiến trình một,
    # bắt đầu từ tiến trình P1, P2, cho đến Pn theo đúng thứ tự.
    for i in range(n):
        # Em in ra một dòng tiêu đề để người dùng biết đang nhập cho tiến trình nào.
        print(f"\n--- Nhập thông tin cho tiến trình P{i+1} ---")
        # Em tiếp tục dùng while True để bắt lỗi nhập liệu cho riêng từng tiến trình.
        while True:
            try:
                # Đầu tiên em hỏi thời điểm đến, tức là lúc nào tiến trình này xuất hiện trong hệ thống.
                arrival = int(input(f"  Thời điểm đến (Arrival Time) của P{i+1}: "))
                # Tiếp theo em hỏi burst time, tức là thời gian CPU cần xử lý xong tiến trình này.
                burst = int(input(f"  Thời gian thực thi (Burst Time) của P{i+1}: "))
                # Cuối cùng là độ ưu tiên, em xin lưu ý quy ước là số càng nhỏ thì ưu tiên càng cao.
                priority = int(
                    input(f"  Độ ưu tiên (Priority, số nhỏ = ưu tiên cao) của P{i+1}: ")
                )

                # Em ràng buộc rằng arrival không được âm và burst phải lớn hơn 0,
                # vì không có tiến trình nào đến vào thời điểm âm hay chạy 0 giây cả.
                if burst <= 0 or arrival < 0:
                    # Nếu sai ràng buộc, em in lỗi và quay lại hỏi cả 3 giá trị từ đầu cho P này.
                    print("  Arrival >= 0 và Burst > 0. Vui lòng nhập lại.")
                    continue
                # Khi cả ba giá trị đều hợp lệ, em thoát khỏi vòng lặp con này.
                break
            except ValueError:
                # Em bắt lỗi nếu người dùng gõ chữ thay vì số nguyên cho một trong ba trường.
                print("  Giá trị không hợp lệ, vui lòng nhập số nguyên.")

        # Sau khi nhập hợp lệ, em thêm tiến trình này vào danh sách processes,
        # mỗi tiến trình lưu dưới dạng [Tên, Arrival Time, Burst Time, Priority].
        processes.append([f"P{i+1}", arrival, burst, priority])

    # Cuối cùng, hàm trả về toàn bộ danh sách tiến trình ra ngoài cho hàm gọi sử dụng.
    return processes


# =============================================================================
# HÀM 2: CHẠY THUẬT TOÁN PRIORITY SCHEDULING (NON-PREEMPTIVE)
# Đầu vào: processes = [[Tên, Arrival, Burst, Priority], ...]
# =============================================================================
# Đây là phần quan trọng nhất của chương trình, em xin trình bày kỹ.
# Hàm này nhận vào danh sách tiến trình và mô phỏng quá trình CPU xử lý từng tiến trình.
def chay_priority_scheduling(processes):
    # Em lấy số lượng tiến trình bằng hàm len, dùng làm điều kiện dừng cho vòng lặp chính.
    n = len(processes)

    # ==========================================
    # GIAI ĐOẠN 1: KHỞI TẠO CẤU TRÚC DỮ LIỆU
    # ==========================================
    # Em khởi tạo ba mảng kết quả, mỗi mảng có n phần tử và đều bằng 0 ở thời điểm ban đầu.

    # Mảng finish_time lưu thời điểm hoàn thành xong việc của từng tiến trình.
    finish_time = [0] * n
    # Mảng tat lưu Turnaround Time, tức tổng thời gian tiến trình lưu lại trong hệ thống.
    tat = [0] * n
    # Mảng wt lưu Waiting Time, tức thời gian tiến trình phải chờ đợi trong hàng đợi.
    wt = [0] * n

    # Em dùng mảng cờ is_completed để đánh dấu tiến trình nào đã chạy xong.
    # Ban đầu tất cả phần tử đều là False, nghĩa là chưa có tiến trình nào hoàn thành.
    is_completed = [False] * n

    # Biến current_time đóng vai trò như "đồng hồ CPU", luôn bắt đầu từ thời điểm 0.
    current_time = 0
    # Biến completed_count đếm số tiến trình đã hoàn thành, dùng để dừng vòng lặp khi đủ n.
    completed_count = 0

    # Hai mảng sau đây phục vụ cho việc vẽ biểu đồ Gantt ở phần in kết quả.
    # gantt_names lưu thứ tự tên tiến trình theo lúc CPU thực thi nó.
    gantt_names = []
    # gantt_times lưu các mốc thời gian chuyển đổi, mặc định bắt đầu từ 0.
    gantt_times = [0]

    # ==========================================
    # GIAI ĐOẠN 2: VÒNG LẶP MÔ PHỎNG CHÍNH
    # ==========================================
    # Em dùng vòng lặp while và lặp cho đến khi tất cả n tiến trình đều đã hoàn thành.
    while completed_count < n:

        # 2.1. Em tìm tất cả các tiến trình đã đến và chưa chạy xong.
        # Đây chính là hàng đợi sẵn sàng, tiếng Anh gọi là Ready Queue.
        available = []
        # Em duyệt qua từng tiến trình trong danh sách processes.
        for i in range(n):
            # Điều kiện 1: thời điểm đến nhỏ hơn hoặc bằng đồng hồ hiện tại.
            # Điều kiện 2: tiến trình đó chưa được đánh dấu là đã hoàn thành.
            if processes[i][1] <= current_time and not is_completed[i]:
                # Nếu cả hai điều kiện đều thỏa mãn, em thêm chỉ số i vào danh sách available.
                available.append(i)

        # Trường hợp đặc biệt: nếu hàng đợi rỗng nghĩa là CPU đang ngồi không, gọi là IDLE.
        # Em chỉ cần tăng đồng hồ lên 1 đơn vị thời gian và thử lại ở vòng sau.
        if not available:
            current_time += 1
            continue

        # 2.2. Trong hàng đợi sẵn sàng, em chọn tiến trình có độ ưu tiên cao nhất.
        # Cụ thể là tiến trình có giá trị Priority nhỏ nhất theo quy ước.
        # Em giả sử người thắng tạm thời là phần tử đầu tiên trong available.
        selected_index = available[0]
        # Em duyệt qua từng tiến trình trong available để so sánh và tìm người thắng cuối cùng.
        for i in available:
            # Nếu tiến trình i có priority nhỏ hơn người đang giữ ngôi đầu,
            # thì i sẽ trở thành người thắng mới.
            if processes[i][3] < processes[selected_index][3]:
                selected_index = i
            # Trường hợp hai tiến trình có priority bằng nhau,
            # em áp dụng quy tắc tie-break: ai đến sớm hơn thì thắng.
            elif processes[i][3] == processes[selected_index][3]:
                if processes[i][1] < processes[selected_index][1]:
                    selected_index = i

        # Em rút thông tin của tiến trình vừa được chọn ra ba biến tạm cho dễ dùng bên dưới.
        name = processes[selected_index][0]
        arrival = processes[selected_index][1]
        burst = processes[selected_index][2]

        # Em in một dòng log trực quan để người xem theo dõi tiến trình nào đang chạy.
        print(f"Thời điểm T = {current_time}: Tiến trình {name} bắt đầu thực thi.")

        # 2.3. Bây giờ em thực thi tiến trình đã chọn.
        # Vì đây là phiên bản KHÔNG CHIẾM QUYỀN, nên tiến trình sẽ chiếm CPU suốt burst time,
        # không bị bất kỳ tiến trình nào khác cướp giữa chừng.
        # Đồng hồ nhảy thẳng đến thời điểm kết thúc bằng cách cộng thêm burst time.
        current_time += burst

        # Em ghi lại dữ liệu Gantt: tên tiến trình vừa chạy và mốc thời gian kết thúc của nó.
        gantt_names.append(name)
        gantt_times.append(current_time)

        # 2.4. Em tính ba chỉ số quan trọng cho tiến trình vừa chạy xong.
        # Thời điểm kết thúc chính là giá trị đồng hồ hiện tại sau khi đã cộng burst.
        finish_time[selected_index] = current_time
        # Turnaround Time bằng thời điểm kết thúc trừ đi thời điểm đến.
        tat[selected_index] = finish_time[selected_index] - arrival
        # Waiting Time bằng Turnaround Time trừ đi Burst Time.
        wt[selected_index] = tat[selected_index] - burst

        # Em đánh dấu tiến trình này đã hoàn thành để các vòng lặp sau bỏ qua nó.
        is_completed[selected_index] = True
        # Tăng bộ đếm hoàn thành lên một, khi nào bằng n thì kết thúc thuật toán.
        completed_count += 1

    # Sau khi vòng lặp kết thúc, hàm trả về năm mảng kết quả cho hàm in báo cáo sử dụng.
    return finish_time, tat, wt, gantt_names, gantt_times


# =============================================================================
# HÀM 3: IN BÁO CÁO KẾT QUẢ RA MÀN HÌNH
# =============================================================================
# Hàm này nhận đầy đủ kết quả từ thuật toán và trình bày dưới ba phần:
# biểu đồ Gantt, bảng kết quả chi tiết, và tổng kết hiệu suất hệ thống.
def in_ket_qua(processes, finish_time, tat, wt, gantt_names, gantt_times):
    # Em lấy số lượng tiến trình để dùng cho việc tính trung bình ở phần cuối.
    n = len(processes)

    # ==========================================
    # PHẦN 1: VẼ BIỂU ĐỒ GANTT DẠNG VĂN BẢN
    # ==========================================
    # Em in tiêu đề của phần Gantt trước.
    print("\n--- BIỂU ĐỒ GANTT ---")

    # Em bắt đầu chuỗi output bằng mốc thời gian đầu tiên, luôn luôn là 0.
    gantt_output = str(gantt_times[0])

    # Em ghép thêm từng đoạn theo định dạng "---[Tên]---> Mốc" cho từng tiến trình đã chạy.
    for i in range(len(gantt_names)):
        gantt_output += f" ---[{gantt_names[i]}]---> {gantt_times[i+1]}"
    # Em in chuỗi Gantt đã ghép hoàn chỉnh ra màn hình.
    print(gantt_output)

    # ==========================================
    # PHẦN 2: BẢNG KẾT QUẢ CHI TIẾT
    # ==========================================
    # Em in tiêu đề của phần bảng kết quả.
    print("\n--- BẢNG KẾT QUẢ CHI TIẾT ---")
    # Em in dòng tiêu đề cột, em dùng ký tự \t là tab để canh các cột cho thẳng hàng.
    print("Process\tArrival\tBurst\tPriority\tFinish\tTAT\tWT")

    # Hai biến này dùng để cộng dồn TAT và WT, phục vụ cho việc tính trung bình ở phần sau.
    total_tat = 0
    total_wt = 0

    # Em duyệt qua từng tiến trình theo thứ tự nhập ban đầu, tức là P1, P2, cho đến Pn.
    for i in range(n):
        # Cộng dồn giá trị TAT của tiến trình thứ i vào tổng.
        total_tat += tat[i]
        # Cộng dồn giá trị WT của tiến trình thứ i vào tổng.
        total_wt += wt[i]
        # Em in một dòng cho tiến trình thứ i với đầy đủ bảy trường thông tin.
        print(
            f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{processes[i][3]}\t\t{finish_time[i]}\t{tat[i]}\t{wt[i]}"
        )

    # ==========================================
    # PHẦN 3: TỔNG KẾT HIỆU SUẤT HỆ THỐNG
    # ==========================================
    # Em in tiêu đề của phần tổng kết.
    print("\n--- TỔNG KẾT HIỆU SUẤT HỆ THỐNG ---")
    # Avg TAT cho biết trung bình mỗi tiến trình lưu lại trong hệ thống bao nhiêu đơn vị thời gian.
    print(f"Thời gian lưu lại hệ thống trung bình (Avg TAT): {total_tat/n}")
    # Avg WT cho biết trung bình mỗi tiến trình phải chờ CPU bao nhiêu đơn vị thời gian.
    print(f"Thời gian chờ trung bình (Avg WT): {total_wt/n}")


# =============================================================================
# KHỐI THỰC THI CHÍNH — chỉ chạy khi file này được chạy trực tiếp, không phải import
# =============================================================================
# Câu lệnh if __name__ == "__main__" đảm bảo khối này chỉ chạy khi ta gõ "python file.py",
# nếu file bị import vào file khác thì khối này sẽ không tự động chạy.
if __name__ == "__main__":
    # Em in một dòng tiêu đề để người dùng biết đang chạy thuật toán nào.
    print("=== THUẬT TOÁN PRIORITY SCHEDULING (Non-Preemptive) ===\n")

    # Bước 1: gọi hàm nhập dữ liệu để lấy danh sách tiến trình từ người dùng.
    processes = nhap_tien_trinh()

    # Bước 2: chạy thuật toán Priority và nhận về năm mảng kết quả thông qua unpacking tuple.
    finish_time, tat, wt, gantt_names, gantt_times = chay_priority_scheduling(processes)

    # Bước 3: gọi hàm in kết quả để hiển thị Gantt, bảng chi tiết và trung bình ra màn hình.
    in_ket_qua(processes, finish_time, tat, wt, gantt_names, gantt_times)

    # Đến đây là kết thúc chương trình. Em xin cảm ơn thầy cô và các bạn đã lắng nghe.
