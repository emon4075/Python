import streamlit as st
from PIL import Image

st.title("First Web App")

st.header("This is a Header")
st.subheader("This is a Sub Header")
st.write("Hello World")
st.text("Gello World")
st.markdown("### This is a Markdown")
st.success("Congo")
st.warning("Not Congo")
st.info("Information")
st.error("Error")
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)
for i in range(10):
    st.write(i)
img = Image.open("E://Python//CS50//Lecture6//Final.gif")
st.image(img, width=200)

st.checkbox("Show")

if st.checkbox("Hello"):
    st.text("Hello world")

name = st.text_input("Enter Text", placeholder="Name")
st.write("Hello", name)
ame = st.text_input("Enter Text", placeholder="Name", type="password")
st.write("Hello", ame)
