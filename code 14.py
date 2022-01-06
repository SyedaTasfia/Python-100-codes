# -----------Question 14-----------

# Write a program that accepts a sentence and
# calculate the number of upper case letters and lower case letters.

inp = input()
dig ={"UPPER CASE":0, "LOWER CASE":0}
for c in inp:
    if c.isupper():
        dig["UPPER CASE"]+=1
    elif c.islower():
        dig["LOWER CASE"]+=1
    else:
        pass
print ("UPPER CASE", dig["UPPER CASE"])
print ("LOWER CASE", dig["LOWER CASE"])