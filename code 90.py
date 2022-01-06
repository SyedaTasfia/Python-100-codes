# -----------Question 90----------

# With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all duplicate values with original order reserved.

def remove_duplicate( list):
    newli=[]
    seen = set()
    for items in list:
        if items not in seen:
            seen.add( items )
            newli.append(items)

    return newli

list =[12,24,35,24,88,120,155,88,120,155]
print (remove_duplicate(list))