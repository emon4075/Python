import streamlit as st

st.title("Image")
st.image("E:\Python\Streamlit\Image.jpg", caption="My PC")
st.markdown("---")

st.title("Video")
st.video("E:\Python\Streamlit\Video.mp4", autoplay=True, muted=True)
st.markdown("---")

st.title("Audio")
st.audio("E:\Python\Streamlit\Audio.mp3", autoplay=True)
st.markdown("---")
