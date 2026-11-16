import json

text = open("source.txt").read()
words = text.split()
table = {}
outputWords = []

#input reader
count = 0
for word in words:
    if word not in table:
        table[word] = []
    if count + 1 < len(words):
        table[word].append(words[count + 1])

    count += 1

json.dump(table, open("singleTable.json", "w"))

print("Done")