# Bug Log - Hệ thống Mekong Mobile Smart CRM (Track AI)

## BUG-01 · Major · Lỗi xử lý chuỗi mô tả rỗng trả về mã lỗi không đúng định dạng
1. **Mã và mức độ:** BUG-01 · MAJOR · Lỗi kiểm tra dữ liệu đầu vào (Input Validation) ở API dự đoán.
2. **Phát hiện bởi:** TC-05 (Test Report).
3. **Triệu chứng:** Khi người dùng gửi yêu cầu dự đoán với chuỗi mô tả rỗng (`""`), dịch vụ FastAPI đôi lúc trả về lỗi server thay vì mã `422 Unprocessable Entity`.
4. **Cách tái lập:** Gửi yêu cầu HTTP POST tới `/du-doan` với thân JSON `{"mo_ta": ""}`.
5. **Nguyên nhân:** Pydantic model chưa giới hạn ràng buộc độ dài tối thiểu (`min_length=5`) cho trường `mo_ta`, dẫn đến việc hàm xử lý văn bản phía dưới bị lỗi khi nhận chuỗi rỗng.
6. **Cách sửa:** Cập nhật schema Pydantic trong `src/serve/app.py` hoặc `src/schemas/` bằng cách thêm ràng buộc `Field(..., min_length=5)`, cấu hình tự động trả về `422` khi dữ liệu không hợp lệ.
7. **Link commit và xác nhận:** [https://github.com/jasondoan08/cdtn1-DoanHoangQuan-l9/commit/<dán-mã-commit-của-bạn>](https://github.com/jasondoan08/cdtn1-DoanHoangQuan-l9) — Chạy lại TC-05 -> Trả về chuẩn mã `422`, PASS.

---

## BUG-02 · Major · Cảnh báo kiểu dữ liệu Pandas FutureWarning khi điền giá trị thiếu
1. **Mã và mức độ:** BUG-02 · MAJOR · Cảnh báo công nghệ tiềm ẩn lỗi hạ cấp kiểu dữ liệu (Downcasting) trong Pandas.
2. **Phát hiện bởi:** Quá trình chạy pytest (`test_build_features_null_values`).
3. **Triệu chứng:** Khi chạy kiểm thử tính năng làm sạch dữ liệu, Terminal xuất hiện dòng cảnh báo `FutureWarning: Downcasting object dtype arrays on .fillna...`.
4. **Cách tái lập:** Chạy lệnh `python -m pytest -q` trên môi trường Python 3.13 với phiên bản pandas mới.
5. **Nguyên nhân:** Hàm `.fillna(0)` trên cột `so_lan_goi_hotline` thực hiện ép kiểu ngầm định không tường minh, bị deprecate ở các phiên bản pandas tương lai.
6. **Cách sửa:** Thêm phương thức `.infer_objects(copy=False)` ngay sau `.fillna(0)` tại tệp `src/features/build_features.py` dòng 12.
7. **Link commit và xác nhận:** [https://github.com/jasondoan08/cdtn1-DoanHoangQuan-l9/commit/<dán-mã-commit-của-bạn>](https://github.com/jasondoan08/cdtn1-DoanHoangQuan-l9) — Chạy lại `pytest` -> Hết cảnh báo, toàn bộ 8 test PASS.

---

## BUG-03 · Critical · Nguy cơ rò rỉ từ vựng (Data Leakage) khi huấn luyện TF-IDF vectorizer
1. **Mã và mức độ:** BUG-03 · CRITICAL · Lỗi thiết kế pipeline huấn luyện máy học (Rò rỉ dữ liệu / Data Leakage).
2. **Phát hiện bởi:** Kiểm tra mã nguồn huấn luyện mô hình (`src/models/train.py`).
3. **Triệu chứng:** Điểm số đánh giá trên tập test quá cao một cách bất thường nhưng khi đưa vào thực tế lại kém ổn định.
4. **Cách tái lập:** Kiểm tra thứ tự các bước trong script huấn luyện: vectorizer được gọi fit trên toàn bộ dữ liệu trước khi chia tập train/test.
5. **Nguyên nhân:** Vi phạm nguyên tắc cốt lõi của Machine Learning: bộ trích xuất đặc trưng (TF-IDF) đã "nhìn thấy" từ vựng của tập test từ trước khi huấn luyện.
6. **Cách sửa:** Đóng gói toàn bộ quy trình thành một Scikit-Learn `Pipeline` (`Pipeline([('vec', TfidfVectorizer()), ('clf', LogisticRegression())])`) để đảm bảo bộ vectorizer chỉ được fit độc lập bên trong từng fold của quá trình cross-validation.
7. **Link commit và xác nhận:** [https://github.com/jasondoan08/cdtn1-DoanHoangQuan-l9/commit/<dán-mã-commit-của-bạn>](https://github.com/jasondoan08/cdtn1-DoanHoangQuan-l9) — Chạy lại kiểm định chéo và test chống rò rỉ -> PASS.