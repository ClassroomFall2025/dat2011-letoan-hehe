import lab6_module_sv  as svpl
class QuanLySinhVien:
    # Khởi tạo danh sách sinh viên rỗng
    def __init__(self):
        self.danh_sach_sinh_vien = []
    # Phuơng thức nhập danh sách sinh viên
    def nhap_dssv(self):
        while True:
            ho_ten_sv = input("Nhập họ tên sinh viên(hoặc nhập e để thoát): ")
            if ho_ten_sv.lower() == "e":
                break
            
            while True:
                nganh_hoc = input("Nhập ngành học: ")
                if nganh_hoc.lower() == "it":
                    java = float(input("Nhập điểm Java: "))
                    html = float(input("Nhập điểm HTML: "))
                    css = float(input("Nhập điểm CSS: "))
                    sv = svpl.SvIT(ho_ten_sv, nganh_hoc, java, html, css)
                    self.danh_sach_sinh_vien.append(sv)
                    break
                elif nganh_hoc.lower() == "biz":
                    marketing = float(input("Nhập điểm Marketing: "))
                    sales = float(input("Nhập điểm Sales: "))
                    sv = svpl.SvBiz(ho_ten_sv, nganh_hoc, marketing, sales)
                    self.danh_sach_sinh_vien.append(sv)
                    break
                else:
                    print("Ngành học không hợp lệ. Vui lòng nhập lại.")
                    continue
        return self.danh_sach_sinh_vien
    # Phuơng thức xuất danh sách sinh viên
    def xuat_dssv(self):
        if not self.danh_sach_sinh_vien:
            print("Danh sách sinh viên rỗng.")
        else:
            
            for sv in self.danh_sach_sinh_vien:
                sv.xuat_tt()
    def xuat_dssv_gioi(self):
        print("Danh sách sinh viên giỏi:  ")
        for sv in self.danh_sach_sinh_vien:
            if sv.hoc_luc() == "Gioi" or sv.hoc_luc() == "Xuat sac":
                sv.xuat_tt()
        else:
            print("Không có sinh viên giỏi trong danh sách.")
    def sap_xep_dssv(self):
        return sorted(self.danh_sach_sinh_vien , key=lambda sv:sv.get_diem(), reverse= True)
       