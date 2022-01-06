# -------------Question 67----------------

# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n
# in comma separated form while n is input by console.

def Num_Generator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

num =int(input())
value = []
for i in Num_Generator(num):
    value.append(str(i))

print( ",".join(value))