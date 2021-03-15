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

    def k(self, listaProcitanihFajlova):
        br = 0

        for textInFile in listaProcitanihFajlova:  # prosledjivanje liste radi
            allWordsinCurrFile = word_tokenize(textInFile)
            currFileStemmedWords = []

            for x in allWordsinCurrFile:
                if(x.isalnum()):
                    w = snowball_stemmer.stem(x)
                    currFileStemmedWords.append(w)

            for rec in currFileStemmedWords:
                if(self.word == rec):
                    # print("nasao rec " + "\"" + self.word + "\"")
                    br += 1
                    break

        if(br == 0):
            print("\"" + self.word + "\"" + " not found in any file, div by 0")
            return

        return br

    def wordScore(self):
        return self.TF * self.IDF


corpusPath = input()
allTxtPaths = list(Path(str(corpusPath)).rglob("*.[tT][xX][tT]"))  # get all txt paths from corpus
snowball_stemmer = SnowballStemmer(language="english")

# loading all files
listaFajlova = []
for x in allTxtPaths:  # opening all files in corpus
    f = open(x)
    listaFajlova.append(f)
ukupBrojFajlova = len(listaFajlova)

listaProcitanihFajlova = []
for fajl in listaFajlova:
    listaProcitanihFajlova.append(fajl.read())

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

# create Word objects and put them in List
freqCounter = Counter(spFileStemmedWords)
listaReciSpFajla = [Word(key, value, ukupBrojFajlova, listaProcitanihFajlova)
                    for key, value in freqCounter.items()]
listaReciSpFajla.sort(key=lambda Word: Word.wordScore(), reverse=True)  # sort by freq

print(len(listaReciSpFajla))
for rec in listaReciSpFajla:
    print("\nRec = " + rec.word)
    print("\nWord Score = " + str(rec.wordScore()))
    print("\nTF = " + str(rec.TF))
    print("\nIDF = " + str(rec.IDF))
    print("\n----------------------")
