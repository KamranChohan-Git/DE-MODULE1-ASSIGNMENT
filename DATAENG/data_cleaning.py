def clean_data(df):
    """Handle missing values and clean dataset."""

    # Fill missing values
    df["country"].fillna("Unknown", inplace=True)
    df["price"].fillna(df["price"].median(), inplace=True)

    # Drop unnecessary columns
    if "region_2" in df.columns:
        df.drop(columns=["region_2"], inplace=True)

    print("Data cleaning completed")
    return df
