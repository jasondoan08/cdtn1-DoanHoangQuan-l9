# Mekong Mobile Smart CRM - Hệ thống Dự báo Khách hàng Rời bỏ (Churn Prediction)

Đồ án học phần ứng dụng Trí tuệ Nhân tạo và Kỹ thuật phần mềm hiện đại, xây dựng hệ thống CRM thông minh tích hợp đường ống ETL tự động kiểm định chất lượng dữ liệu, huấn luyện mô hình Machine Learning và cung cấp dịch vụ dự đoán qua RESTful API bằng FastAPI.

---

## 1. Công nghệ & Môi trường
* **Ngôn ngữ lập trình:** Python 3.13
* **Thư viện xử lý dữ liệu & ML:** Pandas, NumPy, Scikit-learn
* **Framework Web API:** FastAPI, Uvicorn, Pydantic
* **Kiến trúc triển khai:** Container hóa qua Docker, quản lý phụ thuộc binary wheel tối ưu cho Windows.

---

## 2. Cấu trúc Thư mục Dự án
```text
cdtn1-DoanHoangQuan-l9/
│
├── data/                  # Thư mục chứa dữ liệu thô (customers, orders, tickets)
├── src/
│   ├── data/              # Module ETL, kiểm tra chất lượng dữ liệu (load.py)
│   ├── models/            # Module huấn luyện mô hình baseline & pipeline (train.py, baseline.py)
│   └── app.py             # Dịch vụ FastAPI (tích hợp lifespan, logging, /health, /predict)
├── .env.example           # Tệp mẫu cấu hình môi trường
├── requirements.txt       # Danh sách thư viện phụ thuộc ghim phiên bản
└── README.md              # Tài liệu hướng dẫn dự án

Bước 3.1: Cài đặt các thư viện phụ thuộc
Đảm bảo bạn đang đứng ở thư mục gốc của dự án và chạy lệnh sau để cài đặt các gói nhị phân tương thích:

Bash
pip install --only-binary=:all: -r requirements.txt
Bước 3.2: Chạy kiểm tra ETL và Huấn luyện mô hình
Bash
python -m src.models.train
Hệ thống sẽ tự động nạp dữ liệu, kiểm tra dữ liệu bẩn (thiếu khóa, sai định dạng ngày tháng), gán nhãn Churn và đánh giá mô hình Baseline.

Bước 3.3: Khởi động Dịch vụ API FastAPI
Bash
python -m uvicorn src.app:app --reload
Server sẽ khởi động và hiển thị: Uvicorn running on http://127.0.0.1:8000

Bước 3.4: Trải nghiệm Tài liệu API trực tuyến (Swagger UI)
Mở trình duyệt web và truy cập:

Giao diện tài liệu Swagger UI: http://127.0.0.1:8000/docs

Kiểm tra trạng thái hệ thống (/health): Trả về trạng thái hoạt động và xác nhận mô hình đã được nạp.

Dự đoán (/predict): Truyền số ngày không giao dịch để nhận kết quả dự đoán rủi ro rời bỏ (churn_prediction) kèm xác suất (churn_probability) và mã tra cứu (ma_yeu_cau).
