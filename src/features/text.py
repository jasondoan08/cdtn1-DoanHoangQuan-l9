import re

def lam_sach(s):
    """
    Làm sạch văn bản: Giữ nguyên DẤU tiếng Việt, thay thế thông tin định danh cá nhân 
    (SĐT, Serial, Email) bằng các thẻ tag <SDT>, <SERIAL>, <EMAIL>, chuẩn hóa khoảng trắng.
    """
    if s is None or str(s).strip() == '':
        return ''
    
    s = str(s).lower()
    
    # Thay thế thông tin định danh bằng các thẻ tag
    s = re.sub(r'\b0\d{9}\b', ' <SDT> ', s)
    s = re.sub(r'\b(hd|pb|sn)-?\d+\b', ' <SERIAL> ', s, flags=re.I)
    s = re.sub(r'\S+@\S+', ' <EMAIL> ', s)
    
    # Loại bỏ ký tự đặc biệt nhưng GIỮ LẠI dấu tiếng Việt và dấu ngoặc nhọn < > của thẻ tag
    s = re.sub(r'[^\w\s<>àáạảãâấầậẩẫăắằặẳẵèéẹẻẽêếềệểễìíịỉĩòóọỏõôốồộổỗơớờợởỡùúụủũưứừựửữỳýỵỷỹđ]', ' ', s)
    
    # Chuẩn hóa khoảng trắng thừa
    return re.sub(r'\s+', ' ', s).strip()