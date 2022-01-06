# -----------Question 17-----------
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

totalamount = 0
while True:
    source = input()
    if not source:
        break
    values = source.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
         totalamount+=amount
    elif operation=="W":
        totalamount-=amount
    else:
        pass
print("Total Amount is: " ,totalamount)