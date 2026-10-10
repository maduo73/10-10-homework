import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="California Housing Data", layout="wide")
st.title("California Housing Data (1990) by maqichen")

df = pd.read_csv("housing.csv")

min_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000,
)

st.subheader("See more filters in the sidebar:")
locations = st.sidebar.multiselect(
    "Choose the location type",
    options=sorted(df["ocean_proximity"].dropna().unique()),
    default=sorted(df["ocean_proximity"].dropna().unique()),
)
income_level = st.sidebar.radio(
    "Choose income level", ["Low", "Medium", "High"]
)

filtered = df[df["median_house_value"] >= min_value]
filtered = filtered[filtered["ocean_proximity"].isin(locations)]

if income_level == "Low":
    filtered = filtered[filtered["median_income"] <= 2.5]
elif income_level == "Medium":
    filtered = filtered[
        (filtered["median_income"] > 2.5) & (filtered["median_income"] < 4.5)
    ]
else:
    filtered = filtered[filtered["median_income"] >= 4.5]

st.map(filtered, latitude="latitude", longitude="longitude")

st.subheader("Median House Value Distribution")
fig, ax = plt.subplots()
ax.hist(filtered["median_house_value"], bins=30, edgecolor="white")
ax.set_xlabel("Median house value (USD)")
ax.set_ylabel("Number of districts")
st.pyplot(fig)
