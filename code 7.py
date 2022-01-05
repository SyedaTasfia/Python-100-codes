# ------------Question 07------------

# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.

input_string = input()
dimension=[int(x) for x in input_string.split(',')]
rownum=dimension[0]
colnum=dimension[1]
List = [[0 for col in range(colnum)] for row in range(rownum)]

for row in range(rownum):
    for col in range(colnum):
        List[row][col]= row*col

print(List)