class Taikhoan:
    def __init__(self, Sotaikhoan= "", ten = " ", Sodu = 0,loai =""):
        if loai not in ('T', 'C'):
            loai = 'T'
        self.loai = loai 
        self.__ten = ten
        self.__Sodu = Sodu
        self.__Sotaikhoan = Sotaikhoan
        
    def get_ten(self):
        return self.__ten   
    def set_ten(self, ten):
        self.__ten = ten
        
    def get_Sotaikhoan(self):
        return self.__Sotaikhoan
    def set_Sotaikhoan(self, Sotaikhoan):
        self.__Sotaikhoan = Sotaikhoan
    
    def get_Sodu(self):
        return self.__Sodu   
    def set_Sodu(self, Sodu):
        self.__Sodu = Sodu 
            
    # def xuat_tt(self):
    #     print(f"""
    # Số tài khoản: {self.get_Sotaikhoan()} 
    # Tên: {self.get_ten()}
    # Loại tài khoản: {self.loai}
    # Số dư: {self.get_Sodu():,} VND
    # """)
    
    def xuat_tt_dang_bang(self):
        
        print(f" | {self.get_Sotaikhoan():^15} | {self.get_ten():^20} | {self.loai:^5} | {self.get_Sodu():^30,}VND  | ")