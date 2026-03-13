import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Smart Energy Monitoring Dashboard")

df = pd.read_csv("energy_data.csv")

st.subheader("Energy Data")
st.write(df)

st.subheader("Power Usage Chart")
plt.plot(df["Power"])
plt.xlabel("Reading")
plt.ylabel("Power")
st.pyplot(plt)
