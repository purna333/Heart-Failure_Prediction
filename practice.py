import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="My webpage",page_icon=":tada")
st.title("Hello World...:sunglasses:")
st.write("This is my 1st table using streamlit...")
st.caption("This is caption")

#table using DF
df=pd.DataFrame({
    'First col':[1,2,3,4],
    'second col' : [20,30,40,50]
})
st.dataframe(df.style.highlight_between(axis=0))

#line chart
chart=pd.DataFrame(
    np.random.randn(10,4),
    columns=['a','b','c','d']
)
st.line_chart(chart)

#Slider
x=st.slider('x',10,50)
st.write(x,'squared is',x*x)

#Input box
st.text_input("your name",key="name")
st.session_state.name

st.divider()

#check box
if st.checkbox('Show dataframe'):
    chart=pd.DataFrame(
    np.random.randn(10,4),
    columns=['a','b','c','d'])
    "show purna"
    chart

#selected box
# df=pd.DataFrame({
#     'col':['AP','TS','TAMIL','KERALA']
# })
option=st.selectbox(
    'Which one do you like',
    (['APS','TG','TAMIL','KERALA'])
)
'selected: ',option


s=st.selectbox(
    'select 0 or 1',
    (['0','1'])
)

#radio button
l_col,r_col=st.columns(2)
l_col.button('Press me!')
l_col.button('click')
with r_col:
    chosen=st.radio(
        'sorting tech',('selection','insertion','bubble')
    )
    st.write(f"you select this {chosen}!!!")


# st.link_button("go to fb",url)
c=st.color_picker("choose a color")
c
 
st.code("1234,f,gb,b")

st.text_input("text")

st.time_input("time")

st.date_input("date")

prompt=st.chat_input("say smthng")
if prompt:
    st.write(f"the user sent: {prompt}")

data=st.file_uploader("upload csv file")
data

st.write("[learn more >](https://pythonandvba.com)")

# st.camera_input("take a shot")
# st.image("C:\Users\varma\OneDrive\Pictures\Marshmello-e7c9b5c1-3651-4e64-ac03-b12570c1d53e.jpg")

