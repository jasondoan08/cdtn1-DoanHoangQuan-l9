# Nhật ký xử lý sự cố (Bug Log) - Mekong Mobile Smart CRM

| STT | Vấn đề / Lỗi gặp phải | Nguyên nhân gốc rễ | Giải pháp khắc phục | Trạng thái |
|:---:|---|---|---|:---:|
| **1** | **Trùng lặp dòng log (Duplicate Logs)** khi chạy pipeline. | Module `ETLLoader` và `TrainPipeline` cùng cấu hình `StreamHandler` mà không kiểm tra handler tồn tại. | Thêm câu lệnh kiểm tra `if not logger.handlers:` trước khi add handler vào logger. | Đã sửa xong |
| **2** | **Lỗi biên dịch Wheel (`numpy`, `PyYAML`, `pydantic-core`) trên Python 3.13.** | Các phiên bản cũ chưa có sẵn gói binary cho Python 3.13, `pip` cố gắng dịch mã nguồn C/C++ nhưng thiếu Visual Studio Build Tools. | Nâng cấp các gói lên phiên bản tương thích (`pandas==2.2.3`, `numpy==2.2.3`, `PyYAML==6.0.2`, `pydantic==2.8.2`) và dùng cờ `--only-binary=:all:`. | Đã sửa xong |
| **3** | **Lỗi thiếu thư viện `fastapi`** khi khởi động Uvicorn. | Thư viện FastAPI chưa được khai báo đầy đủ trong `requirements.txt` ban đầu. | Bổ sung `fastapi==0.110.0` và `uvicorn==0.28.0` vào `requirements.txt` và cài đặt lại. | Đã sửa xong |