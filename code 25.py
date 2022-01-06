# # ----------Question 25----------

# Define
# a class , which have a class parameter and have a same instance parameter.

class Person:
    name = "Person"

    def __init__(self, name=None):
        # self.name is the instance parameter
        self.name = name


jeffrey = Person("Jeffrey")
print ("%s name is %s" % (Person.name, jeffrey.name))

nimo = Person()
nimo.name = "Nimo"
print("%s name is %s" % (Person.name, nimo.name))