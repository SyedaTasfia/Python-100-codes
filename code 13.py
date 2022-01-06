# -----------Question 13-----------

# Write a program that accepts a sentence and calculate the number of letters and digits.

inp = input()
dig ={"DIGITS":0, "LETTERS":0}
for c in inp:
    if c.isdigit():
        dig["DIGITS"]+=1
    elif c.isalpha():
        dig["LETTERS"]+=1
    else:
        pass
print( "LETTERS", dig["LETTERS"])
print ("DIGITS", dig["DIGITS"])