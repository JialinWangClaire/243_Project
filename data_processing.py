import json
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
EngStopWords = set(stopwords.words('english'))


#----------load book basic information----------
def load_data(file_name, head):
    count = 0
    data = []
    with open(file_name) as fin:
        for l in fin:
            d = json.loads(l)
            count += 1
            data.append(d)
            # break if reaches the specific line
            if (head is not None) and (count > head):
                break
    return data


#----------generate the glove dictionary for mapping----------
def glove_processing(file):
    glove={}
    for lines in file:
        l = lines.split()
        word = l[0]
        list0 = []
        for each in l[1:]:
            list0.append(float(each))
        glove[word] = np.array(list0)
    return glove


#----------save the book id, book name and book abstract to the dictionary----------
def book_processing(e, books, glove):
    book_dic = {}
    book_abs = {}
    for each in range(e):
        abstract = books[each]['description']
        idnum = books[each]['book_id']
        title = books[each]['title']
        if abstract != '':
            v = np.zeros(50)
            count = 0
            for word in abstract.split():
                if word.lower() in EngStopWords or len(word) <= 2:
                    pass
                else:
                    if word in list(glove.keys()):
                        v = v + glove[word]
                        count += 1
            if count != 0:
                v /= count
                book_dic[idnum] = [title, v]
        if abstract != '':
            book_abs[title] = {}
            ps = PorterStemmer()
            for word in abstract.split():
                if word in EngStopWords:
                    pass
                else:
                    rootWord = ps.stem(word)
                    try:
                        book_abs[title][rootWord] += 1
                    except:
                        book_abs[title][rootWord] = 1

    return book_dic, book_abs