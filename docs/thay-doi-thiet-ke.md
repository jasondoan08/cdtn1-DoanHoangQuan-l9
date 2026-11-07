# Nhật ký thay đổi thiết kế
## Điều chỉnh sau phản hồi Bài tập 1 

### TD-01: Bổ sung định nghĩa nhãn Churn và cửa sổ thời gian
- **Phản hồi của GV:** Chưa nêu số mẫu của dataset; nhãn Churn chưa nói rõ cửa sổ thời gian (bao nhiêu ngày không giao dịch).
- **Quyết định:** SỬA / BỔ SUNG.
- **Lý do:** Định nghĩa rõ cửa sổ thời gian (ví dụ: khách hàng không phát sinh đơn hàng mới trong vòng 90 ngày) giúp mô hình Machine Learning xác định chính xác nhãn mục tiêu (Target Label) và có cơ sở để đếm số mẫu thực tế trước khi huấn luyện.
- **Ảnh hưởng tới thành phần:** Cập nhật lại phần Dataset Schema và bổ sung vào script tiền xử lý dữ liệu (`src/data/load.py`) trong Bài tập 2.

### TD-02: Hoàn thiện các mục thiếu sót trong tài liệu SRS
- **Phản hồi của GV:** SRS thiếu bảng thuật ngữ, mục WON'T, mục vai trò, User Story có MoSCoW, quy tắc nghiệp vụ và bảng truy vết FR↔US↔UC.
- **Quyết định:** SỬA / BỔ SUNG.
- **Lý do:** Đáp ứng chuẩn yêu cầu đặc tả phần mềm đầy đủ, phục vụ cho việc kiểm tra tính nhất quán giữa tài liệu thiết kế và mã nguồn hiện thực ở các giai đoạn sau.
- **Ảnh hưởng tới thành phần:** Bổ sung các bảng biểu và phân mục còn thiếu trực tiếp vào tệp `docs/srs.md`.

### TD-03: Chuẩn hóa lại các ngưỡng số cho yêu cầu phi chức năng (NFR-02, NFR-03)
- **Phản hồi của GV:** NFR-02, NFR-03 không có ngưỡng số, nên lập luận 2 và 3 không đạt khuôn.
- **Quyết định:** SỬA / BỔ SUNG.
- **Lý do:** Yêu cầu phi chức năng phải có định lượng rõ ràng (ví dụ: NFR-02 về bảo mật phải chỉ rõ các trường thông tin định danh nào bị lọc bỏ; NFR-03 về bảo trì phải định lượng thời gian triển khai mô hình mới qua API) để làm cơ sở cho lập luận thiết kế ở Mục 3.
- **Ảnh hưởng tới thành phần:** Cập nhật lại nội dung Mục 2.2 và Mục 3.2 trong tài liệu thiết kế hệ thống.

### TD-04: Bổ sung chú thích ký hiệu và vùng ngoài phạm vi cho sơ đồ
- **Phản hồi của GV:** Sơ đồ kiến trúc, ML pipeline chưa có chú thích ký hiệu và phần ngoài phạm vi.
- **Quyết định:** SỬA / BỔ SUNG.
- **Lý do:** Giúp người đọc hiểu chính xác các khối thành phần, ranh giới hệ thống và các yếu tố không nằm trong phạm vi xử lý của prototype.
- **Ảnh hưởng tới thành phần:** Cập nhật lại file `architecture.drawio` và `ml-pipeline.drawio` trên draw.io, xuất lại ảnh PNG tương ứng để đưa vào báo cáo PDF của Bài tập 2.

# Nhật ký Thay đổi Thiết kế & Khắc phục Phản hồi Bài tập 2

## 1. Tiếp thu và Xử lý Phản hồi từ Giảng viên (Bài tập 2)
Dựa trên nhận xét chi tiết của thầy Thanh, em đã xác định các hành động khắc phục cho Bài tập 3 như sau:

* **Nhận xét 1 (Thiếu Confusion Matrix & chỉ số từng nhãn - A4):** Báo cáo BT2 chưa có ma trận nhầm lẫn và các chỉ số chi tiết theo từng nhãn phân loại.
  * **Quyết định xử lý:** Bổ sung script xuất Confusion Matrix, phân tích chi tiết chỉ số (Precision, Recall, F1-score) cho từng nhãn và đưa vào tài liệu Model Card (Thành phần 6 của BT3) theo đúng hướng dẫn track AI.
* **Nhận xét 2 (Thiếu so sánh mô hình & chọn qua tập validation):** Chưa thể hiện việc đối chiếu ít nhất 2 mô hình thật với mô hình cơ sở (baseline) và chọn mô hình tối ưu theo tập validation.
  * **Quyết định xử lý:** Cập nhật script huấn luyện (`src/models/train.py`) để chạy song song Baseline và $\ge 2$ giải thuật học máy, ghi nhận bảng so sánh độ đo trên tập validation.
* **Nhận xét 3 (Thông điệp commit chung chung):** Gần một nửa commit message chưa tuân theo quy ước chuẩn.
  * **Quyết định xử lý:** Từ BT3, áp dụng nghiêm ngặt cú pháp commit message rõ ràng theo mẫu `fix(scope): ...` hoặc `feat(scope): ...` gắn liền với mã bug hoặc chức năng.
* **Nhận xét 4 (README thiếu lệnh chạy kiểm thử):** Tệp hướng dẫn chưa ghi rõ lệnh để chạy bộ test tự động.
  * **Quyết định xử lý:** Đã bổ sung tường minh câu lệnh chạy kiểm thử (`pytest -q`) ngay phần đầu tệp `README.md`.

## 2. Các thay đổi kiến trúc và kỹ thuật khác
* Tách biệt rõ ràng các tầng: ETL dữ liệu (`src/data/`), xử lý văn bản đặc trưng (`src/features/`), huấn luyện và đánh giá mô hình (`src/models/`), cùng tầng dịch vụ API (`src/app.py`).