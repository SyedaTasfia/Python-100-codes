# -----------Question 16-----------

# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.

val = input()
numbers = [x for x in val.split(",") if int(x)%2!=0]
print (",".join(numbers))