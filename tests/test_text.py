import pytest
from src.features.text import lam_sach

def test_TT01_giu_dau_va_ve_chu_thuong():
    """Loại 1: Luồng đúng - Giữ dấu tiếng Việt và đưa về chữ thường"""
    assert lam_sach('Màn Hình bị SỌC') == 'màn hình bị sọc'

def test_TT02_thay_thong_tin_dinh_danh_bang_the():
    """Loại 2: Giá trị biên / Bảo vệ dữ liệu cá nhân"""
    s = lam_sach('Gọi 0912345678, máy HD-10293, mail an@vd.vn')
    assert '<SDT>' in s and '<SERIAL>' in s and '<EMAIL>' in s
    assert '0912345678' not in s

def test_TT03_chuoi_rong_hoac_chi_co_khoang_trang():
    """Loại 3: Dữ liệu sai - Chuỗi rỗng hoặc rác không gây ngoại lệ"""
    assert lam_sach('') == ''
    assert lam_sach(None) == ''
    assert lam_sach('   \n\t   ') == ''
