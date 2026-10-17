
import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.feature_extraction.text import TfidfVectorizer
from src.data.load import load_raw_data, preprocess_and_label_churn
from src.data.split import chia_du_lieu
from src.models.baseline import tao_mo_hinh_baseline

def chay_huan_luyen():
    print("1. Đang nạp và gán nhãn dữ liệu thô...")
    cust, ords, ticks = load_raw_data()
    df_labeled = preprocess_and_label_churn(cust, ords, ticks)
    
    print("2. Đang chia dữ liệu (Train/Val/Test chống rò rỉ)...")
    train_df, val_df, test_df = chia_du_lieu(df_labeled)
    
    # Sử dụng cột số ngày không giao dịch làm đặc trưng số cơ bản cho Baseline
    feature_col = 'so_ngay_khong_giao_dich'
    
    X_train = train_df[[feature_col]].fillna(0)
    y_train = train_df['Churn']
    
    X_val = val_df[[feature_col]].fillna(0)
    y_val = val_df['Churn']
    
    print("3. Đang huấn luyện mô hình Baseline...")
    model = tao_mo_hinh_baseline()
    model.fit(X_train, y_train)
    
    print("4. Đánh giá mô hình trên tập Validation...")
    y_pred = model.predict(X_val)
    y_prob = model.predict_proba(X_val)[:, 1]
    
    print("\n--- KẾT QUẢ ĐÁNH GIÁ (CLASSIFICATION REPORT) ---")
    print(classification_report(y_val, y_pred))
    
    try:
        roc_auc = roc_auc_score(y_val, y_prob)
        print(f"ROC-AUC Score trên tập Validation: {roc_auc:.4f}")
    except Exception as e:
        print("Không thể tính ROC-AUC:", e)

if __name__ == "__main__":
    chay_huan_luyen()