import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://c.pxhere.com/photos/ae/e9/beautiful_bloom_blooming_blossom_blue_blur_botanical_bright-1513717.jpg!d")

with col2:
   st.header("A dog")
   st.image("https://c.pxhere.com/photos/c6/13/bluebell_flower_virginia_bluebell_blooming_blossom_wildflower_floral-770483.jpg!d")

with col3:
   st.header("An owl")
   st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bualabs.com%2Farchives%2F3285%2Fteach-tensorflow-js-build-multi-class-classification-machine-learning-iris-classifier-tabular-data-neural-network-2-dense-layers-tfjs-ep-2%2F&psig=AOvVaw3eqiXsNpf4VUqDywZTjXH5&ust=1706083030574000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNimmN-E84MDFQAAAAAdAAAAABAY")