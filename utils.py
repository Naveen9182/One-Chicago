import pandas as pd
from math import radians, cos, sin, sqrt, atan2

def load_washrooms():
    # Load the Excel file into a DataFrame
    df = pd.read_csv('/Bathrooms_Chicago.csv')
    return df

def calculate_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def find_nearest_washroom(lat, lon):
    washrooms_df = load_washrooms()
    washrooms_df['Distance'] = washrooms_df.apply(
        lambda row: calculate_distance(lat, lon, row['Latitude'], row['Longitude']),
        axis=1
    )
    nearest_washroom = washrooms_df.loc[washrooms_df['Distance'].idxmin()]
    return nearest_washroom
