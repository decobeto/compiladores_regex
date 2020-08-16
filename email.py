import re

email = input('Email')

print(email)

if re.findall('@\w+', email)