def f(x, y=20):
    print('running ' + str(x) + ' ' + str(y))
    return x + y

var1 = f(10)
var2 = f(10, 40)

print(var1)
print(var2)
