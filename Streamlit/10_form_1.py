import streamlit as st

st.title("Form Method-01")
st.subheader("User Registration Method-01")
form = st.form("My Form")
form.text_input(label="Enter Name", placeholder="Name")
form.form_submit_button(label="SUBMIT")
st.markdown("---")


st.title("Form Method-02")
st.markdown(
    "<h1 style = 'text-align:center;'>User Registration</h1>", unsafe_allow_html=True
)
with st.form("Your Form"):
    Col_1, Col_2 = st.columns(2)
    Col_1.text_input(label="First Name", placeholder="John")
    Col_2.text_input(label="Last Name", placeholder="Doe")
    st.text_input(label="Email", placeholder="example@gmail.com")
    st.text_input("Password", type="password")
    st.text_input("Retype Password", type="password")
    st.form_submit_button(label="SubMit")
