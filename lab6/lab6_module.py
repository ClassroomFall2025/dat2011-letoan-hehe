class Chunhat:
    def __init__(self, chieu_dai = 0, chieu_rong = 0):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
        
    def get_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) *2
    
    def get_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
        
    def get_thong_tin(self):
        self.chieu_dai = int(input("Nhap chieu dai: "))
        self.chieu_rong = int(input("Nhap chieu rong: "))
        
    def xuat_tt(self) -> str:
        print( f"Chu vi hcn: {self.get_chu_vi()}, Dien tich hcn: {self.get_dien_tich()}, Chieu dai {self.chieu_dai}, Chieu rong {self.chieu_rong}")
    
class Hinhvuong(Chunhat):
    def __init__(self,canh = 0):
        self.canh = canh
        super().__init__(canh,canh)    
    def xuat_tt(self):
        print( f"Chu vi hv: {self.get_chu_vi_hv()}, Dien tich hv: {self.get_dien_tich_hv()}, Canh: {self.canh}")
        
    def get_thong_tin(self):
        self.canh = int(input("Nhap canh hinh vuong:"))
        self.chieu_dai = self.chieu_rong = self.canh #Gán chiều dài chiều rộng hình chữ nhật thành cạnh của hình vuông để tái sử dụng hàm tính diện tích hình chữ nhật
    
    def get_chu_vi_hv(self):
        return self.canh * 4
    def get_dien_tich_hv(self):
        return super().get_dien_tich()
        
        
    