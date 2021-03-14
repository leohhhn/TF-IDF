from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import string

ss = SnowballStemmer(language="english")


class Word:
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency


f = open("lol.txt")

fileText = f.read()
translateDict = str.maketrans('', '', string.punctuation)
fileWords = fileText.translate(translateDict)
# removing punctuation from text
fileWords = fileWords.split()  # splitting text with whitespace
stemmed_words = []

for x in fileWords:  # stemming words
    if(x.isalnum()):
        w = ss.stem(x)
        stemmed_words.append(w)

c = Counter(stemmed_words)

listaReci = [Word(key, value) for key, value in c.items()]
# make list of Words
listaReci.sort(key=lambda Word: Word.frequency, reverse=True)  # sort by freq

for w in listaReci:
    print(w.word + " " + str(w.frequency))
