# quy tat dat ten
# 1__ Là chữ
# 2__ Là số
# 3__ Là dấu gạch dưới
# ==Lưu ý:
#  Không được bắt đầu bằng số
print("========================Câu1 ===========================")

pi = 3.14159
diameter = 3

radius = diameter / 2

area = pi * (radius**2)

print("Diện tích hình tròn là:", area)

print("========================Câu 2 ===========================")


message = """Then he said "I don't know.\""""

print(message)

print("========================Câu 3 ===========================")

a = "+"
b = "-"

s = (a + b) * 22 + a

print(s)
print("========================Câu 4 ===========================")

start_hour = 6
start_min = 52
start_sec = 0
# 1km trung bình (8p 15s) + 3km nhanh (7p 12s) + 1km trung bình (8p 15s)
total_seconds = (8 * 60 + 15) + 3 * (7 * 60 + 12) + (8 * 60 + 15)

#  tổng giây ra phút và giây dư
total_minutes = total_seconds // 60
rem_seconds = total_seconds % 60

# Cộng vào thời gian bắt đầu
end_min = start_min + total_minutes
end_hour = start_hour + (end_min // 60)
end_min = end_min % 60

print(f"Tôi về đến nhà lúc: {end_hour:02d}:{end_min:02d}:{rem_seconds:02d} am")

# print("========================Câu 5 ===========================")
purchaseAmount = eval(input("Enter purchase amount: "))
tax = purchaseAmount * 0.06

phan_nguyen = int(tax)

phan_thap_phan = int((tax * 100) - (phan_nguyen * 100) + 0.00001)

s_nguyen = str(phan_nguyen)
s_thap_phan = str(phan_thap_phan)


ket_qua = s_nguyen + "." + s_thap_phan

print("Sales tax is " + ket_qua)
