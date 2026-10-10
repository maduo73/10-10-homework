import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")

st.title("World Cities")

df = pd.read_csv("worldcities.csv")

population_filter = st.slider(
    "Minimal Population (Millions):", 0.0, 40.0, 3.6
)

capital_options = [value for value in df["capital"].dropna().unique()]
capital_filter = st.sidebar.multiselect(
    "Capital Selector", capital_options, capital_options
)

form = st.sidebar.form("country_form")
country_filter = form.text_input("Country Name (enter ALL to reset)", "ALL")
form.form_submit_button("Apply")

df = df[df["population"] >= population_filter]
df = df[df["capital"].isin(capital_filter)]
if country_filter.strip().upper() != "ALL":
    df = df[df["country"].str.casefold() == country_filter.strip().casefold()]

st.map(df)
st.subheader("City Details:")
st.write(df[["city", "country", "population"]])

st.subheader("Total Population By Country")
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby("country")["population"].sum().sort_values(ascending=False)
pop_sum.plot.bar(ax=ax)
ax.set_ylabel("Population (millions)")
st.pyplot(fig)
