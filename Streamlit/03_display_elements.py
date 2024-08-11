import streamlit as st
import pandas as pd


st.title("Write")
st.write("### H3")
st.markdown("---")


st.title("Metric Funtion")
st.metric(label="Wind Speed", value="141ms⁻¹", delta="-1.4ms⁻¹")
st.write("---")

st.title("Data Frame")
st.subheader("Table")
df = pd.read_json("E:\Python\Streamlit\data.json")
st.table(df)

st.subheader("Data Frame")
st.dataframe(df)
st.markdown("---")
