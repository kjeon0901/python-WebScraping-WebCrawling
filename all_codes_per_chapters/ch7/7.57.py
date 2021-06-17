import re

# 전화번호 추출
test_num = "저의 전화번호는 010-6666-7777 입니다"

pattern = re.compile('[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')  #숫자숫자숫자-숫자숫자숫자숫자-숫자숫자숫자숫자 형태
pattern1 = re.compile('\d\d\d-\d\d\d\d-\d\d\d\d')  #숫자숫자숫자-숫자숫자숫자숫자-숫자숫자숫자숫자 형태
pattern2 = re.compile('\d{3}-\d{4}-\d{4}')  #숫자숫자숫자-숫자숫자숫자숫자-숫자숫자숫자숫자 형태
c = pattern.findall(test_num)
d = pattern1.findall(test_num)
e = pattern2.findall(test_num)
print(c)
print(d)
print(e)

test_str = """I am Park Jeong-tae. I live in Paju.
I lived in Paju for 25 years. estadsffjkfad test
Sample text for testing:
abcdefghijklmestnopqrsAvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 +-.,!@#$%^&*();\/|<>"'
12345 -98.7 3.141 .6180 9,000 +42"""

pattern = re.compile('[a-zA-Z0-9]+') # a부터 z까지, A부터 Z까지, 0부터 9까지 포함된 것
pattern1 = re.compile('\w+')
c = pattern.findall(test_str)
d = pattern1.findall(test_str)
print(c)
print(d)

pattern = re.compile('[^a-z]+')  # a부터 z까지 포함되지 않는 것
c = pattern.findall(test_str)
print(c)

pattern = re.compile('[^A-Z]+')  # A부터 Z까지 포함되지 않는 것
c = pattern.findall(test_str)
print(c)

pattern = re.compile('t..t')  # t문자문자t 패턴
pattern1 = re.compile('t...t')  # t문자문자문자t 패턴
c = pattern.findall(test_str)
d = pattern1.findall(test_str)
print(c)
print(d)

pattern = re.compile('t?est\w+')  # test나 est로 시작하는 문자열 뒤에 \w가 있어야 됨
pattern1 = re.compile('t?est\w*')  # test나 est로 시작하는 문자열 뒤에 \w가 없어도 됨
c = pattern.findall(test_str)
d = pattern1.findall(test_str)
print(c)
print(d)
