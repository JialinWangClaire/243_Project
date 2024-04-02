import streamlit as st
import pickle
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

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
     values = st.slider(
          'Select a range of years',
          2005, 2018, (2010, 2018))
     st.write('Years:', values)
     sales_data = {
          'Year': list(range(2005, 2019)),
          'Sales': p
     }
     df = pd.DataFrame(sales_data)

     # Function to get sales for a specific range of years
     def get_sales_for_range(start_year, end_year):
          filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
          return filtered_df['Sales']

     start_year = values[0]
     end_year = values[1]
     sales_for_range = get_sales_for_range(start_year, end_year)
     st.markdown(
          "<p style='font-family: Arial; font-size: 18px; color: orange;'>Here is the sales line chart for you!</p>",
          unsafe_allow_html=True)
     # Plotting the array using Matplotlib
     fig, ax = plt.subplots(figsize=(6, 3))
     ax.plot(range(start_year,end_year+1) ,sales_for_range.tolist(), marker='o')
     ax.set_xlabel('Year')
     ax.set_ylabel('Sale')
     ax.set_title('Sale prediction')
     ax.grid(True)

     # Display the plot in Streamlit
     st.pyplot(fig)
except:
     st.write("Sorry, the book is not in record now.")

