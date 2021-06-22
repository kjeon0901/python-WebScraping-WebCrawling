try:
    a = 10
    b = 0

    print(a)
    print(b)

except IndexError:
    print('Index error 발생')
except ZeroDivisionError:
    print('ZeroDivision error 발생')
else:
    print('try가 정상적으로 실행됬을 때')
finally:
    print('최종적으로 무조건 실행되는 구문')
