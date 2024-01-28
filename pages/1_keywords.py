import streamlit as st
import pickle
from itertools import islice
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
EngStopWords = set(stopwords.words('english'))

st.set_page_config(layout="wide")
st.title("Goodreads Book Recommendation System: keywords matching")
st.write("The first part is to find the most relevant books according to keyword searching. For instance, if we search for “dragon”, books that mention “dragon” most frequently in the abstract will appear in the search result in descending order.")


with open('/Users/wangjialin/Desktop/BIGPro/243project/pythonProject/book_abs.pickle', 'rb') as f:
    book_abs = pickle.load(f)

# matching step
word = st.text_input('Keyword')
if word in EngStopWords:
    st.write("Invalid stopword search")
else:
    ps = PorterStemmer()
    rootWord = ps.stem(word)
    st.write("Here are the most relevant books with the keyword:", word)
    flag = 0
    origin = {}
    for i in book_abs.keys():
        if rootWord in book_abs[i].keys():
            origin[i] = book_abs[i][rootWord]
            flag = 1
    new = dict(sorted(origin.items(), key=lambda item: item[1], reverse=True))
    first_10_items = dict(islice(new.items(), 10))
    for key, value in first_10_items.items():
        st.write(key, value)
    if flag == 0:
        st.write("Empty Search")

st.sidebar.text("Web Creator: Jialin Wang")