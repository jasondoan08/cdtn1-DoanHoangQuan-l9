import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Xây dựng các đặc trưng (features) từ DataFrame đầu vào.
    Bắt buộc dùng chung cho cả train và inference để tránh lệch dữ liệu.
    """
    df = df.copy()
    
    # Vd xử lý: Điền giá trị thiếu cho các cột số
    if 'so_lan_goi_hotline' in df.columns:
        df['so_lan_goi_hotline'] = df['so_lan_goi_hotline'].fillna(0)
        
    # Tạo đặc trưng mới (Ví dụ: tỷ lệ phàn nàn trên tổng số tương tác)
    if 'tong_tuong_tac' in df.columns and 'so_lan_phan_nan' in df.columns:
        df['ty_le_phan_nan'] = df['so_lan_phan_nan'] / (df['tong_tuong_tac'] + 1e-5)
        
    # Chọn ra đúng danh sách các cột đặc trưng mô hình yêu cầu (giữ nguyên thứ tự)
    expected_features = ['so_lan_goi_hotline', 'tong_tuong_tac', 'ty_le_phan_nan']
    
    # Đảm bảo trả về đúng các cột cần thiết
    for col in expected_features:
        if col not in df.columns:
            df[col] = 0 # Giá trị mặc định nếu thiếu cột
            
    return df[expected_features]