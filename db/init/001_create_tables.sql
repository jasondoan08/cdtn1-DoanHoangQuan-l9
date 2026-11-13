-- Tạo bảng khách hàng và bảng lưu phiếu hỗ trợ/sự cố (CRM)
CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tickets (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    mo_ta TEXT NOT NULL,
    predicted_label VARCHAR(50),
    confidence FLOAT,
    status VARCHAR(20) DEFAULT 'OPEN',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);