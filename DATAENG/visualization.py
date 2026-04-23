import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def plot_price_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["price"], bins=50, kde=True)
    plt.title("Price Distribution")
    plt.show()


def plot_price_vs_points(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="price", y="points", data=df)
    plt.title("Price vs Rating")
    plt.show()


def plot_country_counts(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(y="country", data=df, order=df["country"].value_counts().index[:10])
    plt.title("Top Wine Producing Countries")
    plt.show()


def plot_correlation(df):
    plt.figure(figsize=(6, 4))
    sns.heatmap(df[["price", "points"]].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()
