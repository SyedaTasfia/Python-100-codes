# ---------------Question 02-------------

# ------------Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.----------

def factorial(x):
    if x ==0:
        return 1
    return x * factorial(x-1)

print("Enter any number :")

x = int(input())

print("The factorial is:", factorial(x))