import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_trip_distance_distribution(df: pd.DataFrame):
    """Plot distribution of trip distances."""
    plt.figure(figsize=(8,5))
    sns.histplot(df['trip_distance'], bins=50, kde=True)
    plt.title("Distribution of Trip Distances")
    plt.xlabel("Distance (miles)")
    plt.ylabel("Count")
    plt.show()
