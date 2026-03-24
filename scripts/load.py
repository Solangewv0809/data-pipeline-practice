import pandas as pd

def load_data(df):
    df.to_csv("data/processed_data.csv", index=False)
    print("Data loaded successfully")

if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data

    df = extract_data()
    df = transform_data(df)
    load_data(df)
