import streamlit as st

st.set_page_config(layout="wide")
st.title("Goodreads Book Recommendation System: keywords matching")
st.write("The first part is to find the most relevant books according to keyword searching. For instance, if we search for “dragon”, books that mention “dragon” most frequently in the abstract and title will appear in the search result in descending order.")

dic = {'a':['dog','monkey','pig','dragon'], 'b':['snake','horse','sheep','monkey','rat','tiger'], 'c':['pig','tiger','dragon','horse','dog']}
word = st.text_input('Keyword')
st.write('Here are the most relevant books with the keyword:', word)
for each in dic.keys():
    if word in dic[each]:
        st.write(each)