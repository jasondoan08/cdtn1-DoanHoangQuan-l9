1. Giới thiệu và phạm vi
- Bối cảnh: Luồng nghiệp vụ "Tự động phân loại sự cố bảo hành bằng AI" (Luồng L9) thuộc hệ thống Smart CRM Mekong Mobile, nhằm hỗ trợ nhân viên tiếp nhận phân loại chính xác nhóm lỗi từ mô tả của khách hàng. 
- Điều CHỦ Ý KHÔNG LÀM (Mức WON'T): Hệ thống KHÔNG tự động phê duyệt/từ chối yêu cầu bảo hành, KHÔNG tự động hủy phiếu và KHÔNG thay thế quyết định xử lý của nhân viên kỹ thuật. 
- Bảng thuật ngữ (Glossary):
Thuật ngữ	Khái niệm / Giải thích
Phiếu bảo hành	Hồ sơ điện tử ghi nhận thông tin tiếp nhận sự cố thiết bị của khách hàng.
Nhóm sự cố (Category)	Phân loại lỗi hư hỏng của thiết bị (VD: Lỗi màn hình, Lỗi pin/nguồn, Lỗi bo mạch, Lỗi phần mềm).
Confidence Score	Điểm số độ tin cậy của mô hình AI đối với kết quả dự đoán (giá trị từ 0.0 đến 1.0).
Retrain	Quá trình huấn luyện lại mô hình AI bằng tập dữ liệu mới tích lũy.
2. Các bên liên quan và vai trò (Actors)
Vai trò (Actor)	Quyền hạn / Công việc được làm	Hạn chế / Điều không được làm
Nhân viên tiếp nhận	- Nhập mô tả sự cố từ khách hàng.
- Kích hoạt tính năng AI dự đoán nhóm lỗi.
- Xác nhận hoặc chọn lại nhóm lỗi thủ công.	- KHÔNG được can thiệp vào thuật toán hoặc sửa đổi điểm số độ tin cậy của AI.
- KHÔNG có quyền xuất dữ liệu retrain.
Quản trị viên AI	- Xem bảng thống kê hiệu năng mô hình (Accuracy, F1-Score).
- Trích xuất tập dữ liệu phản hồi (các ca dự đoán sai) để huấn luyện lại.	- KHÔNG tham gia trực tiếp vào quy trình tạo và xử lý phiếu bảo hành hàng ngày.
 <img width="975" height="643" alt="image" src="https://github.com/user-attachments/assets/1b076323-5f73-4336-85cb-8066d5337a2a" />

3. Yêu cầu chức năng (Functional Requirements) & User Story
- FR1 (Tự động phân loại sự cố): Hệ thống phải có khả năng tiếp nhận văn bản mô tả và phân loại tự động thành nhóm sự cố tương ứng.
  
	+ US1 (MUST): Là Nhân viên tiếp nhận, tôi muốn nhập đoạn mô tả lỗi và bấm "Dự đoán" để AI đề xuất nhóm sự cố tự động, giúp giảm thời gian nhập liệu.

	+ US2 (MUST): Là Nhân viên tiếp nhận, tôi muốn thấy điểm độ tin cậy (Confidence score) đi kèm kết quả dự đoán để đánh giá mức độ tin cậy của gợi ý.

	+ US3 (MUST): Là Nhân viên tiếp nhận, tôi muốn có thể chọn lại nhóm sự cố thủ công nếu kết quả AI dự đoán chưa chính xác. 
- FR2 (Quản lý và theo dõi hiệu năng AI): Hệ thống phải ghi nhận dữ liệu phản hồi và cung cấp công cụ theo dõi chất lượng mô hình.
  
	+ US4 (SHOULD): Là Quản trị viên AI, tôi muốn hệ thống tự động lưu vết các trường hợp nhân viên chọn lại nhóm lỗi khác với AI để thu thập dữ liệu phục vụ retrain.

	+ US5 (SHOULD): Là Quản trị viên AI, tôi muốn xem báo cáo tỷ lệ chính xác (Accuracy, F1-Score) theo thời gian thực để đánh giá chất lượng mô hình.

	+ US6 (COULD): Là Nhân viên tiếp nhận, tôi muốn hệ thống gợi ý 1-2 hướng xử lý sơ bộ dựa trên nhóm lỗi AI vừa phân loại.

	+ US7 (WON'T): Là Hệ thống AI, tự động hủy các phiếu bảo hành không đúng quy định (Nằm ngoài phạm vi hệ thống). 
4. Yêu cầu phi chức năng (Non-Functional Requirements - NFR)
NFR1 (Hiệu năng suy luận): Thời gian phản hồi API của mô hình dự đoán AI từ lúc nhân viên nhấn nút đến khi trả về kết quả phải < 2 giây đối với 95%số lượng yêu cầu.

NFR2 (Tính khả dụng): Giao diện hệ thống phải hiển thị tương thích, không lỗi bố cục trên màn hình độ phân giải tối thiểu 1024x768 pixels. 

NFR3 (Độ chính xác mô hình): Mô hình AI phân loại sự cố phải đạt chỉ số Macro F1-Score tối thiểu >=80% trên tập dữ liệu kiểm thử (Test set). 

5. Ràng buộc và Quy tắc nghiệp vụ (Business Rules)
   
BR1 (Độ dài mô tả): Văn bản mô tả sự cố do nhân viên nhập phải có độ dài tối thiểu từ 3 từ trở lên thì hệ thống mới cho phép kích hoạt tính năng dự đoán AI. 

BR2 (Ngưỡng cảnh báo độ tin cậy): Nếu điểm độ tin cậy (Confidence Score) của dự đoán < 0.60, hệ thống phải hiển thị kết quả kèm cảnh báo màu vàng và bắt buộc nhân viên phải xác nhận thủ công. 

BR3 (Nhật ký lưu vết - Audit Log): Mọi thao tác nhân viên chọn lại nhóm lỗi khác với gợi ý ban đầu của AI đều phải được ghi log bắt buộc gồm: User ID, Timestamp, Nhãn AI gợi ý, Nhãn nhân viên chọn. 

6. Bảng truy vết yêu cầu (Requirement Traceability Matrix)
   
Mã Yêu cầu (FR)	Tên Yêu cầu chức năng	User Story	Use Case liên quan	Mức MoSCoW

FR1	Tự động phân loại sự cố bằng AI	US1, US2	Dự đoán nhóm sự cố tự động	MUST

FR1	Cho phép hiệu chỉnh kết quả dự đoán	US3	Hiệu chỉnh kết quả dự đoán	MUST

FR2	Lưu vết dữ liệu phục vụ retrain	US4	Trích xuất dữ liệu huấn luyện	SHOULD

FR2	Thống kê và hiển thị báo cáo hiệu năng	US5	Xem báo cáo hiệu năng AI	SHOULD
