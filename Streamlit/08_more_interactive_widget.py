from PIL import Image
import streamlit as st

st.title("Slider")
slider_value = st.slider("Choose Range", min_value=10, max_value=200, step=50)
st.write(slider_value)
st.markdown("---")

st.title("Text Input")
name = st.text_input("Enter Your Name", max_chars=100, placeholder="Name")
st.write(name)
st.markdown("---")


st.title("Text Area")
message = st.text_area(
    label="Enter Message", height=200, max_chars=500, placeholder="Message"
)
st.write(message)
st.markdown("---")


st.title("Date Input")
date = st.date_input(label="Enter Date")
st.write(date)
st.markdown("---")


st.title("Time Input")
time = st.time_input("Enter Time")
st.write(time)
st.markdown("---")

st.title("Capture Image")
me = st.camera_input(label="Get You Image")
if me:
    image = Image.open(me)
    st.image(image)
    image.save("captured_image.png")
else:
    pass
