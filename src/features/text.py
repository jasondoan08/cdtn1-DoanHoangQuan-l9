import re
import unicodedata

def lam_sach(s):
    """
    Giữ DẤU tiếng Việt, thay thế thông tin định danh cá nhân bằng các thẻ tương ứng, 
    chuẩn hóa khoảng trắng và chuyển về chữ thường.
    """
    if s is None or str(s).strip() == '':
        return ''
    
    s = str(s).lower()
    
    # Thay thế số điện thoại bằng thẻ <SDT>
    s = re.sub(r'\b0\d{9}\b', '<SDT>', s)
    # Thay thế mã serial bằng thẻ <SERIAL>
    s = re.sub(r'\b(hd|pb|sn)-?\d+\b', '<SERIAL>', s, flags=re.I)
    # Thay thế email bằng thẻ <EMAIL>
    s = re.sub(r'\S+@\S+', '<EMAIL>', s)
    
    # Loại bỏ các ký tự đặc biệt không cần thiết nhưng giữ lại chữ cái tiếng Việt có dấu
    s = re.sub(r'[^\w\sàáạảãâấầậẩẫăắằặẳẵèéẹẻẽêếềệểễìíịỉĩòóọỏõôốồộổỗơớờợởỡùúụủũưứừựửữỳýỵỷỹđ]', ' ', s)
    
    # Chuẩn hóa khoảng trắng thừa
    return re.sub(r'\s+', ' ', s).strip()
