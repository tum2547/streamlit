import streamlit as st
import pandas as pd
import datetime

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

        number = st.number_input('Insert a number')
st.write('The current number is ', number)
number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write('The current number is ', number)

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)
today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)
d

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)
t = st.time_input('Set an alarm for', value=None)
st.write('Alarm is set for', t)

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))