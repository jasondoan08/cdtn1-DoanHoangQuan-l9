import os
import joblib
import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
from src.data.load import load_raw_data, preprocess_and_label_churn
from src.data.split import chia_du_lieu
from src.models.baseline import tao_mo_hinh_baseline

def danh_gia_tap_test():
    print("1. Đang nạp và xử lý dữ liệu để chuẩn bị đánh giá Test...")
    cust, ords, ticks = load_raw_data()
    df_labeled = preprocess_and_label_churn(cust, ords, ticks)
    
    # Chia dữ liệu để lấy đúng tập Test độc lập
    train_df, val_df, test_df = chia_du_lieu(df_labeled)
    
    feature_col = 'so_ngay_khong_giao_dich'
    
    # Huấn luyện lại trên tập Train (hoặc load mô hình đã lưu)
    X_train = train_df[[feature_col]].fillna(0)
    y_train = train_df['Churn']
    
    X_test = test_df[[feature_col]].fillna(0)
    y_test = test_df['Churn']
    
    print("2. Đang huấn luyện mô hình trên tập Train...")
    model = tao_mo_hinh_baseline()
    model.fit(X_train, y_train)
    
    print("3. Đánh giá mô hình trên tập Test (Test Set Evaluation)...")
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    
    print("\n--- KẾT QUẢ ĐÁNH GIÁ TRÊN TẬP TEST ---")
    print(classification_report(y_test, y_pred))
    
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)
    
    try:
        roc_auc = roc_auc_score(y_test, y_prob)
        print(f"ROC-AUC Score trên tập Test: {roc_auc:.4f}")
    except Exception as e:
        print("Không thể tính ROC-AUC:", e)
        
    # 4. Lưu mô hình vào thư mục artifacts/
    os.makedirs("artifacts", exist_ok=True)
    model_path = "artifacts/churn_baseline_model.pkl"
    joblib.dump(model, model_path)
    print(f"\n4. Đã lưu mô hình thành công tại: {model_path}")

if __name__ == "__main__":
    danh_gia_tap_test()
