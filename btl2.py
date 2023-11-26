import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file Excel
file_path = 'DuLieuThucHanh2_V1.xlsx'
df_san_pham = pd.read_excel(file_path, sheet_name='San Pham')
df_nhan_vien = pd.read_excel(file_path, sheet_name='Nhan Vien')
df_hoa_don = pd.read_excel(file_path, sheet_name='Hoa Don')
df_thong_tin = pd.read_excel(file_path, sheet_name='Thong Tin Hoa Don')

#
# Hiển thị 4 dataframe
print("Dataframe từ Sheet1(San Pham):")
print(df_san_pham)
print("\nDataframe từ Sheet2(Nhan Vien):")
print(df_nhan_vien)
print("\nDataframe từ Sheet3(Hoa Don):")
print(df_hoa_don)
print("\nDataframe từ Sheet4(Thong Tin Hoa Don):")
print(df_thong_tin)
