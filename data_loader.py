import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load NYC taxi data from CSV."""
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} rows.")
    return df
