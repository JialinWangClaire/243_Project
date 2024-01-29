from data_processing import load_data, glove_processing
import numpy as np
from nltk.corpus import stopwords
EngStopWords = set(stopwords.words('english'))
import pickle
from nltk.stem import PorterStemmer
from wordcloud import WordCloud
from matplotlib import pyplot as plt

n = 500  # lines to read
interaction = load_data('goodreads_interactions_history_biography.json', head=n)

p = 3 # number of people in the demo
interaction_dic = {}
for each in interaction:
    if len(interaction_dic.keys()) == p+1:
        break
    if  each['rating'] >= 5 and each['is_read'] == True:
        try:
            interaction_dic[each['user_id']].append(each['book_id'])
        except:
            interaction_dic[each['user_id']] = []

interaction_dic = {k: v for k, v in interaction_dic.items() if k != list(interaction_dic.keys())[-1]}



e = 300000  # lines to read the abstracts
books = load_data('goodreads_books_history_biography.json', head = e)
abstracts = {}
for person in interaction_dic.keys():
    for each in range(e):
        if books[each]['book_id'] in interaction_dic[person]:
            try:
                abstracts[person].append(books[each]['description'])
            except:
                abstracts[person] = []


#----------Reader Profile Visualization----------
# for each in abstracts.values():
#     print(len(each))
total = ''
ps = PorterStemmer()
for group in abstracts.values():
    total = ''
    for text in group:
        for word in text.split():
            if word.lower() in EngStopWords or len(word) <= 2:
                pass
            else:
                rootWord = ps.stem(word)
                total = total + rootWord + ' '
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(total)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


# NLP-build person profile
file = open('glove.6B.50d.txt', 'r')
glove = glove_processing(file)
profiles = {}
for person in abstracts.keys():
    nv = np.zeros(50)
    count2 = 0
    for each in abstracts[person]:
        if each != '':
            v = np.zeros(50)
            count = 0
            for word in each.split():
                if word.lower() in EngStopWords or len(word) <= 2:
                    pass
                else:
                    if word in list(glove.keys()):
                        v = v + glove[word]
                        count += 1
            if count != 0:
                v /= count
            nv = nv + v
            count2 += 1
            if count2 != 0:
                nv /= count2
    profiles[person] = nv
print(profiles)

# pickle dump
with open('profiles.pickle', 'wb') as handle:
    pickle.dump(profiles, handle, protocol=pickle.HIGHEST_PROTOCOL)