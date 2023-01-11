import pickle
from staff import NhanVien
def nhap_list_danh_sach_nhan_vien(ds_nhan_vien):
    while True:
        hoten = input("Nhập họ tên nhân viên (nhập 'q' để dừng nhập): ")
        if hoten == 'q':
            break
        tuoi = int(input("Nhập tuổi nhân viên = "))
        luong = input("Nhập lương nhân viên = ")
        nhan_vien = NhanVien(hoten, tuoi, luong)
        ds_nhan_vien.append(nhan_vien)
    return ds_nhan_vien
def in_list_danh_sach_nhan_vien(ds_nhan_vien):
    for item in ds_nhan_vien:
        print("Danh sách nhân viên :" , item)
    return item
def sap_xep_danh_sach(ds_nhan_vien):
    ds_sinh_vien = sorted(ds_nhan_vien, reverse=True)
    for item in ds_sinh_vien:
        print("Sắp xếp danh sách: " ,item)
    return item
def luu_tap_tinnhiphan(ds_nhan_vien, filename):
    with open(filename,'wb') as f:
        pickle.dump(ds_nhan_vien, f)
        print("Lưu tập tin nhị phân")
def main():
    ds_nhan_vien = []
    nhap_danh_sach_nhan_vien(ds_nhan_vien)
    in_danh_sach_nhan_vien(ds_nhan_vien)
    sap_xep_danh_sach(ds_nhan_vien)
    luu_tap_tinnhiphan(ds_nhan_vien, 'NhanVien.dat')
if _name__=='__main_':
    main()