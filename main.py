# main back-end function
from data_processing import load_data, glove_processing, book_processing
import pickle


def main_function():
    e = 1000 # lines to train
    books = load_data('goodreads_books_history_biography.json',head = e)

    file = open('glove.6B.50d.txt','r')
    glove = glove_processing(file)

    book_dic, book_abs = book_processing(e, books, glove)

    return book_dic, book_abs

book_dic, book_abs = main_function()

# pickle dump
with open('book_dic.pickle', 'wb') as handle:
    pickle.dump(book_dic, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('book_abs.pickle', 'wb') as handle:
    pickle.dump(book_abs, handle, protocol=pickle.HIGHEST_PROTOCOL)


