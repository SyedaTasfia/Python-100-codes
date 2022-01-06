# -----------Question 82----------

# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"]
# and the object is in ["Hockey","Football"].

subject=["I", "You"]
verb=["Play", "Love"]
object=["Hockey","Football"]
for i in range(len(subject)):
    for j in range(len(verb)):
        for k in range(len(object)):
            sentences = "%s %s %s." % (subject[i], verb[j], object[k])
            print (sentences)