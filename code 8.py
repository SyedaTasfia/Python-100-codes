# ----------------Question 08--------------

# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.

item=[x for x in input().split(',')]
item.sort()
print(','.join(item))