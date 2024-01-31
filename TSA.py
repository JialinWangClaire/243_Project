import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings
import pickle

# Load the CSV file into a DataFrame
csv_filename = 'book_year_counts.csv'
df = pd.read_csv(csv_filename)

# Set the 'book_id' column as the index
df.set_index('book_id', inplace=True)

# Order for the ARIMA model
order = (1, 1, 1)  # You might need to adjust the order based on your data

# Ignore warnings
warnings.filterwarnings("ignore")

# Iterate over each row in the DataFrame
for book_id, sales_data in df.iterrows():
    sales_data = sales_data.dropna()

    # Convert the 'year' columns to datetime and set them as an index
    sales_data.index = pd.to_datetime(sales_data.index, format='%Y')

    # Fit an ARIMA model with explicit frequency
    model = ARIMA(sales_data, order=order)
    fit_model = model.fit()

    # Make predictions for the year 2018
    predictions = fit_model.predict(start=len(sales_data), end=len(sales_data) + 1, typ='levels')
    df.loc[book_id, '2018'] = predictions.values[0]

print(df)
# pickle dump
with open('prediction.pickle', 'wb') as handle:
    pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)