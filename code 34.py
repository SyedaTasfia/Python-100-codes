# ---------Question 34-----------

# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
# The function should just print the values only.

def print_Dict():
    di = dict()
    for i in range(1, 21):
        di[i] = i ** 2
    for (k, v) in di.items():
        print ( v)


print_Dict()