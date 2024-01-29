import streamlit as st
from PIL import Image

st.set_page_config(page_title="index",layout="wide")
st.title("Goodreads Book Recommendation System")
st.subheader("History & Biography")
image = Image.open("/Users/wangjialin/Desktop/BIGPro/243project/pythonProject/history-and-biography-500px-1.png")
st.image(image, width=600)
st.write("Develop a book recommendation system using the Goodreads dataset in the interactive website format. We will employ natural language processing, regression methods, and basic front-end development technology.")

image2 = Image.open("/Users/wangjialin/Desktop/BIGPro/243project/pythonProject/2432.png")
st.image(image2, width=800)

st.sidebar.text("Web Creator: Jialin Wang")