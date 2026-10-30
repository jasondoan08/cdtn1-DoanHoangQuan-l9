
import logging
import sys
import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score
from src.data.load import load_raw_data, preprocess_and_label_churn
from src.data.split import chia_du_lieu
from src.models.baseline import tao_mo_hinh_baseline

# Cấu hình logging chuẩn mực xuất ra stdout (phục vụ Docker thu thập log)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("TrainPipeline")

def chay_huan_luyen():
    try:
        logger.info("1. Đang nạp và gán nhãn dữ liệu thô...")
        cust, ords, ticks = load_raw_data()
        df_labeled = preprocess_and_label_churn(cust, ords, ticks)
        
        logger.info("2. Đang chia dữ liệu (Train/Val/Test chống rò rỉ)...")
        train_df, val_df, test_df = chia_du_lieu(df_labeled)
        
        # Sử dụng cột số ngày không giao dịch làm đặc trưng số cơ bản cho Baseline
        feature_col = 'so_ngay_khong_giao_dich'
        
        X_train = train_df[[feature_col]].fillna(0)
        y_train = train_df['Churn']
        
        X_val = val_df[[feature_col]].fillna(0)
        y_val = val_df['Churn']
        
        logger.info("3. Đang huấn luyện mô hình Baseline...")
        model = tao_mo_hinh_baseline()
        model.fit(X_train, y_train)
        
        logger.info("4. Đánh giá mô hình trên tập Validation...")
        y_pred = model.predict(X_val)
        y_prob = model.predict_proba(X_val)[:, 1]
        
        # Ghi log kết quả đánh giá dạng cấu trúc thông điệp
        report_str = classification_report(y_val, y_pred)
        logger.info(f"\n--- KẾT QUẢ ĐÁNH GIÁ (CLASSIFICATION REPORT) ---\n{report_str}")
        
        # Xử lý ngoại lệ an toàn cho metric phụ (tránh crash pipeline nếu thiếu lớp)
        try:
            roc_auc = roc_auc_score(y_val, y_prob)
            logger.info(f"ROC-AUC Score trên tập Validation: {roc_auc:.4f}")
        except Exception as e:
            logger.warning(f"Không thể tính ROC-AUC Score (có thể do tập validation đơn lớp): {e}")

    except Exception as e:
        # Bắt lỗi nghiêm trọng ở tầng trên cùng, ghi log ERROR kèm ngăn xếp lỗi (stack trace)
        logger.error("Quá trình huấn luyện mô hình thất bại do lỗi hệ thống:", exc_info=True)
        # Thoát với mã lỗi non-zero để hệ thống CI/CD hoặc Docker biết pipeline bị hỏng
        sys.exit(1)

if __name__ == "__main__":
    chay_huan_luyen()