import heapq  # Thư viện hàng đợi ưu tiên (Priority Queue)


def dijkstra(graph, start_node):
    distances = {node: float("infinity") for node in graph}
    distances[start_node] = 0

    # Hàng đợi ưu tiên: Luôn lưu cặp (khoảng_cách, tên_đỉnh)
    priority_queue = [(0, start_node)]

    print(f"🚀 Bắt đầu tìm đường từ: {start_node}\n")

    while priority_queue:
        # 2. LẤY RA (POP)
        # Lấy đỉnh có khoảng cách nhỏ nhất hiện tại trong hàng chờ
        current_dist, current_node = heapq.heappop(priority_queue)

        # 3. KIỂM TRA "RÁC" (LAZY DELETION)
        # Nếu khoảng cách vừa lấy ra > khoảng cách đã lưu trong bảng -> Bỏ qua
        # (Đây là trường hợp đỉnh B có giá trị 4 cũ kỹ mà mình nói ở trên)
        if current_dist > distances[current_node]:
            continue

        print(f"🔹 Đang xét đỉnh {current_node} (Khoảng cách tích lũy: {current_dist})")

        # 4. DUYỆT CÁC ĐỈNH KỀ
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight

            # 5. NỚI LỎNG (RELAXATION)
            # Nếu tìm thấy đường đi mới ngắn hơn đường cũ
            if distance < distances[neighbor]:
                print(
                    f"   -> Cập nhật {neighbor}: Giảm từ {distances[neighbor]} xuống {distance}"
                )
                distances[neighbor] = distance

                # 6. ĐẨY VÀO (PUSH)
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


my_graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2, "F": 6},
    "E": {"C": 10, "D": 2, "F": 3},
    "F": {"D": 6, "E": 3},
}

# --- CHẠY THỬ ---
ket_qua = dijkstra(my_graph, "A")

print("\n" + "=" * 30)
print("🏁 KẾT QUẢ ĐƯỜNG ĐI NGẮN NHẤT TỪ A:")
for node, dist in ket_qua.items():
    print(f"Đến {node}: {dist}")
