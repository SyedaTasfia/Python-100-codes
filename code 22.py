# # ----------Question 22----------

# Write a program to compute the frequency of the words from the input.
# # The output should output after sorting the key alphanumerically.
from typing import KeysView

freq_word = {}
line = input()
for word in line.split():
    freq_word[word] = freq_word.get(word,0)+1

words = [freq_word.keys()]
words.sort()
for w in words:
    print( "%s:%d" % (w, freq_word[w]))
