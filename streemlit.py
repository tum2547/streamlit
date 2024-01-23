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
   st.image("https://c.pxhere.com/photos/73/a2/potato_flowers_petals_stamens_flower_plant_yellow_rosa_nature-1288559.jpg!d")

#import pandas as pd
df=pd.read_csv("./data/iris.cav")
st.write(df.head(10))

st.write(df.groupby('variety').mean())
chart_data=df.groupby('variety').mean()
chart_data.columns

chart_data = pd.DataFrame(
   {
       "col1": df['variety'],
       "col2": df['sepal.width'],
       "col3": df['sepal.length']
    
    }
)

st.bar_chart(chart_data, x="col1", y=["col2","col3"], color=["#FF0000", "#0000FF"])