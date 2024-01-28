import streamlit as st

st.set_page_config(layout="wide")
st.title("Goodreads Book Recommendation System: sale predictions")
st.write("The third part is to do future book sale predictions. Based on historical book sale statistics, we use linear or nonlinear regression to predict future sale amounts. Of course, we can add filters to the website, to focus on different types of books.")

st.sidebar.text("Web Creator: Jialin Wang")