import random

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


#starting word
cWord = random.choice(words)
outputWords.append(cWord)


#Adds random words to string
for i in range(100):
    if not len(table[cWord]) == 0:
        cWord = random.choice(table[cWord])
        outputWords.append(cWord)
    else:
        break

output = " ".join(outputWords)

print("")
print(output)
print("")