from pathlib import Path
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import string
import nltk
import numpy as np
nltk.download('punkt')


class Word:
    TF = 0
    IDF = 0
    listaFajlova = []
    N = 0

    def __init__(self, word, TF, ukupBrojFajlova, listaFajlova):
        self.word = word
        self.TF = TF
        self.listaFajlova = listaFajlova
        self.N = ukupBrojFajlova

    # def k(self, listaFajlova):
    #     brojac = 0
    #     for fajl in listaFajlova:
    #         currText = fajl.read()
    #         allWordsinCurrFile = snowball_stemmer.word_tokenize(currText)
    #         for rec in allWordsinCurrFile:
    #             if(self.word == rec):
    #                 br += 1
    #                 break
    #     return brojac
    #
    # def getIDF(self):
    #    IDF = np.log(N/self.k(listaFajlova))
    #    return IDF
    #
    # def wordScore():
    #     return TF*getIDF


corpusPath = input()
allTxtPaths = list(Path(corpusPath).rglob("*.[tT][xX][tT]"))  # get all txt paths from corpus
snowball_stemmer = SnowballStemmer(language="english")

# loading all files
listaFajlova = []
for x in allTxtPaths:  # opening all files in corpus
    f = open(x)
    listaFajlova.append(f)
ukupBrojFajlova = len(listaFajlova)

# specific file stuff
spFilePath = input()
spFile = open(str(spFilePath))
wordsInSpFile = word_tokenize(spFile.read())
spFileStemmedWords = []  # lista korenovanih reci iz specificnog fajla

for x in wordsInSpFile:
    if(x.isalnum()):
        w = snowball_stemmer.stem(x)
        spFileStemmedWords.append(w)

freqCounter = Counter(spFileStemmedWords)
listaReciSpFajla = [Word(key, value, ukupBrojFajlova, None)
                    for key, value in freqCounter.items()]
listaReciSpFajla.sort(key=lambda Word: Word.TF, reverse=True)  # sort by freq
