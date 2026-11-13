-- Nạp dữ liệu mẫu để hệ thống không bị trống trơn khi khởi động
INSERT INTO customers (full_name, phone) VALUES 
('Nguyen Van A', '0901234567'),
('Tran Thi B', '0918765432')
ON CONFLICT (phone) DO NOTHING;

INSERT INTO tickets (customer_id, mo_ta, predicted_label, confidence, status) VALUES 
(1, 'May sac khong vao dien, cam sac khong len', 'PIN_SAC', 0.92, 'OPEN'),
(2, 'Man hinh bi soc xanh, cam ung luc duoc luc khong', 'MAN_HINH', 0.85, 'OPEN');