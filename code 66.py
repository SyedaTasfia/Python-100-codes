# -------------Question 66----------------

# Please write a program using generator to print the even numbers between 0 and n in
# comma separated form while n is input by console.

def Even_Generator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


num =int(input())
value = []
for i in Even_Generator(num):
    value.append(str(i))

print(",".join(value))
