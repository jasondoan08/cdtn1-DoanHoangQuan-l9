from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

def tao_mo_hinh_baseline():
    """
    Xây dựng mô hình Baseline sử dụng Logistic Regression.
    Sử dụng class_weight='balanced' để xử lý hiện tượng mất cân bằng nhãn (Churn 93% vs 7%).
    """
    model = Pipeline([
        ('clf', LogisticRegression(
            class_weight='balanced',
            random_state=42,
            max_iter=1000
        ))
    ])
    return model

if __name__ == "__main__":
    model = tao_mo_hinh_baseline()
    print("Khởi tạo mô hình Baseline thành công:", model)
