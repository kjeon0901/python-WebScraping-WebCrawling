import re

test_str= """I am Park Jeong-tae. I live in Paju.
I lived in Paju for 25 years.
Sample text for testing:
abcdefghijklmnopqrsAvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\/|<>"'
12345 -98.7 3.141 .6180 9,000 +42"""

pattern = re.compile('[0-9]')
pattern1 = re.compile('[0-9]+')
c = pattern.findall(test_str)
d = pattern1.findall(test_str)

print(c)
print(d)
