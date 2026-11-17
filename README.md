# Word Level Markov Chain

A word-based Markov Chain implementation in Python that generates text based on any Gutenburg Project book

## How it works
- Every time a word appears it is added to a list (e.g. "John")
- Every word that follows a word is added to a list attached to the word (e.g. "John is", "John was")
- A word is randomly selected to begin the sentence
- Out of the possible successors, one is chosen randomly and added to the sentence
- Then that word's succesors are chosen from randomly
- This continues until a word has no successors, or until there are 10 words in the sentenc

## How to use
- Download any book from https://www.gutenberg.org/
- Drop it into the markov-chain folder
- Rename it to "raw.txt"
- Run Converter.py to convert the raw file into usable text
- Run SingleTable.py or DoubleTable.py to generate a .json file for the generator to use
- Run SingleGenerator.py or DoubleGenerator.py 
