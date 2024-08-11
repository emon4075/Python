import streamlit as st
import pandas as pd


st.title("Check Box")
state = st.checkbox("Check Me")
if state:
    st.success("Checked")
else:
    pass
st.markdown("---")

st.title("Radio Button")
radio_button = st.radio("Choose You Option?", options=("A", "B", "C"))
st.write(radio_button)
st.markdown("---")


st.title("Select Box")
select_box = st.selectbox("Choose Car", options=("BMW", "NISSAN", "FORD"))
st.success(select_box)
st.markdown("---")


st.title("Multi Select")
multi_select = st.multiselect(
    "Choose Any Three?", options=("BMW", "NISSAN", "FORD", "TOYOTA", "MAZADA")
)
st.write(multi_select)
df = pd.DataFrame(multi_select)
st.write(df)
st.markdown("---")

st.title("Button")
submit = st.button("Submit")
if submit:
    f = open("i.txt", "w")
    f.write(df.to_string())
    f.write(select_box)
    f.close()
else:
    pass
