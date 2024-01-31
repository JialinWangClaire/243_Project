import streamlit as st

st.set_page_config(layout="wide")
st.title("Goodreads Book Recommendation System: sale predictions")
st.write("The third part is to do future book sale predictions. Based on historical book sale statistics, we use linear or nonlinear regression to find the most important features contributing to the book popularity, and also use time series analysis to predict future sales. ")

st.sidebar.text("Web Creator: Jialin Wang")