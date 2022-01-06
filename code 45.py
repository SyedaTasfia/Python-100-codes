# -------------Question 45------------

# Write a program which can map() and filter() to make a list whose
# elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

List = [1,2,3,4,5,6,7,8,9,10]
even_number = list(map(lambda x: x**2, filter(lambda x: x%2==0,List)))
print (even_number)