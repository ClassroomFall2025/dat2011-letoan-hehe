from Quan_ly_tai_khoan import * 

menu = {
    1: "Tạo tài khoản",
    2: "Gửi tiền",
    3: "Rút tiền",
    4: "Kiểm tra số dư",
    5: "Danh sách tài khoản",
    6: "Đóng( xóa) tài khoản",
    7: "Chỉnh sửa thông tin tài khoản",
    8: "Tìm kiếm theo tên",
    9: "Xuất báo cáo",
    10: "Sao lưu dữ liệu",
    11: "Phục hồi dữ liệu",
    12: "Thoát"
}
ds_tk = Quan_ly_tai_khoan()
# In menu
def in_menu():
    print("=" * 15 + "Quản lý ngân hàng" + "=" * 14)
    for key, value in menu.items():
        print(f"| {key}. {value} {(40 - len(value)) * ' '}  ")
    print("=" * 46)
    while True:
        
        while True:
            try:
                luachon = int(input("\nNhập lựa chọn của bạn (1-12): "))
                if luachon in menu.keys():
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
                    continue
            except ValueError:
                print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
                continue
        match luachon:
            case 1:
                #print("=" * 15 + "Tạo tài khoản" + "=" * 18)
                ds_tk.tao_tk()
                ghifile(ds_tk)
                   
            case 2:
                Guitien(ds_tk)
            case 3:
                Rut_tien(ds_tk)
            case 4:
                kiem_tra_so_du(ds_tk)
            case 5:
                hien_thi_ds_tk(ds_tk)
            case 6:
                xoa_tk(ds_tk)
                ghifile(ds_tk)
            case 7:
                cap_nhat_tk(ds_tk)
            case 8:
                tim_kiem_tk(ds_tk)
            case 9:
                xuat_bao_cao(ds_tk)
            case 10:
                sao_luu_file(ds_tk)
            case 11:
                pass
            case 12:
                print("Cảm ơn đã sử dụng chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
            
                