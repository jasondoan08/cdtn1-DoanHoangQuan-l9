# BẢNG KHAI BÁO SỬ DỤNG CÔNG CỤ AI HỖ TRỢ
**Học phần:** Chuyên đề Tốt nghiệp 1 (Specialized Graduation Topic I)  
**Học kỳ:** HK1, Năm học 2026 – 2027  
**Bài nộp:** [ ] Bài tập 1 (BT1)   [X] Bài tập 2 (BT2)   [ ] Bài tập 3 (BT3)  

---

### I. THÔNG TIN SINH VIÊN
* **Họ và tên:** Đoàn Hoàng Quân
* **Mã số sinh viên:** 2374802010412
* **Chuyên ngành (Track):** [ ] SE   [ ] DA   [X] AI
* **Luồng nghiệp vụ đã chọn:** L9 – Dự báo khách hàng rời bỏ

---

### II. BẢNG KHAI BÁO CHI TIẾT

| Công cụ AI | Dùng vào việc gì | Áp dụng ở phần nào (File / Mục) | Đã kiểm chứng & Chỉnh sửa thế nào |
| :--- | :--- | :--- | :--- |
| **Gemini** | 
- Đọc file CDTN1-buổi 01 và 02, dựa vào các luồng có trong buổi 01, hãy gợi ý tôi luồng nào dễ sử dụng và phù hợp với chuyên ngành tôi đang học(tôi học AI)
-> Danh sách liệt kê L10 (Tự động phân loại yêu cầu) hoặc L9 (Dự báo khách hàng rời bỏ) -> em chọn L9
- Hãy hướng dẫn tôi clone git và cho tôi các code để update lên git hub
-> để clone git: git clone https://github.com/<tài-khoản>/<tên-repo>.git
cd <tên-repo>
  để update lên git hub qua clone:
git add .
git commit -m
git push origin main
- Trình bày giúp tôi nên ghi gì vào trong Readme.md
-> Dự án Dự báo Khách hàng Rời bỏ (L9)
1. Mục tiêu
Hệ thống phân tích lịch sử mua hàng và bảo hành để dự báo khách hàng có nguy cơ không quay lại mua sắm.
2. Công nghệ sử dụng
Python 3.11+
Pandas, Scikit-learn, Matplotlib
FastAPI, Uvicorn
3. Trạng thái dự án
 Khởi tạo cấu trúc dự án
 Thiết lập môi trường ảo (venv)
 Chạy thành công Smoke Test kiểm tra dữ liệu
- Về phiêu phạm vi sẽ điền những gì
-> Bước 1: Điền Phiếu phạm vi Mã luồng & Tên luồng: L9 - Dự báo khách hàng rời bỏ.   Phạm vi diễn đạt bằng 1 câu: "Hệ thống phân tích lịch sử mua hàng và bảo hành để dự báo khách hàng có nguy cơ không quay lại mua sắm".   Danh sách 5 User Story dự kiến:   US1: Là hệ thống AI, tôi muốn tổng hợp dữ liệu lịch sử mua hàng và yêu cầu bảo hành của từng khách hàng.   US2: Là hệ thống AI, tôi muốn tiền xử lý dữ liệu và trích xuất các đặc trưng hành vi (như số ngày từ lần mua cuối, tần suất mua, tổng tiền).US3: Là hệ thống AI, tôi muốn dự đoán xác suất rời bỏ (churn) của một khách hàng dựa trên mô hình đã huấn luyện.US4: Là nhân viên Marketing, tôi muốn nhận danh sách các khách hàng có nguy cơ rời bỏ cao để có kế hoạch chăm sóc.US5: Là quản lý, tôi muốn xem thống kê tỷ lệ khách hàng có nguy cơ rời bỏ trên tổng số khách hàng.Dữ liệu làm việc: Chọn "Sinh mô phỏng". ước lượng: "Khoảng 1000 - 2000 dòng dữ liệu giao dịch giả lập".   Công nghệ dự kiến: Python, Scikit-learn, FastAPI, Jupyter Notebook
*Ghi chú:*
- Nếu ở bài nộp này sinh viên **hoàn toàn không sử dụng bất kỳ công cụ AI nào**, hãy ghi rõ `Không sử dụng công cụ AI` vào bảng.


---

### III. CAM KẾT VỀ LIÊM CHÍNH HỌC THUẬT

> **"Tôi xác nhận đã đọc, hiểu và chịu trách nhiệm về toàn bộ nội dung nộp."**

* **Chữ ký / Họ tên sinh viên:** Đoàn Hoàng Quân  
* **Ngày khai báo:** 28/09/2026

Công cụ AI: Gemini

Dùng vào việc gì:

Gợi ý mở rộng danh sách User Story theo chuẩn INVEST, hỗ trợ phát biểu tiêu chí chấp nhận Given-When-Then và gán nhãn MoSCoW.

Rà soát quy tắc vẽ sơ đồ Use Case chuẩn UML (phát hiện lỗi vẽ mũi tên, gợi ý tách Actor phân quyền và kiểm tra số lượng Use Case).

Gợi ý cấu trúc dàn ý SRS 6 mục, chuẩn hóa công thức phát biểu Yêu cầu phi chức năng (NFR) có ngưỡng số đo được và khung Bảng truy vết.

Gợi ý khung nội dung phát biểu bài toán Học máy (ML Problem Statement) cho Track AI.

Áp dụng ở phần nào:

Mục 1: Bản SRS rút gọn (docs/srs.md).

Mục 2: Sơ đồ Use Case (docs/usecase.drawio) và Bảng đặc tả Use Case.

Mục 4: Mô hình dữ liệu & Đặc tả AI (docs/ml-problem-statement.md).

Cách kiểm chứng:

Đối chiếu trực tiếp nội dung gợi ý với các yêu cầu bắt buộc và Rubric chấm điểm trong file đề bài.

Tự thực thao tác vẽ và tinh chỉnh sơ đồ trực tiếp trên phần mềm draw.io, kiểm tra lại logic nghiệp vụ thực tế.

Đọc lại toàn bộ tài liệu, rà soát lỗi chính tả, tự tính toán và điền con số thực tế vào Bảng truy vết và các chỉ số NFR.

"Tôi xác nhận đã đọc, hiểu và chịu trách nhiệm về toàn bộ nội dung nộp."

Họ và tên: Đoàn Hoàng Quân

MSSV: 2374802010412

Ngày: 06/10/2026

1. Công cụ AI: Gemini.
2. Dùng vào việc gì: 
- Hỗ trợ lên ý tưởng khung cấu trúc cho tài liệu phân tích yêu cầu (SRS).
- Gợi ý cách xây dựng các lập luận đánh đổi (trade-offs) khi thiết kế kiến trúc hệ thống dựa trên yêu cầu phi chức năng (NFR).
- Tư vấn các bước tiêu chuẩn cần có trong một luồng xử lý Machine Learning (ML Pipeline).
- Hỗ trợ đối chiếu, rà soát logic khi trích xuất các trường dữ liệu (feature) từ nhiều file CSV phân tán để gom vào bảng Dataset Schema.
- Rà soát bản phác thảo giao diện (Wireframe) do sinh viên tự vẽ và góp ý bổ sung các thông tin còn thiếu (như việc hiển thị rõ Tỷ lệ Churn ở màn hình Kết quả).
3. Áp dụng ở phần nào: 
- Mục 2: Yêu cầu hệ thống và sơ đồ Use Case (Các gạch đầu dòng FR và NFR).
- Mục 3.2: Lập luận Thiết kế dựa trên Yêu cầu Phi chức năng.
- Mục 4.2: Bảng Mô tả Dữ liệu (Dataset Schema).
- Mục 5: Thiết kế giao diện UI Wireframe (Phần rà soát tính hợp lý của bố cục).
4. Cách kiểm chứng: 
- Đã đọc hiểu, tự đánh giá và chọn lọc các gợi ý của AI, loại bỏ các phần không phù hợp để đối chiếu sát với bối cảnh bài toán Luồng 9 (Mekong Mobile Smart CRM).
- Tự tay thao tác vẽ toàn bộ các sơ đồ (Architecture, ML Pipeline) và thiết kế 3 màn hình Wireframe trên công cụ draw.io.
- Tự kiểm chứng lại các trường dữ liệu được ánh xạ từ các file gốc (`customers_raw.csv`, `orders_2024_2026.csv`, `tickets_history.csv`) để đảm bảo không xảy ra rò rỉ dữ liệu (Data Leakage) khi định nghĩa nhãn.
- Đã tự tinh chỉnh, diễn đạt lại văn phong báo cáo để phản ánh đúng tư duy và quyết định thiết kế của cá nhân.
"Tôi xác nhận đã đọc, hiểu và chịu trách nhiệm về toàn bộ nội dung nộp."
- Họ tên sinh viên: Đoàn Hoàng Quân
- Mã số sinh viên: 2374802010412
- Ngày: 10/10/2026

