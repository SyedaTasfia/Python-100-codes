# -----------Question 92----------

# Please write a program which count and
# print the numbers of each character in a string input by console.

dic = {}
sr=input()
for s in sr:
    dic[s] = dic.get(s,0)+1
print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
