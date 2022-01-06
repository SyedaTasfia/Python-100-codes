# -------------Question 98-------------

# Write a Python program that accept a list of integers and check the length and the fifth element.
# Return true if the length of the list is 8 and fifth element occurs thrice in the said list.

def test(nums):
    if (len(nums) == 8 and nums.count(nums[4]) == 3):
       print("True")
    else:
        print("False")

n = [19,19,15,5,5,5,1,2]
print(test(n))