class SVpoly():
    def __init__(self,ten, nganh_hoc):
        self.ten = ten
        self.nganh_hoc = nganh_hoc
        
    def get_diem(self):
        pass
    
    def hoc_luc(self):
        if self.get_diem() >=9 and self.get_diem() <= 10:
            return "Xuat sac"
        if self.get_diem() >=8:
            return "Gioi"
        if self.get_diem() >=7:
            return "Kha"
        if self.get_diem() >=5:
            return "Trung binh"
        else:
            return "Chua dat"
        
    def xuat_tt(self):
        print(f" Ten sinh vien: {self.ten}, Nganh hoc: {self.nganh_hoc.upper()}, Diem: {self.get_diem()}, Hoc luc: {self.hoc_luc()}")
class SvIT(SVpoly):
    def __init__(self, ten, nganh_hoc, diem_java, diem_html, diem_css):
        super().__init__(ten, nganh_hoc)
        self.diem_java = diem_java
        self.diem_html = diem_html
        self.diem_css = diem_css
        
    def get_diem(self):
        return( 2 * self.diem_java + self.diem_html + self.diem_css) /4
    
class SvBiz(SVpoly):
    def __init__(self, ten, nganh_hoc, diem_marketing, diem_sales):
        super().__init__(ten, nganh_hoc)
        self.diem_marketing = diem_marketing
        self.diem_sales = diem_sales
        
    def get_diem(self):
        return ( 2 * self.diem_marketing + self.diem_sales)/3
    