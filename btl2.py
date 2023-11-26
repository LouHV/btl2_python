import pandas as pd
import matplotlib.pyplot as plt

# a. Đọc dữ liệu từ file Excel
file_path = 'DuLieuThucHanh2_V1.xlsx'
df_san_pham = pd.read_excel(file_path, sheet_name='San Pham')
df_nhan_vien = pd.read_excel(file_path, sheet_name='Nhan Vien')
df_hoa_don = pd.read_excel(file_path, sheet_name='Hoa Don')
df_thong_tin = pd.read_excel(file_path, sheet_name='Thong Tin Hoa Don')

# Hiển thị 2 dataframe
print("Dataframe từ Sheet1(San Pham):")
print(df_san_pham)
print("\nDataframe từ Sheet2(Nhan Vien):")
print(df_nhan_vien)
print("\nDataframe từ Sheet3(Hoa Don):")
print(df_hoa_don)
print("\nDataframe từ Sheet4(Thong Tin Hoa Don):")
print(df_thong_tin)

# b. Tạo DataFrame mới df_ban_hang
df_ban_hang1 = df_thong_tin.groupby('ID San Pham')['So Luong'].sum().reset_index()
df_ban_hang = df_san_pham[['ID San Pham','Ten']].merge( df_ban_hang1, on='ID San Pham', how='left')
df_ban_hang.fillna(0, inplace=True)
print("\nDataframe df_ban_hang: ")
print(df_ban_hang)

# thông tin sản phẩm bán chạy nhất
max_soluong_ban = df_ban_hang[df_ban_hang['So Luong'] == df_ban_hang['So Luong'].max()]
print("\nThông tin sản phẩm bán chạy nhất:")
print(max_soluong_ban)
