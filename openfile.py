from pathlib import Path
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import string
import nltk
nltk.download('punkt')


class Word:
    TF = 0
    IDF = 0

    def __init__(self, word, TF):
        self.word = word
        self.TF = TF

    tf_idf = TF*IDF


def k(Word, listaFajlova):
    brojac = 0
    for fajl in listaFajlova:
        currText = fajl.read()
        allWordsinCurrFile = snowball_stemmer.word_tokenize(currText)
        for rec in allWordsinCurrFile:
            if(Word.word == rec):
                br += 1
                break
    return brojac


# corpusPath = input()
# allTxtPaths = list(Path(corpusPath).rglob("*.[tT][xX][tT]"))
# get all txt paths from corpus
spFilePath = input()
snowball_stemmer = SnowballStemmer(language="english")
spFile = open(str(spFilePath))

wordsInSpFile = word_tokenize(spFile.read())

spFileStemmedWords = []  # lista korenovanih reci iz specificnog fajla

for x in wordsInSpFile:
    if(x.isalnum()):
        w = snowball_stemmer.stem(x)
        spFileStemmedWords.append(w)

freqCounter = Counter(spFileStemmedWords)
listaReciSpFajla = [Word(key, value) for key, value in freqCounter.items()]
listaReciSpFajla.sort(key=lambda Word: Word.TF, reverse=True)
# sort by freq

for w in listaReciSpFajla:
    print(w.word + " " + str(w.TF))


# listaReci = [Word(key, value, 0) for key, value in c.items()]
# make list of Words
# listaReci.sort(key=lambda Word: Word.TF, reverse=True)  # sort by freq
