import json

text = open("source.txt").read()
words = text.split()
table = {}
outputWords = []

for i in range(0, len(words)):
    if i < len(words) - 1:
        pair = words[i] + " " + words[i + 1]

        if pair not in table:
            table[pair] = []
        if i < len(words) - 2:
            table[pair].append(words[i + 2])

print("Done")

json.dump(table, open("doubleTable.json", "w"))
    