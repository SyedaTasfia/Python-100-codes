# ----------------Question 09--------------

# Write a program that accepts sequence of lines as input
# and prints the lines after making all characters in the sentence capitalized.
line = []
while True:
    Input = input()
    if Input:
        line.append(Input.upper())
    else:
        break;

for sentences in line:
    print(sentences)