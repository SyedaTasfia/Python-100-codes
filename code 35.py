# ---------Question 35-----------

# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

def print_list():
    List = list()
    for i in range(1, 21):
        List.append(i ** 2)
    print (List)


print_list()