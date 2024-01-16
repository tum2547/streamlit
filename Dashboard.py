import streamlit as st
import pandas as pd

# สร้างแดชบอร์ด
st.title("ทดสอบการใช้งาน Streamlit")

st.header("Header")
st.subheader('Raw data')

# แสดงความ
st.write("testing")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

df = pd.read_csv(url)
st.write(df.head(10))
st.write(df.shape)

df2 = df.groupby('species')['body_mass_g'].mean()
st.write(df2)
st.bar_chart(df2)

genre = st.radio(
     "คุณชอบหนังอะไร",
    ('การ์ตูน', 'ดร่าม่า', 'หนังสือพม'))

st.write(f"You selected {genre}")

option = st.selectbox(
   "How would you like to be contacted?",
   ("Email", "Home phone", "Mobile phone"),
   index=None,
   placeholder="Select contact method...",
)

st.write('You selected:', option)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)