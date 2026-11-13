# Model Card: Mekong Mobile Smart CRM - AI Prediction Module

## 1. Overview (Tổng quan mô hình)
- **Model Name:** Mobile Customer Behavior / Churn Prediction Model
- **Version:** v1.0
- **Track:** AI Track (BT3)
- **Author/Team:** Doan Hoang Quan (cdtn1-DoanHoangQuan-l9)
- **Intended Use:** Mô hình được thiết kế để phân tích hành vi khách hàng, dự đoán khả năng mua hàng hoặc rời bỏ dịch vụ của khách hàng trong hệ thống Mekong Mobile Smart CRM, hỗ trợ bộ phận chăm sóc khách hàng đưa ra chiến lược tiếp thị phù hợp.

## 2. Architecture & Tech Stack (Kiến trúc & Công nghệ)
- **Language:** Python 3.13
- **Frameworks:** FastAPI, Pydantic (dùng để validate dữ liệu đầu vào/đầu ra của mô hình), Scikit-learn (hoặc thư viện học máy tương ứng).
- **Deployment:** Docker & Docker Compose (tích hợp cùng cơ sở dữ liệu PostgreSQL).

## 3. Training & Data Source (Dữ liệu huấn luyện)
- **Data Source:** Dữ liệu được khởi tạo và nạp tự động từ các tập lệnh SQL trong thư mục dự án:
  - `db/init/001_create_tables.sql`: Định nghĩa cấu trúc các bảng quản lý khách hàng, lịch sử giao dịch và tương tác.
  - `db/init/002_seed_data.sql`: Dữ liệu mẫu ban đầu (seed data) phục vụ cho việc kiểm thử và huấn luyện mô hình.
- **Features (Đặc trưng đầu vào):** 
  - Lịch sử mua sắm thiết bị di động (tần suất, giá trị đơn hàng).
  - Thời gian tương tác gần nhất với cửa hàng.

## 4. Validation & Governance (Kiểm hợp lệ dữ liệu)
- **Pydantic Validation:** Mọi yêu cầu (request) gửi tới API dự đoán của mô hình đều được kiểm tra tính hợp lệ về kiểu dữ liệu (kiểu số, chuỗi, email, v.v.) thông qua các schema Pydantic, đảm bảo hệ thống không bị lỗi khi nhận dữ liệu rác.
- **Health Check:** Mô hình được tích hợp endpoint `/health` để tự động kiểm tra trạng thái hoạt động thông qua cơ chế Healthcheck của Docker Compose.

## 5. Limitations & Future Work (Hạn chế & Hướng phát triển)
- **Limitations:** Mô hình hiện tại sử dụng tập dữ liệu mẫu cố định (`seed_data.sql`), độ chính xác có thể thay đổi khi áp dụng vào dữ liệu thực tế lớn hơn.
- **Future Work:** Tích hợp mô hình học sâu (Deep Learning) nâng cao và tự động cập nhật trọng số mô hình định kỳ từ cơ sở dữ liệu PostgreSQL.