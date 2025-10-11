import math
import time
History = []
def func_1():
    number_1 = float(input("Nhập số thứ nhất: "))
    number_2 = float(input("Nhập số thứ hai: "))
    sum_two_number = number_1 + number_2
    sub_two_number = number_1 - number_2
    mul_two_number = number_1 * number_2
    div_two_number = number_1 / number_2 
    operator = input("Nhập toán tử cần tính (+, -, *, /): ")
    if operator == "+":
            print("Cộng 2 số: %d + %d = %.2f " % (number_1, number_2, sum_two_number))
    elif operator == "-":
            print("Trừ 2 số: %d - %d = %.2f " % (number_1, number_2, sub_two_number))
    elif operator == "*":
            print("Nhân 2 số: %d * %d = %.2f " % (number_1, number_2, mul_two_number))
    elif operator == "/":
        if number_2 != 0:
            print("Chia 2 số: %d / %d = %.2f " % (number_1, number_2, div_two_number))
        else:
            print("Lỗi! Không thể chia cho 0")
            
def func_2():
    base_number = float(input("Nhập số cần tính lũy thừa: "))
    exponent_number = float(input("Nhập số mũ: "))
    print("%d mũ %d = %.2f" % (base_number, exponent_number, math.pow(base_number, exponent_number)))
    
def func_3():
    number_3 = float(input("Nhập số cần tính căn bậc 2: "))
    if number_3 < 0:
        print("Lỗi! Không thể tính căn bậc 2 của số âm")
    else:
        print("Căn bậc 2 của %.2f là: %.2f" % (number_3, math.sqrt(number_3)))
        
def func_4():
    trig_funtion = input("Nhập hàm lượng giác cần tính (sin, cos, tan): ")
    if trig_funtion.lower() == "sin":
        number_x = float(input("Nhập góc x (độ): "))
        rad_number_x = math.radians(number_x) # Đổi độ sang radian
        print("sin(%.2f) = %.2f" % (number_x, math.sin(rad_number_x)))
    elif trig_funtion.lower() == "cos":
        number_x = float(input("Nhập góc x (độ): "))
        rad_number_x = math.radians(number_x) # Đổi độ sang radian
        print("cos(%.2f) = %.2f" % (number_x, math.cos(rad_number_x)))
    elif  trig_funtion.lower() == "tan":
        number_x = float(input("Nhập góc x (độ): "))
        rad_number_x = math.radians(number_x) # Đổi độ sang radian
        if math.cos(rad_number_x) == 0:
                print("Lỗi! Không thể tính tan của góc này")
        else:
                print("tan(%.2f) = %.2f" % (number_x, math.tan(rad_number_x)))
                
def func_5():
    log_number = float(input("Nhập số cần tính logarit: "))
    if log_number <= 0:
        print("Lỗi! Không thể tính logarit của số âm hoặc số 0")
    else:
        print("log(%.2f) = %.2f" % (log_number, math.log10(log_number)))
        
def func_6():
    He_so_bac_1 = int(input("Nhập hệ số a: "))
    He_so_tu_do = int(input("Nhập hệ số b: "))
    print("Phương trình đã cho: ", He_so_bac_1, "x +", He_so_tu_do, "= 0")
    if He_so_bac_1 == 0:
        if He_so_tu_do == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        Nghiem_pt = -He_so_tu_do / He_so_bac_1
        print("Nghiệm của phương trình là: x =", Nghiem_pt)
        
def func_7():
    He_so_bac_2 = float(input("Nhập hệ số a: "))
    He_so_bac_1 = float(input("Nhập hệ số b: "))
    He_so_tu_do = float(input("Nhập hệ số c: "))
    delta = He_so_bac_1 ** 2 - 4 * He_so_bac_2 * He_so_tu_do
    print("Phương trình đã cho: ", He_so_bac_2, "x^2 +", He_so_bac_1, "x +", He_so_tu_do, "= 0")
    if He_so_bac_2 == 0:
        if He_so_bac_1 == 0:
            if He_so_tu_do == 0:
                print("Phương trình vô số nghiệm")
            else:
                print("Phương trình vô nghiệm")
        else:
            Nghiem_pt = round((-He_so_tu_do / He_so_bac_1),1)
            print("Phương trình bậc nhất, nghiệm là: x =", Nghiem_pt)
    else:
        if delta < 0:
            print("Delta:", delta)
            print("Phương trình vô nghiệm")
        elif delta == 0:
            Nghiem_pt = round((-He_so_bac_1 / (2 * He_so_bac_2)),1) # Làm tròn 1 chữ số thập phân
            print("Phương trình có nghiệm kép: x =", Nghiem_pt)
        else:
            Nghiem_1 = round(((-He_so_bac_1 + math.sqrt(delta)) / (2 * He_so_bac_2)),1) 
            Nghiem_2 = round(((-He_so_bac_1 - math.sqrt(delta)) / (2 * He_so_bac_2)),1)
            print("Phương trình có hai nghiệm phân biệt:")
            print("x1 =", Nghiem_1)
            print("x2 =", Nghiem_2)
            
def func_8():
    if not History:
        print("Chưa có lịch sử")
    else:
        print("Lịch sử chức năng đã dùng")
        for i, func_name in enumerate (History, 1):
            print(f"{i}.{func_name}")

            
def func_9():
    n_time = time.time()
    local_time = time.localtime(n_time)
    Formatted = time.strftime(" %d/%m/%Y %H:%M:%S",local_time)
    print(f" Bây giờ là :{Formatted} ")