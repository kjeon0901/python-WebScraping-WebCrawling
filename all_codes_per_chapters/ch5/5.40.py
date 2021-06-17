try:
    a = 10
    b = 0

    print(a)
    print(b)
    print(a/0)
except IndexError:
    print('Index error 발생')
except ZeroDivisionError:
    print('ZeroDivision error 발생')
