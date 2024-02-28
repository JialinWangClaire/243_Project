import streamlit as st
import pickle
from matplotlib import pyplot as plt
import numpy as np

st.set_page_config(layout="wide")
st.title("Goodreads Book Recommendation System: sale predictions")
st.write("The third part is to do future book sale predictions. Based on historical book sale statistics, we use linear or nonlinear regression to find the most important features contributing to the book popularity, and also use time series analysis to predict future sales. ")

st.sidebar.text("Web Creator: Jialin Wang")


with open('/Users/wangjialin/Desktop/BIGPro/243project/pythonProject/prediction.pickle', 'rb') as f:
    predictions = pickle.load(f)
predictions.index = predictions.index.astype(str)
book_id = st.text_input('Book_id: example: 5544, 10988, 23202')

if book_id == '':
    st.write("Empty Search")
try:
     p = predictions.loc[book_id].values
     st.write('The sale prediction for the book', book_id, 'in 2018 is:', round(p[-1]))
     # Generate years from 2005 to 2018
     years = np.arange(2005, 2019)

     # Plotting the array using Matplotlib
     fig, ax = plt.subplots(figsize=(6, 3))
     ax.plot(years ,p, marker='o')
     ax.set_xlabel('Year')
     ax.set_ylabel('Sale')
     ax.set_title('Sale prediction')

     # Display the plot in Streamlit
     st.pyplot(fig)
except:
     st.write("Sorry, the book is not in record now.")

