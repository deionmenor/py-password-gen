import csv
import random
import itertools


fh = open("data/word_bank.csv", "r")
wordReader = csv.reader(fh)
wordList = []

for word in wordReader:
    wordList.append(word)
    
pw = random.sample(wordList, k=4)
pw = [p[0] for p in pw]
pw = "-".join(pw)

print(pw)
    