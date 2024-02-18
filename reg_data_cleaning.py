from data_processing import load_data
import csv
from collections import Counter

n = 500000  # lines to read
interactions = load_data('goodreads_interactions_history_biography.json', head=n)

interaction_count = {}
for each in interactions:
    try:
        interaction_count[each['book_id']].append(each['date_added'][-4:])
    except:
        interaction_count[each['book_id']] = [each['date_added'][-4:]]


count_dict = {key: len(set(value)) for key, value in interaction_count.items()}

sorted_count_dict = dict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True))
top_1000_results = dict(list(sorted_count_dict.items())[:1000])

books_to_predict = []
for key, value in top_1000_results.items():
     books_to_predict.append(key)

# Initialize an empty set for all years
all_years = set()

# Iterate through the dictionary and add each year to the set
for book_id, years in interaction_count.items():
    all_years.update(set(years))
# Sort the years
all_years = sorted(all_years)

# Initialize a Counter for each book, including all years in the fixed list
book_year_counts = {book_id: Counter(interaction_count.get(book_id, [])) for book_id in books_to_predict}

# Transpose the data for writing to CSV
transposed_data = [
    {'book_id': book_id, **{year: count[year] for year in all_years}}
    for book_id, count in book_year_counts.items()
]

# Write the results to a CSV file
csv_filename = 'book_year_counts.csv'
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['book_id'] + list(all_years))

    # Write the header
    csv_writer.writeheader()

    # Write each book's year counts
    csv_writer.writerows(transposed_data)

print(f'The book year counts have been written to {csv_filename}.')