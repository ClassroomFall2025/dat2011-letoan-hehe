class Sanpham:
    def __init__(self, ten = "", gia = 0, giam_gia = 0):
        self.__ten = ten
        self.__gia = gia
        self.__giam_gia = giam_gia
        
    def get_ten_sp(self):
        return self.__ten
    
    def set_ten_sp(self,ten):
        self.__ten = ten
        
    def get_gia(self):
        return self.__gia
    
    def set_gia(self, gia):
        self.__gia = gia
        
    def set_giam_gia(self,giam_gia):
        self.__giam_gia = giam_gia
        
    def get_giam_gia(self):
        return self.__giam_gia
        
    
    def xuat_tt(self):
        print(f"""
        Tên sản phẩm: {self.get_ten_sp()}
        Gía: {self.get_gia()}
        Giảm giá: {self.get_giam_gia()}
        Thuế : {self.thue()}
        """)
    
    def thue(self):
        return int(self.get_gia() * 0.1)
    
    def nhap_tt(self):
        tensp = input("Nhập tên sản phẩm")
        self.set_ten_sp(tensp)
        gia = int(input("Nhập giá sản phẩm"))
        self.set_gia(gia)
        giam_gia = int(input("Nhập giảm giá"))
        self.set_giam_gia(giam_gia)
        
    def __str__(self):
        return(f"""
        Tên sản phẩm: {self.get_ten_sp()}
        Gía: {self.get_gia()}
        Giảm giá: {self.get_giam_gia()}
        Thuế : {self.thue()}
        """)