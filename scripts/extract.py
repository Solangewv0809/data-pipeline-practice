import pandas as pd

def extract_data():
    df = pd.read_csv("data/sample_data.csv")
    print("Data extracted successfully")
    return df

if __name__ == "__main__":
    extract_data()
