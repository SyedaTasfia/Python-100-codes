# -------------Question 100-------------

# Write a Python program to check a given list of integers where the sum of the first i integers is i

def test(nums):
    if (all([sum(nums[:i]) == i for i in range(len(nums))])):
       print("True")
    else:
        print("False")

nums = [1,1,1,1,1,1]
test(nums)