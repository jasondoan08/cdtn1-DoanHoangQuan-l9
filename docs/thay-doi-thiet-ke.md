# Nhật ký thay đổi thiết kế
## Điều chỉnh sau phản hồi Bài tập 1 (Buổi 8, Ngày 16/10/2026)

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
- **Lý do:** Giúp người đọc (và giảng viên chấm bài) hiểu chính xác các khối thành phần, ranh giới hệ thống và các yếu tố không nằm trong phạm vi xử lý của prototype.
- **Ảnh hưởng tới thành phần:** Cập nhật lại file `architecture.drawio` và `ml-pipeline.drawio` trên draw.io, xuất lại ảnh PNG tương ứng để đưa vào báo cáo PDF của Bài tập 2.
