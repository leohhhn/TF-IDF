import sys
from pathlib import Path
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import numpy as np
# sys.stdout.reconfigure(encoding='utf-8')


class Word:

    TF = 0
    IDF = 0
    ukupBrojFajlova = 0
    k = 0
    word_score = 0

    def __init__(self, word, TF, ukupBrojFajlova):
        self.word = word
        self.TF = TF
        self.ukupBrojFajlova = ukupBrojFajlova

    def wordScore(self):
        self.word_score = self.TF * self.IDF
        return self.word_score

    def set_IDF(self, k):
        self.IDF = np.log(ukupBrojFajlova / k)
        self.wordScore()


corpusPath = input()
allTxtPaths = list(Path(str(corpusPath)).rglob("*.[tT][xX][tT]"))  # get all txt paths from corpus
snowball_stemmer = SnowballStemmer(language="english")
ukupBrojFajlova = len(allTxtPaths)


# map all (stemmed) words from all files to a map {path of file word was found in:frequency}
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


# specific file stuff
spFilePath = input()
spFile = open(str(spFilePath))
readFile = spFile.read()
spFile.close()
wordsInSpFile = word_tokenize(readFile)

spFileStemmedWords = []  # lista stemovanih reci iz specificnog fajla

# get list of stemmed words
for x in wordsInSpFile:
    if(x.isalnum()):
        w = snowball_stemmer.stem(x)
        spFileStemmedWords.append(w)


spfWordCounter = Counter(spFileStemmedWords)
listaReciSpFajla = [Word(key, value, ukupBrojFajlova)
                    for key, value in spfWordCounter.items()]

for rec in listaReciSpFajla:
    for key in wordMap:
        if(rec.word == key):
            rec.set_IDF(len(wordMap[key]))

listaReciSpFajla.sort(key=lambda Word: Word.wordScore(), reverse=True)

task1out = ""

if(len(listaReciSpFajla) >= 10):
    for i in range(10):
        task1out += listaReciSpFajla[i].word + ', '
else:
    for i in range(len(listaReciSpFajla)):
        task1out += listaReciSpFajla[i].word + ', '

print(task1out[:-2])


# TASK 2

sentInSpFile = sent_tokenize(readFile)
sentMap = {}

for sent in sentInSpFile:
    sentScore = 0
    currSentWords = word_tokenize(sent)
    for rec in currSentWords:
        rec = snowball_stemmer.stem(rec)
        for wordObj in listaReciSpFajla:
            if(rec == wordObj.word):
                sentScore += wordObj.word_score
    sentMap[sent] = sentScore

sentMapCopy = {}
sorted_keys = sorted(sentMap, key=sentMap.get, reverse=True)

if(len(sorted_keys) >= 5):
    for i in range(5):
        sentMapCopy[sorted_keys[i]] = sentMap[sorted_keys[i]]
else:
    for i in range(len(sorted_keys)):
        sentMapCopy[sorted_keys[i]] = sentMap[sorted_keys[i]]


task2out = ""
for sent in sentMap:
    for snt in sentMapCopy:
        if(sent == snt):
            task2out += sent + ' '
print(task2out[:-1])
