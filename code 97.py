# -------------Question 97-------------

# Write a Python program find a list of integers
# with exactly two occurrences of nineteen and at least three occurrences of five.

def test(nums):
    if (nums.count(19) == 2 and nums.count(5) >= 3):
       print("True")
    else:
        print("False")

n = [19,19,5,5,2,5,3]
print(test(n))