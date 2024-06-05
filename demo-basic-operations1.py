import streamlit as st
st.title("hello,2208!")
st.header("首页")
st.subheader("动态")
st.text("hhhhhhh")
st.markdown("this is an image:\n ![](https://static-data.gaokao.cn/upload/school/202119/1618799669_7967_thumb.jpg)")
if st.checkbox("show/Hide"):
    st.text("You checked the box")
status=st.radio("select gender:",('Male','Female'))
if status == 'Male':
    st.success("Male")
else:
    st.success("Famale")
hobbies=st.multiselect("Hobbies",['Reading','Writing','Coding','Traveling'])
st.write("You selected:",hobbies)
if st.button("about"):
    st.text("Streamlit is a great tool")
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("hello,",name)
level=st.slider("Select your level",1,5)
st.write("you select:",level)
from fastai.vision.all import *
upload_img=st.file_uploader("upload an image",type=['jpg','png'])
if upload_img is not None:
    img=PILImage.create(upload_img)
    st.image(img.to_thumb(256,256),caption="uploaded image")