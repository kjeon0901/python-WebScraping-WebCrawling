try:
    a = 10
    b = 0

    print(a)
    print(b)
    print(a/0)
except ZeroDivisionError:
    print('ZeroDivisionError error 발생')
