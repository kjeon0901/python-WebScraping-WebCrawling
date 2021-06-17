import re

test_str= """I am Park Jeong-tae. I live in Paju.
I lived in Paju for 25 years.
Sample text for testing:
abcdefghijklmnopqrsAvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\/|<>"'
12345 -98.7 3.141 .6180 9,000 +42"""

pattern = re.compile('[a-z]')
pattern1 = re.compile('[a-z]+')
c = pattern.findall(test_str)
d = pattern1.findall(test_str)

print(c)
print(d)

pattern = re.compile('[A-Z]')
pattern1 = re.compile('[A-Z]+')
c = pattern.findall(test_str)
d = pattern1.findall(test_str)

print(c)
print(d)
