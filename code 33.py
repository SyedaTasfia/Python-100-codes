# ---------Question 33-----------

# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys.

def print_Dict():
    di = dict()
    for i in range(1, 21):
        di[i] = i ** 2
    print (di)


print_Dict()