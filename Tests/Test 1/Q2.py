import os
import collections as c

def histogram (word):
    letters = dict()
    word = word.upper()
    for letter in word:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

try:
    with open('word.txt', 'r') as words:
            for word in words:
                print(f"Histogram of the word {word.upper()} is:")
                print(histogram(word))
except FileNotFoundError:
    print('Error...File not found!')

