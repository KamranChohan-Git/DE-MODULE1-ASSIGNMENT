import os


def create_directory(path: str):
    """Create directory if it does not exist."""
    os.makedirs(path, exist_ok=True)
    print(f"📁 Directory ensured: {path}")


def save_data(df, output_path: str):
    """Save dataframe to CSV."""
    df.to_csv(output_path, index=False)
    print(f"✅ File saved to {output_path}")
