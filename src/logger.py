import logging
import sys

def get_logger(name: str) -> logging.Logger:
    """Cấu hình bộ ghi log chuẩn có định dạng thời gian, mức độ và tên module."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Tránh bị nhân đôi handler nếu gọi nhiều lần
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        
        # Định dạng log chuẩn mực: [Thời gian] - [Tên module] - [Mức độ] - [Nội dung]
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger