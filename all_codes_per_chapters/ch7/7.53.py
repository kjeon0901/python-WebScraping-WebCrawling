import re

test_str= "test t1sd j test1"

pattern = re.compile('test')
a = pattern.match(test_str)
b = pattern.search(test_str)
c = pattern.findall(test_str)
d = pattern.finditer(test_str)

print('-- match result --')
print(a)
print(a.group(), a.start(), a.end(), a.span())

print('-- search result --')
print(b)
print(b.group(), b.start(), b.end(), b.span())

print('-- findall result --')
print(c)

print('-- finditer result --')
print(d)
for i in d:
    print(i.group(), i.start(), i.end(), i.span())
