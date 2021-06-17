from m2 import var1 as m2_var1, var2 as m2_var2, f1 as m2_f1

var1 = 'm1 hello'
var2 = 'm1 world'

def f1():
    print('m1.py f1() 함수')

if __name__ =="__main__":

    print(var1)
    print(var2)
    print(m2_var1)
    print(m2_var2)
    f1()
    m2_f1()
