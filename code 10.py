# ----------------Question 10--------------

# Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them alphanumerically.

source = input()
words = [word for word in source.split(" ")]
print(" ".join(sorted(list(set(words)))))
