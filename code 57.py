# -------------Question 57-------------

# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address.
# Both user names and company names are composed of letters only.

import re
emailaddress = input()
part2 = "(\w+)@(\w+)\.(com)"
round2 = re.match(part2,emailaddress)
print (round2.group(2))