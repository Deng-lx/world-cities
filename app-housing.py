import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("California Housing Data (1990) by Deng-lx")

housing = pd.read_csv("housing.csv")

min_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000,
)

filtered = housing[housing["median_house_value"] >= min_value]

st.subheader("See more filters in the sidebar:")

location_types = sorted(housing["ocean_proximity"].dropna().unique())

selected_locations = st.sidebar.multiselect(
    "Choose the location type",
    location_types,
    default=location_types,
)

filtered = filtered[filtered["ocean_proximity"].isin(selected_locations)]

income_level = st.sidebar.radio(
    "Choose income level",
    ["Low", "Medium", "High"],
)

if income_level == "Low":
    filtered = filtered[filtered["median_income"] <= 2.5]
elif income_level == "Medium":
    filtered = filtered[
        (filtered["median_income"] > 2.5)
        & (filtered["median_income"] < 4.5)
    ]
else:
    filtered = filtered[filtered["median_income"] >= 4.5]

st.map(filtered[["latitude", "longitude"]])

fig, ax = plt.subplots()
ax.hist(filtered["median_house_value"], bins=30)
ax.set_xlabel("Median House Value")
ax.set_ylabel("Number of Districts")
ax.set_title("Distribution of Median House Value")
st.pyplot(fig)