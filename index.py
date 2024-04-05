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

st.write("The best regression model we select to predict the total interaction count of a book is XGBoost.")
image3 = Image.open("/Users/wangjialin/Desktop/BIGPro/243project/pythonProject/2434.png")
st.image(image3, width=700)

st.write("Three most important features are ratings_count, text_reviews_count and publisher_encoded based on the F score. We can pay much attention to these features when estimating the popularity of each book.")
image4 = Image.open("/Users/wangjialin/Desktop/BIGPro/243project/pythonProject/2433.png")
st.image(image4, width=700)

st.sidebar.text("Web Creator: Jialin Wang")
st.sidebar.image("/Users/wangjialin/Desktop/BIGPro/243project/pythonProject/mcj038257400001.jpeg", use_column_width=True)
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

with st.form("my_form"):
   slider_val = st.slider("How much would you rate our website?", 1,10,8)
   feedback = st.text_input('Your suggestions')
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
if submitted:
       st.write("You rate", slider_val)
       print(slider_val, feedback)