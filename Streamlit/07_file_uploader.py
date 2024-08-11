import streamlit as st
import pandas as pd

st.title("File Uploader")
files = st.file_uploader(
    "Upload Your Files", type=["json", "jpg", "mp4"], accept_multiple_files=True
)

if files:
    for file in files:
        if file.name.endswith(".mp4"):
            st.video(file)

        elif file.name.endswith(".jpg"):
            st.image(file)

        elif file.name.endswith(".json"):
            json_data = pd.read_json(file)
            st.write(json_data)
else:
    pass
