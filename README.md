# Word Level Markov Chain

A Markov Chain implementation in Python that generates text based on any Gutenburg Project book

## How it works

**Single Order:**
- Every time a word appears it is added to a list (e.g. "John")
- Every word that follows a word is added to a list attached to the word (e.g. "John is", "John was")
- A word is randomly selected to begin the sentence
- Out of the possible successors, one is chosen randomly and added to the sentence
- Then that word's succesors are chosen from randomly
- This continues until a word has no successors, or until there are 100 words in the sentence

**Double Order:**
- Coming Soon

## How to use
- Download any book from https://www.gutenberg.org/
- Drop it into the markov-chain folder
- Rename it to "raw.txt"
- Run Converter.py to convert the raw file into usable text
- Run SingleOrder.py or DoubleOrder.py 
