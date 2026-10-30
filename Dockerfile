# Sử dụng ảnh nền Python 3.13 slim gọn nhẹ và ghim phiên bản
FROM python:3.13-slim
# Thiết lập thư mục làm việc bên trong container
WORKDIR /app
# Tạo nhóm và người dùng non-root để đảm bảo bảo mật (không chạy quyền root)
RUN groupadd -r appuser && useradd -r -g appuser appuser
# Sao chép tệp requirements.txt trước để tận dụng cơ chế lưu cache của Docker layer
COPY requirements.txt .
# Cài đặt các thư viện phụ thuộc
RUN pip install --no-cache-dir -r requirements.txt
# Sao chép toàn bộ mã nguồn còn lại vào container
COPY . .
# Chuyển quyền sở hữu thư mục /app cho non-root user
RUN chown -R appuser:appuser /app
# Chuyển sang sử dụng non-root user
USER appuser
# Đảm bảo Python xuất log trực tiếp ra stdout (không đệm - unbuffered)
ENV PYTHONUNBUFFERED=1
# Khai báo cổng (nếu ứng dụng của bạn chạy dịch vụ web/API, ví dụ cổng 8000)
EXPOSE 8000
# Tích hợp Healthcheck để tự động kiểm tra sức khỏe container
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health').read()" || exit 1
# Lệnh mặc định khi container chạy (bạn có thể thay đổi tùy thuộc vào điểm vào của dự án, ví dụ: src/train.py hoặc dịch vụ API)
CMD ["python", "src/models/train.py"]