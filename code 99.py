# -------------Question 99-------------

# Write a Python program that accept an integer test
# whether an integer greater than 4^4 and which is 4 mod 34

def test(nums):
    if (n % 34 == 4 and n > 4 ** 4):
       print("True")
    else:
        print("False")

n = 922
print(test(n))