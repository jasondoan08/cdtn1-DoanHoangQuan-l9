# Dự án Dự báo Khách hàng Rời bỏ (L9)

## 1. Mục tiêu
Hệ thống phân tích lịch sử mua hàng và bảo hành để dự báo khách hàng có nguy cơ không quay lại mua sắm.

## 2. Công nghệ sử dụng
- Python 3.11+
- Pandas, Scikit-learn, Matplotlib
- FastAPI, Uvicorn

## 3. Trạng thái dự án
- [x] Khởi tạo cấu trúc dự án
- [x] Thiết lập môi trường ảo (venv)
- [x] Chạy thành công Smoke Test kiểm tra dữ liệu

Mục 2: Yêu cầu môi trường: Python 3.13, thư viện pandas, scikit-learn, pytest, joblib.

Mục 6: Trạng thái tiến độ hiện tại: Đã hoàn thành việc nạp dữ liệu thô, gán nhãn Churn, chia dữ liệu chống rò rỉ 70/15/15, làm sạch văn bản bảo mật PII, vượt qua 3 unit test và huấn luyện/đánh giá mô hình Baseline (Logistic Regression với class_weight='balanced').

“Nhãn churn=1 có tỷ lệ Recall thấp, dẫn đến việc mô hình bỏ sót nhiều khách hàng chuẩn bị rời bỏ dịch vụ, gây rủi ro thất thoát doanh thu.”

“Cặp nhãn bị nhầm lẫn nhiều nhất là giữa khách hàng ít tương tác nhưng phàn nhiều và khách hàng trung thành, nguyên nhân do thiếu biến đặc trưng về thời gian gắn bó.”

“Không xuất hiện hiện tượng nhãn 'thùng rác' hút dữ liệu sai lệch quá mức, phân bố dự đoán nằm trong ngưỡng chấp nhận được.”

## 3. Hướng dẫn từng bước dựng hệ thống
Bước 1: Cài đặt các thư viện phụ thuộc:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

Bước 2: Chạy script huấn luyện mô hình và tạo tệp metrics.json:
\`\`\`bash
python src/models/train_model.py
\`\`\`

Bước 3: Chạy toàn bộ các unit test để kiểm tra logic:
\`\`\`bash
pytest -v
\`\`\`
### **Mục 6: Tiến độ hiện tại**

```markdown
## 6. Tiến độ hiện tại
- Hoàn thành xây dựng pipeline Machine Learning (tiền xử lý dữ liệu, huấn luyện mô hình LogisticRegression, sinh file `metrics.json`).
- Đã kiểm thử thành công toàn bộ Unit Test (8/8 tests passed).
- Hoàn tất kiểm thử E2E trên môi trường thư mục sạch và đẩy toàn bộ mã nguồn lên GitHub thành công.