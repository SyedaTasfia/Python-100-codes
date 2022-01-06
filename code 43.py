# -------------Question 43------------

# Write a program which can filter even numbers in a list by using filter function.
# The list is: [1,2,3,4,5,6,7,8,9,10].

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_num = list(filter(lambda x: x%2==0, List))
print (even_num)
