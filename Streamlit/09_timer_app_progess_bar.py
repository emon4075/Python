import streamlit as st
import time

st.title("Progress Bar")
bar = st.progress(0, text="Please Wait")
for i in range(100):
    if i > 50:
        bar.progress(i)
        time.sleep(0.01)
    else:
        bar.progress(i)
        time.sleep(0.1)
