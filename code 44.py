# -------------Question 44------------

# Write a program
# which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

List = [1,2,3,4,5,6,7,8,9,10]
Squared_Numbers = list(map(lambda x: x**2, List))
print(Squared_Numbers)