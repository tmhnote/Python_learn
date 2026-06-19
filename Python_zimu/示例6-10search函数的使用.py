import re
pattern = '\d\.\d+'
s = 'I study Python 3.11 every day Python 2.7 I love you'

match = re.search(pattern, s)

s2 = '4.10 Python I study every day'

s3 = 'I study everyday Python '

match2 = re.search(pattern, s2)
match3 = re.search(pattern, s3)

print(match)
print(match2)
print(match3) # None

print(match.group())
print(match2.group())