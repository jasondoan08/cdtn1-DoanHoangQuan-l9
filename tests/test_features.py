import pandas as pd
import pytest
from src.features.build_features import build_features

def test_build_features_normal_case():
    """Kiểm tra trường hợp dữ liệu bình thường đủ cột."""
    df_input = pd.DataFrame({
        'so_lan_goi_hotline': [2],
        'tong_tuong_tac': [10],
        'so_lan_phan_nan': [1]
    })
    df_output = build_features(df_input)
    assert list(df_output.columns) == ['so_lan_goi_hotline', 'tong_tuong_tac', 'ty_le_phan_nan']
    assert len(df_output) == 1

def test_build_features_missing_columns():
    """Kiểm tra trường hợp đầu vào bị thiếu cột (giá trị biên/ngoại lệ)."""
    df_input = pd.DataFrame({
        'so_lan_goi_hotline': [3] 
    })
    df_output = build_features(df_input)
    assert 'tong_tuong_tac' in df_output.columns
    assert df_output['tong_tuong_tac'].iloc[0] == 0

def test_build_features_empty_dataframe():
    """Kiểm tra trường hợp DataFrame rỗng."""
    df_input = pd.DataFrame(columns=['so_lan_goi_hotline', 'tong_tuong_tac', 'so_lan_phan_nan'])
    df_output = build_features(df_input)
    assert len(df_output) == 0
    assert list(df_output.columns) == ['so_lan_goi_hotline', 'tong_tuong_tac', 'ty_le_phan_nan']

def test_build_features_null_values():
    """Kiểm tra trường hợp dữ liệu có chứa giá trị NaN (null)."""
    df_input = pd.DataFrame({
        'so_lan_goi_hotline': [None],
        'tong_tuong_tac': [10],
        'so_lan_phan_nan': [2]
    })
    df_output = build_features(df_input)
    assert df_output['so_lan_goi_hotline'].iloc[0] == 0

def test_build_features_output_shape():
    """Kiểm tra số lượng cột trả về luôn cố định là 3 cột đặc trưng."""
    df_input = pd.DataFrame({
        'so_lan_goi_hotline': [1, 2],
        'tong_tuong_tac': [5, 6],
        'so_lan_phan_nan': [0, 1],
        'cot_du_thua': ['a', 'b']
    })
    df_output = build_features(df_input)
    assert df_output.shape[1] == 3