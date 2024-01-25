import streamlit as st

st.set_page_config(layout="wide")
st.title("Goodreads Book Recommendation System: contents recommendation")
st.write("The second part is to find the book a specific customer will take interest in. We turn all the useful words in the book abstracts they read before into vectors and integrate vectors into a profile vector for each reader. Then we do the matching step, finding the closest distance between book vectors and profile vectors. If we type user ID 101012 on the website, the system will recommend several books he would like to read according to his reading history.")
