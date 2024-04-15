import folium
from streamlit_folium import st_folium

def show_map(lat, lon, washrooms):
    map_ = folium.Map(location=[lat, lon], zoom_start=14)
    folium.Marker([lat, lon], tooltip='Your Location', icon=folium.Icon(color='blue')).add_to(map_)
    for index, row in washrooms.iterrows():
        folium.Marker(
            [row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            popup=f"{row['Name']} - Details: {row['Address']}"
        ).add_to(map_)
    return map_
