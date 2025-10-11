from lab4 import * # import cac chức năng của máy tính bỏ túi
class Maytinh:
    def __init__(self):
        self.chay = True
        
    def hien_menu(self):
        self.menu = {
            1: "Tính cộng trừ nhân chia",
            2: "Tính lũy thừa",
            3: "Tính căn bậc 2 ",
            4: "Tính hàm lượng giác",
            5: "Tính logarit",
            6: "Giải phương trình bậc 1",
            7: "Giải phương trình bậc 2",
            8: "Xem lịch sử sử dụng",
            9: "Xem đồng hồ",
            10: "Thoát chương trình"
        }
        print("="*24+"MENU CHƯƠNG TRÌNH"+"="*23)
        for self.key , self.value in self.menu.items():
            print(f"| {self.key} : {self.value} {(55 - len(self.value)) * ' '} |")
        print("="*64)
        
    def thuc_hien_chuc_nang(self):

        while True:
            try:
                self.lua_chon = int(input("Chọn chức năng chương trình 1-10:"))
                break
            except ValueError:
                print("Lựa chọn không hợp lệ")
        if self.lua_chon == 1:
            func_1()
            History.append("Phép tính cơ bản")
        if self.lua_chon == 2:
            func_2()
            History.append("Phép tính lũy thừa")
        if self.lua_chon == 3:
            func_3()
            History.append("Phép tính căn bậc 2")
        if self.lua_chon == 4:
            func_4()
            History.append("Phép tính hàm lượng giác")
        if self.lua_chon == 5:
            func_5()
            History.append("Phép tính logarit")
        if self.lua_chon == 6:
            func_6()
            History.append("Giải phương trình bậc 1")
        if self.lua_chon == 7:
            func_7()
            History.append("Giải phương trình bậc 2")
        if self.lua_chon == 8:
            func_8()
            History.append("Xem lịch sử chức năng")
        if self.lua_chon == 9:
            func_9()
            History.append("Xem thời gian hiện tại")
        if self.lua_chon == 10:
            print("Cảm ơn")
    
    def chay_ct(self):
        while self.chay:
            self.thuc_hien_chuc_nang()
            if self.lua_chon == 10:
                self.chay = False
            
            
            
        