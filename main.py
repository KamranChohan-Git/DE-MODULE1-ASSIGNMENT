from DATAENG.data_loader import load_data
from DATAENG.data_cleaning import clean_data
from DATAENG.eda import inspect_data, check_missing
from DATAENG.visualization import (
    plot_price_distribution,
    plot_price_vs_points,
    plot_country_counts,
    plot_correlation
)
from DATAENG.utils import save_data, create_directory


def main():
    # Paths
    input_path = "data/raw/winemag-data_first150k.csv"
    output_path = "data/processed/cleaned_wine_data.csv"

    # Ensure processed folder exists
    create_directory("data/processed")

    # Load data
    df = load_data(input_path)

    # EDA (basic)
    inspect_data(df)
    check_missing(df)

    # Clean data
    df = clean_data(df)

    # Visualizations
    plot_price_distribution(df)
    plot_price_vs_points(df)
    plot_country_counts(df)
    plot_correlation(df)

    # Save cleaned dataset
    save_data(df, output_path)


if __name__ == "__main__":
    main()