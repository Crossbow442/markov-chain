import random
import json

oldTable = json.load(open("doubleTable.json"))
table = {}

for key in oldTable:
    pair = tuple(key.split())
    table[pair] = oldTable[key]

outputWords = []

cStr = random.choice(list(table.keys()))
outputWords.append(cStr[0].capitalize())


#Adds random words to string
for i in range(20):
    if not len(table[cStr]) == 0:
        cStr = (cStr[1], random.choice(table[cStr]))
        outputWords.append(cStr[0])
    else:
        break

output = " ".join(outputWords) + "."

print("")
print(output)
print("")