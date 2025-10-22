from Tai_khoan import *
from datetime import datetime
import csv
import os
import shutil

class Quan_ly_tai_khoan:
    def __init__(self):
        self.ds_tai_khoan = []
        
    def tao_tk(self):
        
        while True:
            self.ten = input("Nhập tên chủ tài khoản (hoặc nhập e để thoát): ")
            if self.ten.lower() == 'e':
                break
            while True:
                try:
                    self.so_tk = int(input("Nhập số tài khoản: "))
                    if kiem_tra_so_tk_trung(self.so_tk, self):
                        continue
                    break
                except ValueError:
                    print("Số tài khoản phải là số nguyên. Vui lòng nhập lại.")
            while True:
                self.loai = input("Nhập loại tài khoản (T - Tiết kiệm, C - Cá nhân): ").upper()
                if self.loai in ('T', 'C') and self.loai.isalpha():
                    break
                else:
                    print("Loại tài khoản không hợp lệ. Vui lòng nhập lại.")
            user = Taikhoan(self.so_tk, self.ten, 0, self.loai)
            self.ds_tai_khoan.append(user)
            print("Tạo tài khoản thành công!\n")
        print("\nDanh sách tài khoản hiện có:")
        print(f" | {"Số tài khoản":^15} | {"Tên":^20} | {"Loại":^5} | {"Số dư":^30}     | ")
        self.xuat_tt()
        
    def xuat_tt(self):
        if not self.ds_tai_khoan:
            print("Danh sách tài khoản rỗng.")
        else:
            for tk in self.ds_tai_khoan:
                tk.xuat_tt_dang_bang()


        
def Guitien(ds_tk):
    kiemtra = kiem_tra_so_tk(ds_tk)
    if kiemtra is not None:
            while True:
                try:
                    so_tien = int(input("Nhập số tiền cần gửi: "))
                    if so_tien <= 0:
                            print("Số tiền gửi phải lớn hơn 0. Vui lòng nhập lại")
                            continue
                    else:
                            kiemtra.set_Sodu(kiemtra.get_Sodu() + so_tien)
                            print(f"Đã gửi {so_tien} vào tài khoản {kiemtra.get_Sotaikhoan()}. Số dư hiện tại: {kiemtra.get_Sodu()}")
                            break
                except ValueError:
                    print("Số tiền phải là số nguyên. Vui lòng nhập lại.")

def  Rut_tien(ds_tk):
    kiem_tra = kiem_tra_so_tk(ds_tk)
    if  kiem_tra is not None:
        while True:
            print("\n")
            print("Số dư hiện tại:", kiem_tra.get_Sodu())
            print("Chọn chức năng:")
            print("1: Rút tiền")
            print("2: Thoát")
            lua_chon = input("Nhập lựa chọn của bạn:")    
            if lua_chon == "1":
                while True:
                    try:
                        so_tien_rut = int(input("Nhập số tiền cần rút: "))
                        break
                    except:
                        print("Số tiền rút phải là số nguyên. Vui lòng nhập lại.")
                        continue
                if so_tien_rut > kiem_tra.get_Sodu():
                    print("Số dư không đủ để rút số tiền yêu cầu.")
                else:
                    so_du_moi = kiem_tra.get_Sodu() - so_tien_rut
                    kiem_tra.set_Sodu(so_du_moi)
                    print(f"Đã rút {so_tien_rut} từ tài khoản {kiem_tra.get_Sotaikhoan()}. Số dư hiện tại: {kiem_tra.get_Sodu()}")          
            elif lua_chon == "2":
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
def kiem_tra_so_du(ds_tk):
    while True:
        try:
            check_tk = int(input("\nNhập số tài khoản cần kiểm tra số dư: "))
            break
        except ValueError:
            print("Số tài khoản phải là số nguyên. Vui lòng nhập lại.")
            
    for tk in ds_tk.ds_tai_khoan:
        if tk.get_Sotaikhoan() == check_tk:
            print("\nThông tin tài khoản: ")
            print(f" | {"Số tài khoản":^15} | {"Tên":^20} | {"Loại":^5} | {"Số dư":^30}     | ")
            tk.xuat_tt_dang_bang()
        
                
def hien_thi_ds_tk(ds_tk):
    for tk in ds_tk.ds_tai_khoan:
        print("="*83)
        print(f" | {"Số tài khoản":^15} | {"Tên":^20} | {"Loại":^5} | {"Số dư":^30}     | ")
        tk.xuat_tt_dang_bang()
        
    
def xoa_tk(ds_tk):
    for tk in ds_tk.ds_tai_khoan:
        if kiem_tra_so_tk(ds_tk):
            ds_tk.ds_tai_khoan.remove(tk)
            print("Xóa tài khoản thành công.")
            return
        else:
            print("Không tìm thấy tài khoản. Vui lòng kiểm tra lại số tài khoản.")
    return
            
def cap_nhat_tk(ds_tk):
    for tk in ds_tk.ds_tai_khoan:
        if kiem_tra_so_tk(ds_tk):
            print("\n")
            print("=" * 3 + " Cập nhật thông tin tài khoản " + "=" * 4)
            print("| 1. Cập nhật tên                   |")
            print("| 2. Cập nhật loại tài khoản        |")
            print("| 3. Cập nhật số dư                 |")
            print("| 4. Thoát                          |")
            print("=" * 37)

            while True:
                lua_chon = input("\nNhập lựa chọn của bạn (1-4): ")
                if lua_chon == "1":
                    ten_moi = input("Nhập tên mới cho tài khoản: ")
                    tk.set_ten(ten_moi)
                if lua_chon == "2":
                    while True:
                        loai_moi = input("Nhập loại tài khoản mới (T - Tiết kiệm, C - Cá nhân):").upper()
                        if loai_moi in ('T','C') and loai_moi.isalpha():
                            tk.loai = loai_moi
                            break
                        else:
                            print("Loại tài khoản không hợp lệ. Vui lòng nhập lại.")
                            continue
                if lua_chon == "3":
                    while True:
                        try:
                            so_du_moi = int(input("Nhập số dư mới:"))
                            if so_du_moi < 0:
                                print("\nSố dư không được âm. Vui lòng nhập lại.")
                                continue
                            tk.set_Sodu(so_du_moi)
                            print(f"\nĐã thêm {so_du_moi} vào tài khoản thành công.")
                            break
                        except ValueError:
                            print("\nSố dư phải là số nguyên. Vui lòng nhập lại.")
                            continue
                if lua_chon == "4":
                    break
                        
def tim_kiem_tk(ds_tk):
    ds_timkiem = []
    
    tu_khoa = input("Nhập từ khóa để tìm kiếm: ").lower()
    for tk in ds_tk.ds_tai_khoan:
        if tu_khoa in tk.get_ten().lower():
            ds_timkiem.append(tk)
    print(f"Tìm thấy {len(ds_timkiem)} tài khoản có từ khóa {tu_khoa}: \n")
    for result in ds_timkiem:
        print(f" | {'Số tài khoản':^15} | {"Tên":^20} | {"Loại":^5} | {"Số dư":^30}     | ")
        result.xuat_tt_dang_bang()

#Kiểm tra số tài khoản
def kiem_tra_so_tk(ds_tk):
    while True:
        try:
            check_tk = int(input("Nhập số tài khoản : "))
            break
        except ValueError:
            print("Số tài khoản phải là số nguyên. Vui lòng nhập lại.")
    for tk in ds_tk.ds_tai_khoan:
        if tk.get_Sotaikhoan() == check_tk:
            print("\nTìm thấy tài khoản:")
            return tk
    print("Không tìm thấy tài khoản.")
    return None
                      
def ghifile(ds_tk):
   
    file_name = "taikhoan.csv"
    file_exists = os.path.exists(file_name)
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Sotaikhoan', 'Ten', 'Loai', 'Sodu']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for tk in ds_tk.ds_tai_khoan:
            writer.writerow({
                'Sotaikhoan': tk.get_Sotaikhoan(),
                'Ten': tk.get_ten(),
                'Loai': tk.loai,
                'Sodu': tk.get_Sodu()
            })

def doc_file():
    with open("taikhoan.csv", mode ='r', encoding = 'utf-8')as file:
        file.readline()
        for line in file:
            print(line.strip())
def kiem_tra_so_tk_trung(check_so_tk, ds_tk):
    for tk in ds_tk.ds_tai_khoan:
        if tk.get_Sotaikhoan() == check_so_tk:
            print("Số tài khoản đã tồn tại. Vui lòng nhập số tài khoản khác.")
            return True

def dem_tai_khoan_theo_loai(ds_tk, loai):
    count = 0
    for tk in ds_tk.ds_tai_khoan:
        if tk.loai == loai:
            count += 1
    return count

def dem_tong_so_du_(ds_tk):
    tong_so_du = 0
    for tk in ds_tk.ds_tai_khoan:
        tong_so_du += tk.get_Sodu()
    return tong_so_du

def xuat_bao_cao(ds_tk):
    file_name = "Bao_cao_tai_khoan.txt"
    with open(file_name, mode = 'w', encoding = 'utf-8') as file:
        file.write("BÁO CÁO QUẢN LÝ TÀI KHOẢN NGÂN HÀNG\n")
        file.write(f"Ngày báo cáo: {datetime.now().strftime('%d-%M-%Y %H:%M:%S')}\n\n")
        file.write(f"Tổng số tài khoản: {len(ds_tk.ds_tai_khoan)}\n")
        tk_loai_T = dem_tai_khoan_theo_loai(ds_tk, 'T')
        tk_loai_C = dem_tai_khoan_theo_loai(ds_tk, 'C')
        file.write(f"Số tài khoản loại Tiết kiệm (T): {tk_loai_T}\n")
        file.write(f"Số tài khoản loại Cá nhân (C): {tk_loai_C}\n")
        tong_so_du = dem_tong_so_du_(ds_tk)
        file.write(f"Tổng số dư tất cả tài khoản: {tong_so_du}\n")
        
def sao_luu_file(ds_tk):
    with open("backup/taikhoan.csv", mode = 'w', encoding = 'utf-8') as file:
        print("Sao luu file taikhoan.csv")
        file.write(f"File được sao lưu vào lúc {datetime.now().strftime("%d-%M-%Y %H:%M:%S")}\n")
    with open("backup/taikhoan.csv", mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['Sotaikhoan', 'Ten', 'Loai', 'Sodu']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for tk in ds_tk.ds_tai_khoan:
            writer.writerow({
                'Sotaikhoan': tk.get_Sotaikhoan(),
                'Ten': tk.get_ten(),
                'Loai': tk.loai,
                'Sodu': tk.get_Sodu()
            })
        
# def sao_luu_file():
#     file_goc = "taikhoan.csv"
#     back_up = "backup/taikhoan.csv"
#     shutil.copy2(file_goc,back_up)
    
    
            
    
        
            
        