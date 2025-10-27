import pandas as pd

def average_trip_distance(df: pd.DataFrame) -> float:
    """Calculate average trip distance."""
    return df['trip_distance'].mean()

def top_pickup_locations(df: pd.DataFrame, n=5):
    """Get top N pickup locations."""
    return df['PULocationID'].value_counts().head(n)
