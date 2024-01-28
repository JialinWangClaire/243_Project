from data_processing import load_data
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
EngStopWords = set(stopwords.words('english'))
from matplotlib import pyplot as plt
from collections import Counter

e = 40 # lines to train
books = load_data('goodreads_books_history_biography.json',head = e)
#----------Frequency Comparison----------
before = []
after = []
count = 0
map = []
total = ''
for each in range(e):
    abstract = books[each]['description']
    if abstract != '':
        count += 1
        print("Before NLP:", abstract)
        print("Number of Words:", len(abstract))
        before.append(len(abstract))
        s = ''
        ps = PorterStemmer()
        for word in abstract.split():
            if word.lower() in EngStopWords or len(word) <= 2:
                pass
            else:
                rootWord = ps.stem(word)
                s = s + rootWord + ' '
                total = total + rootWord + ' '
                map.append(rootWord)
        print("After NLP:", s)
        print("Number of Words:", len(s))
        after.append(len(s))
plt.plot(range(count),before,label='before nlp')
plt.plot(range(count),after,label='after nlp')
plt.legend()
plt.ylabel('Number')
plt.xlabel('Book index')
plt.title('Number of words before and after nlp')
plt.show()

#----------Word Map----------
word_counts = Counter(map)
most_common_words = word_counts.most_common(10)
print("Top 10 most common root words in the first 40 books:")
for word, count in most_common_words:
    print(f"{word}: {count} times")

from wordcloud import WordCloud

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(total)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
