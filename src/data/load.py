import pandas as pd
from datetime import datetime

def load_raw_data(data_dir="data/"):
    """Nạp các tệp dữ liệu thô từ thư mục data/"""
    customers_df = pd.read_csv(f"{data_dir}/customers_raw.csv")
    orders_df = pd.read_csv(f"{data_dir}/orders_2024_2026.csv")
    tickets_df = pd.read_csv(f"{data_dir}/tickets_history.csv")
    return customers_df, orders_df, tickets_df

def preprocess_and_label_churn(customers_df, orders_df, tickets_df):
    """
    Tiền xử lý và định nghĩa nhãn Churn khớp với cấu trúc thực tế của file orders_2024_2026.csv
    """
    print("Các cột trong customers_df:", customers_df.columns.tolist())
    print("Các cột trong orders_df:", orders_df.columns.tolist())
    
    # Xử lý ngày giao dịch đa định dạng từ cột 'ngay'
    orders_df['ngay_chuan'] = pd.to_datetime(orders_df['ngay'], errors='coerce', dayfirst=True)
    
    # do orders_2024_2026 dùng 'so_dien_thoai' hoặc 'ten_khach_hang' để định danh,
    # theo 'so_dien_thoai' để tìm ngày giao dịch gần nhất của khách
    group_col = 'so_dien_thoai' if 'so_dien_thoai' in orders_df.columns else 'ten_khach_hang'
    
    latest_order = orders_df.groupby(group_col)['ngay_chuan'].max().reset_index()
    latest_order.columns = ['key_lien_ket', 'ngay_giao_dich_cuoi']
    
    # Lấy mốc thời gian lớn nhất trong dữ liệu làm mốc hiện tại
    max_date = latest_order['ngay_giao_dich_cuoi'].max()
    latest_order['so_ngay_khong_giao_dich'] = (max_date - latest_order['ngay_giao_dich_cuoi']).dt.days
    
    # Định nghĩa nhãn Churn: Khách hàng không giao dịch trên 90 ngày -> Churn = 1, ngược lại = 0
    latest_order['Churn'] = latest_order['so_ngay_khong_giao_dich'].apply(lambda x: 1 if x > 90 else 0)
    
    # Đồng bộ khóa với bảng customers_raw (giả định customers_raw có cột 'so_dien_thoai')
    merge_col = 'so_dien_thoai' if 'so_dien_thoai' in customers_df.columns else 'ten_khach_hang'
    
    merged_df = pd.merge(customers_df, latest_order, left_on=merge_col, right_on='key_lien_ket', how='left')
    merged_df['Churn'] = merged_df['Churn'].fillna(1) # Khách không có lịch sử đơn hàng tính là Churn = 1
    
    return merged_df

if __name__ == "__main__":
    cust, ords, ticks = load_raw_data()
    final_df = preprocess_and_label_churn(cust, ords, ticks)
    print("\n--- KẾT QUẢ XỬ LÝ ---")
    print("Kích thước dữ liệu sau khi gán nhãn:", final_df.shape)
    print("Phân bố nhãn Churn:")
    print(final_df['Churn'].value_counts(normalize=True).round(3))
