# -------------Question 60---------------

# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
from unidecode import unidecode

source = input()
u= unidecode(source ,"utf-8")
print(u)