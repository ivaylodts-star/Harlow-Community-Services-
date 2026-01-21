import streamlit as st
import pandas as pd

# Load your data
@st.cache_data
def load_data():
    return pd.read_csv("services.csv")

df = load_data()

st.title("Patient Service Browser")

# Search bar
search_query = st.text_input("Search for a service or location:")

# Filter logic
if search_query:
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
else:
    filtered_df = df

# Display data
st.dataframe(filtered_df, use_container_width=True)
