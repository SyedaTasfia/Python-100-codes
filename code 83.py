# -----------Question 83----------

# Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

List = [5,6,77,45,22,12,24]
List = [x for x in List if x%2!=0]
print (List)