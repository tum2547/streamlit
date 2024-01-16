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