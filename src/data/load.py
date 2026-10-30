import logging
import sys
import pandas as pd
from datetime import datetime

# Cấu hình logging cho module nạp dữ liệu
logger = logging.getLogger("ETLLoader")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

def load_raw_data(data_dir="data/"):
    """Nạp các tệp dữ liệu thô từ thư mục data/ với cơ chế bắt lỗi an toàn."""
    try:
        logger.info(f"Đang nạp các tệp dữ liệu thô từ thư mục: {data_dir}")
        customers_df = pd.read_csv(f"{data_dir}/customers_raw.csv")
        orders_df = pd.read_csv(f"{data_dir}/orders_2024_2026.csv")
        tickets_df = pd.read_csv(f"{data_dir}/tickets_history.csv")
        
        logger.info(f"Nạp thành công: customers ({len(customers_df)} dòng), orders ({len(orders_df)} dòng), tickets ({len(tickets_df)} dòng)")
        return customers_df, orders_df, tickets_df
    except Exception as e:
        logger.error(f"Lỗi nghiêm trọng khi đọc tệp dữ liệu thô: {e}", exc_info=True)
        sys.exit(1)

def preprocess_and_label_churn(customers_df, orders_df, tickets_df):
    """
    Tiền xử lý, kiểm tra chất lượng dữ liệu (Data Quality) và định nghĩa nhãn Churn.
    """
    logger.info("Bắt đầu tiền xử lý và kiểm tra chất lượng dữ liệu...")
    
    # 1. Quality Check: Kiểm tra cột định danh khách hàng
    merge_col = 'so_dien_thoai' if 'so_dien_thoai' in customers_df.columns else 'ten_khach_hang'
    order_group_col = 'so_dien_thoai' if 'so_dien_thoai' in orders_df.columns else 'ten_khach_hang'
    
    # Kiểm tra dữ liệu trống ở khóa chính
    missing_cust_keys = customers_df[merge_col].isnull().sum()
    if missing_cust_keys > 0:
        logger.warning(f"Phát hiện {missing_cust_keys} dòng thiếu khóa định danh ({merge_col}) trong bảng khách hàng!")

    # 2. Xử lý ngày giao dịch đa định dạng từ cột 'ngay'
    orders_df['ngay_chuan'] = pd.to_datetime(orders_df['ngay'], errors='coerce', dayfirst=True)
    invalid_dates = orders_df['ngay_chuan'].isnull().sum()
    if invalid_dates > 0:
        logger.warning(f"Phát hiện {invalid_dates} dòng có định dạng ngày tháng không hợp lệ trong bảng đơn hàng đã bị chuyển thành NaT.")

    # 3. Tính toán ngày giao dịch cuối của từng khách hàng
    latest_order = orders_df.groupby(order_group_col)['ngay_chuan'].max().reset_index()
    latest_order.columns = ['key_lien_ket', 'ngay_giao_dich_cuoi']
    
    # Lấy mốc thời gian lớn nhất trong dữ liệu làm mốc hiện tại
    max_date = latest_order['ngay_giao_dich_cuoi'].max()
    if pd.isna(max_date):
        logger.error("Không tìm thấy mốc thời gian giao dịch hợp lệ nào trong orders_df!")
        max_date = datetime.now()

    latest_order['so_ngay_khong_giao_dich'] = (max_date - latest_order['ngay_giao_dich_cuoi']).dt.days
    
    # Định nghĩa nhãn Churn: Khách hàng không giao dịch trên 90 ngày -> Churn = 1, ngược lại = 0
    latest_order['Churn'] = latest_order['so_ngay_khong_giao_dich'].apply(lambda x: 1 if x > 90 else 0)
    
    # 4. Gộp dữ liệu khách hàng và lịch sử đơn hàng
    merged_df = pd.merge(customers_df, latest_order, left_on=merge_col, right_on='key_lien_ket', how='left')
    
    # Xử lý khách hàng không có lịch sử đơn hàng (khách mới / mất tích) -> tính Churn = 1
    missing_history_count = merged_df['Churn'].isnull().sum()
    if missing_history_count > 0:
        logger.warning(f"Có {missing_history_count} khách hàng không có lịch sử giao dịch trong orders, tự động gán nhãn Churn = 1.")
    merged_df['Churn'] = merged_df['Churn'].fillna(1)
    
    logger.info(f"Hoàn tất tiền xử lý. Kích thước dữ liệu hợp nhất: {merged_df.shape}")
    return merged_df

if __name__ == "__main__":
    cust, ords, ticks = load_raw_data()
    final_df = preprocess_and_label_churn(cust, ords, ticks)
    logger.info("\n--- KẾT QUẢ XỬ LÝ ---")
    logger.info(f"Kích thước dữ liệu sau khi gán nhãn: {final_df.shape}")
    logger.info("Phân bố nhãn Churn:\n" + str(final_df['Churn'].value_counts(normalize=True).round(3)))