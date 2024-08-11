import streamlit as st

st.title("Markdown")
st.markdown("**Hello** *World*\n" "- One\n" "- Two\n" "- Three\n")
st.markdown(
    """
    ```
    {
        "firstName":"Abdullah"
        "lastName":"Emon"
    }
    ```
    """
)

st.markdown(
    """
    ```
    print("Hello World")
    for x in range(10):
        print(x)
    ```
    """
)

st.markdown("`print('Hello World')`")
st.markdown("---")


st.title("LaTeX")
st.latex(r"\begin{pmatrix}a & b \\ c & d \end{pmatrix}")
st.markdown("---")



st.title("JSON")
jsonDict = {"Number": [1, 2, 3], "Name": "Emon,Remon"}
st.json(jsonDict)
st.markdown("---")



st.title('CODE')
code = """
print("Hello World")
for i in range(10):
    print(i)
def function():
    return 0
"""
st.code(code,language="python")