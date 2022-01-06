# ---------Question 39-----------

# Define a function which can generate and
# print a tuple where the value are square of numbers between 1 and 20 (both included).

def print_Tuple():
    List = list()
    for i in range(1, 21):
        List.append(i ** 2)
    print(tuple(List))


print_Tuple()