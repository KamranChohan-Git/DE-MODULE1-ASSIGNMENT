def inspect_data(df):
    """Display basic dataset information."""
    print("\n📊 Dataset Shape:", df.shape)
    print("\n📌 Columns:", df.columns.tolist())
    print("\n🧾 Info:")
    print(df.info())
    print("\n📈 Summary Statistics:")
    print(df.describe())


def check_missing(df):
    """Check missing values."""
    missing = df.isnull().sum().sort_values(ascending=False)
    print("\n⚠️ Missing Values:\n", missing[missing > 0])