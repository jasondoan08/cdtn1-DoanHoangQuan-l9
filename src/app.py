import logging
import sys
import uuid
from contextlib import asynccontextmanager
import pandas as pd
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from src.models.baseline import tao_mo_hinh_baseline
from src.data.load import load_raw_data, preprocess_and_label_churn

# Cấu hình logging chuẩn mực
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("FastAPIApp")

# Biến toàn cục lưu mô hình
ml_model = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Cơ chế quản lý vòng đời ứng dụng: Load mô hình lúc khởi động"""
    global ml_model
    logger.info("Đang khởi động ứng dụng và load mô hình Machine Learning...")
    try:
        cust, ords, ticks = load_raw_data()
        df_labeled = preprocess_and_label_churn(cust, ords, ticks)
        
        feature_col = 'so_ngay_khong_giao_dich'
        X_train = df_labeled[[feature_col]].fillna(0)
        y_train = df_labeled['Churn']
        
        ml_model = tao_mo_hinh_baseline()
        ml_model.fit(X_train, y_train)
        logger.info("Load và khởi tạo mô hình thành công!")
    except Exception as e:
        logger.error(f"Không thể khởi tạo mô hình lúc khởi động: {e}", exc_info=True)
        raise e
    
    yield
    logger.info("Đang tắt ứng dụng...")

# Khởi tạo FastAPI với giao diện được Việt hóa hoàn toàn
app = FastAPI(
    title="Mekong Mobile Smart CRM - Hệ thống Dự báo Khách hàng Rời bỏ (Churn Prediction)",
    description="Tài liệu API dịch vụ Trí tuệ Nhân tạo phục vụ quản trị quan hệ khách hàng, dự đoán nguy cơ khách hàng rời bỏ.",
    version="2.1.0",
    lifespan=lifespan
)

# Khai báo cấu trúc dữ liệu đầu vào với chú thích tiếng Việt
class CustomerInput(BaseModel):
    so_ngay_khong_giao_dich: float = Field(
        ..., 
        description="Số ngày khách hàng không phát sinh giao dịch tính đến thời điểm hiện tại", 
        example=120
    )

@app.get(
    "/health", 
    status_code=status.HTTP_200_OK,
    summary="Kiểm tra trạng thái sức khỏe hệ thống",
    description="Kiểm tra xem dịch vụ API có đang hoạt động ổn định và mô hình AI đã được nạp sẵn sàng trong bộ nhớ hay chưa."
)
def health_check():
    """Endpoint kiểm tra sức khỏe hệ thống"""
    if ml_model is None:
        raise HTTPException(status_code=503, detail="Mô hình chưa sẵn sàng trong hệ thống")
    return {
        "trang_thai": "Hoạt động bình thường (Healthy)",
        "mo_hinh_da_tai": True
    }

@app.post(
    "/predict", 
    status_code=status.HTTP_200_OK,
    summary="Dự đoán nguy cơ khách hàng rời bỏ (Churn)",
    description="Nhận các chỉ số hành vi của khách hàng, chạy qua mô hình Machine Learning và trả về kết quả dự đoán kèm xác suất rủi ro."
)
def predict_churn(data: CustomerInput):
    """Endpoint dự đoán Churn"""
    request_id = str(uuid.uuid4())
    logger.info(f"[{request_id}] Nhận yêu cầu dự đoán với dữ liệu: {data.dict()}")
    
    if ml_model is None:
        logger.error(f"[{request_id}] Dự đoán thất bại do mô hình chưa sẵn sàng.")
        raise HTTPException(status_code=503, detail=f"Mô hình chưa sẵn sàng. Mã yêu cầu: {request_id}")
    
    try:
        input_df = pd.DataFrame([[data.so_ngay_khong_giao_dich]], columns=['so_ngay_khong_giao_dich'])
        
        prediction = int(ml_model.predict(input_df)[0])
        probability = float(ml_model.predict_proba(input_df)[0][1])
        
        logger.info(f"[{request_id}] Dự đoán thành công: Churn={prediction}, Xác suất={probability:.4f}")
        
        return {
            "ma_yeu_cau": request_id,
            "du_bao_nguy_co_churn": prediction,
            "xac_suat_churn": round(probability, 4),
            "thong_bao": "Dự đoán thành công"
        }
    except Exception as e:
        logger.error(f"[{request_id}] Lỗi xử lý dự đoán: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail=f"Lỗi nội bộ hệ thống. Mã tra cứu: {request_id}"
        )