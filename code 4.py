# ------------Question 04-----------
# --------Write a program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number.---------

print("Enter any values: ")

values = input()

list = values.split(",")

t = tuple(list)

print("Output is:")

print(list)

print(t)
