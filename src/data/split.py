from sklearn.model_selection import train_test_split

def chia_du_lieu(df, nhan='Churn', hat_giong=42):
    """
    Chia tập dữ liệu thành Train (70%), Validation (15%), và Test (15%)
    Sử dụng stratify để giữ nguyên tỉ lệ nhãn Churn ở các tập.
    Quy tắc: Chia dữ liệu TRƯỚC khi thực hiện bất kỳ bước trích xuất đặc trưng nào.
    """
    # Bước 1: Tách Train (70%) và tập tạm (30%)
    train_df, temp_df = train_test_split(
        df, 
        test_size=0.30, 
        random_state=hat_giong, 
        stratify=df[nhan]
    )
    
    # Bước 2: Tách tập tạm thành Validation (15%) và Test (15%)
    val_df, test_df = train_test_split(
        temp_df, 
        test_size=0.50, 
        random_state=hat_giong, 
        stratify=temp_df[nhan]
    )
    
    print(f"Kích thước tập Train: {train_df.shape[0]} mẫu")
    print(f"Kích thước tập Validation: {val_df.shape[0]} mẫu")
    print(f"Kích thước tập Test: {test_df.shape[0]} mẫu")
    
    return train_df, val_df, test_df

if __name__ == "__main__":
    # Test thử module split với load.py
    from src.data.load import load_raw_data, preprocess_and_label_churn
    
    cust, ords, ticks = load_raw_data()
    df_labeled = preprocess_and_label_churn(cust, ords, ticks)
    
    train, val, test = chia_du_lieu(df_labeled)
