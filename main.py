from src.data_loader import load_data
from src.analysis import average_trip_distance, top_pickup_locations
from src.visualization import plot_trip_distance_distribution

DATA_PATH = "data/nyc_taxi_sample.csv"

def main():
    df = load_data(DATA_PATH)
    print(f"Average Trip Distance: {average_trip_distance(df):.2f} miles")
    print("Top Pickup Locations:")
    print(top_pickup_locations(df))
    plot_trip_distance_distribution(df)

if __name__ == "__main__":
    main()
