import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://pxhere.com/th/photo/1513717?utm_content=shareClip&utm_medium=referral&utm_source=pxhere")

with col2:
   st.header("A dog")
   st.image("https://pxhere.com/th/photo/1478961?utm_content=shareClip&utm_medium=referral&utm_source=pxhere")

with col3:
   st.header("An owl")
   st.image("https://pxhere.com/th/photo/685563?utm_content=shareClip&utm_medium=referral&utm_source=pxhere")