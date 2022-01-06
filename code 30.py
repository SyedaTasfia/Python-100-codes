# # ----------Question 30----------

# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print al l strings line by line.

def print_Value(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 > len2:
        print(str1)
    elif len2 > len1:
        print(str2)
    else:
        print(str1)
        print(str2)


print_Value("two", "three")
