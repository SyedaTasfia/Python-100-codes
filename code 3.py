# ---------------Question 03-------------

# ------------With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
# such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.-------------------

print("Enter any number:")
N = int(input())
D = dict()
for i in range(1, N+1):
    D[i] = i*i

print(D)