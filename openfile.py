from pathlib import Path
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import numpy as np


class Word:

    TF = 0
    IDF = 0
    ukupBrojFajlova = 0
    listaProcitanihFajlova = []

    def __init__(self, word, TF, ukupBrojFajlova, listaProcitanihFajlova):
        self.word = word
        self.TF = TF
        self.listaFajlova = listaProcitanihFajlova
        self.ukupBrojFajlova = ukupBrojFajlova
        self.IDF = np.log(ukupBrojFajlova / self.k(listaProcitanihFajlova))

    def wordScore(self):
        return self.TF * self.IDF


corpusPath = input()
allTxtPaths = list(Path(str(corpusPath)).rglob("*.[tT][xX][tT]"))  # get all txt paths from corpus
snowball_stemmer = SnowballStemmer(language="english")


wordMap = {}

for x in allTxtPaths:  # opening all files in corpus
    with open(x, 'r') as f:
        currFileText = f.read()
        currFileWords = word_tokenize(currFileText)
        for rec in currFileWords:
            if(rec.isalnum()):
                rec = snowball_stemmer.stem(rec)
                if(rec not in wordMap):
                    wordMap[rec] = {}
                if(f.name not in wordMap[rec]):
                    wordMap[rec][f.name] = 0
                wordMap[rec][f.name] += 1


# ukupBrojFajlova = len(dictProcitanihFajlova)

# for key in dictProcitanihFajlova:

# print(ukupBrojFajlova)

# specific file stuff
spFilePath = input()
spFile = open(str(spFilePath))
wordsInSpFile = word_tokenize(spFile.read())
spFileStemmedWords = []  # lista korenovanih reci iz specificnog fajla

for x in wordsInSpFile:
    if(x.isalnum()):
        w = snowball_stemmer.stem(x)
        spFileStemmedWords.append(w)


# # create Word objects and put them in List
# freqCounter = Counter(spFileStemmedWords)
# listaReciSpFajla = [Word(key, value, ukupBrojFajlova, listaProcitanihFajlova)
#                     for key, value in freqCounter.items()]
# listaReciSpFajla.sort(key=lambda Word: Word.wordScore(), reverse=True)  # sort by freq
#
# print(len(listaReciSpFajla))
# for rec in listaReciSpFajla:
#     print("\nRec = " + rec.word)
#     print("\nWord Score = " + str(rec.wordScore()))
#     print("\nTF = " + str(rec.TF))
#     print("\nIDF = " + str(rec.IDF))
#     print("\n----------------------")
