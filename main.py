import json

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

with open('categories.json', 'r') as fp:
    categories = json.loads(fp.read())
stemmer = PorterStemmer()


def preprocess(sentence):
    words = word_tokenize(sentence)
    words = [stemmer.stem(word) for word in words]
    _stopwords = set(stopwords.words('english'))
    return {word for word in words if word not in _stopwords}


def getCategoryCount(question):
    processed_words = preprocess(question)
    category_count = {}
    for category, words in categories.iteritems():
        for word in words:
            if word in processed_words:
                category_count[category] = category_count.get(category, 0)+1
    return category_count


def getClassifiedCategories(category_count):
    categories, max_count = [], 0
    for category, count in category_count.iteritems():
        if max_count < count:
            categories = [category]
            max_count = count
        elif max_count == count:
            categories.append(category)
    return categories


# question = raw_input()
# category_count = getCategoryCount(question)
# print getClassifiedCategories(category_count)
