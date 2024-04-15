import streamlit as st
import WashroomFinder as WashroomFinder  # Script for finding washrooms
import HospitalFinder as HospitalFinder  # Script for finding hospitals
import CrimeLocalityFinder as CrimeLocalityFinder  # Script for finding danger spots
import WashroomFinderCoordinates as WashroomFinderCoordinates  # Additional script for testing washrooms coordinates


# Sidebar for navigation
st.sidebar.title('Navigation')
option = st.sidebar.radio('Choose a service:',
                          ('Home',
                           'Find Nearby Washrooms',
                           'Find Nearby Hospitals',
                           'Find Nearby Danger Spots',
                           'Test Washroom Finder'))

if option == 'Home':
    st.subheader("Welcome to the Community Assistance Portal")
    st.write("Please select an option from the sidebar to find nearby facilities or check areas for safety.")
elif option == 'Find Nearby Washrooms':
    WashroomFinder.main()
elif option == 'Find Nearby Hospitals':
    HospitalFinder.main()
elif option == 'Find Nearby Danger Spots':
    CrimeLocalityFinder.main()
elif option == 'Test Washroom Finder':
    WashroomFinderCoordinates.main()
