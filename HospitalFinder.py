import streamlit as st
import pandas as pd
import geocoder
import geopy.distance

def get_current_location():
    # Get location using IP
    g = geocoder.ip('me')
    return g.latlng

def fetch_closest_washroom(lat, lon, df):
    closest_washroom = None
    min_distance = float('inf')  # Initialize with a very large number
    for _, row in df.iterrows():
        dist = geopy.distance.distance((lat, lon), (row['latitude'], row['longitude'])).km
        if dist < min_distance:
            min_distance = dist
            closest_washroom = row
    return closest_washroom

def main():
    # Correcting column names and loading washrooms data
    df_washrooms = pd.read_csv('Hospitals.csv')
    df_washrooms.columns = df_washrooms.columns.str.strip()  # Removing any trailing spaces in column names

    st.title('Welcome to the Hackathon Project')
    st.header('Hospital Finder')



    

    if st.button("Use Current Location", key="hospital_finder_button"):
        latlng = get_current_location()
        if latlng:
            closest_washroom = fetch_closest_washroom(latlng[0], latlng[1], df_washrooms)
            if closest_washroom is not None:
                st.write(f"Closest Hospital: {closest_washroom['facility']}")
                st.write(f"Address :({closest_washroom['address']})")
                st.write(f"Insurence Accepted: {closest_washroom['insurances_accepted']}")
            else:
                st.error("No Hospitals found near your current location.")
        else:
            st.error("Could not determine your current location.")
