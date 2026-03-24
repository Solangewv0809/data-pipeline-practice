import pandas as pd
from scripts.transform import transform_data

def test_transform():
    sample_data = pd.DataFrame({
        "Name ": ["Alice", "Bob", None],
        "Age": [25, 30, 22]
    })

    result = transform_data(sample_data)

    assert "name" in result.columns
    assert result.isnull().sum().sum() == 0
