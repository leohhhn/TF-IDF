from pathlib import Path
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import numpy as np


class Word:

    TF = 0
    IDF = 0
    ukupBrojFajlova = 0
    listaFajlova = []

    def __init__(self, word, TF, ukupBrojFajlova, listaFajlova):
        self.word = word
        self.TF = TF
        self.listaFajlova = listaFajlova
        self.ukupBrojFajlova = ukupBrojFajlova
        self.IDF = np.log(ukupBrojFajlova / self.k(listaFajlova))

    def k(self, listaFajlova):
        br = 0

        for fajl in listaFajlova:  # prosledjivanje liste radi
            allWordsinCurrFile = word_tokenize(fajl.read())
            currFileStemmedWords = []

            for x in allWordsinCurrFile:
                if(x.isalnum()):
                    w = snowball_stemmer.stem(x)
                    currFileStemmedWords.append(w)

            for rec in currFileStemmedWords:
                if(self.word == rec):
                    print("nasao rec " + "\"" + self.word + "\"" + " u fajlu " + str(fajl.name))
                    br += 1
                    break

        if(br == 0):
            print("\"" + self.word + "\"" + " not found in any file, div by 0")
            return 1

        return br

    def wordScore(self):
        return self.TF * self.IDF


# corpusPath = input()
allTxtPaths = list(Path("corpus").rglob("*.[tT][xX][tT]"))  # get all txt paths from corpus
snowball_stemmer = SnowballStemmer(language="english")

# loading all files
listaFajlova = []
for x in allTxtPaths:  # opening all files in corpus
    f = open(x)
    listaFajlova.append(f)
ukupBrojFajlova = len(listaFajlova)
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

freqCounter = Counter(spFileStemmedWords)
listaReciSpFajla = [Word(key, value, ukupBrojFajlova, listaFajlova)
                    for key, value in freqCounter.items()]
listaReciSpFajla.sort(key=lambda Word: Word.TF, reverse=True)  # sort by freq
for rec in listaReciSpFajla:
    print(rec.word)

#
# for rec in listaReciSpFajla:
#     print("\nRec = " + rec.word)
#     print("\nWord Score = " + str(rec.wordScore()))
#     print("\nTF = " + str(rec.TF))
#     print("\nIDF = " + str(rec.IDF))
#     print("\n----------------------")
