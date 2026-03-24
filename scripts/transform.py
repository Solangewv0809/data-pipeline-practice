def transform_data(df):
    # Example: clean column names
    df.columns = [col.lower().strip() for col in df.columns]

    # Example: drop missing values
    df = df.dropna()

    print("Data transformed successfully")
    return df
