"""
def function1():
    print("Subscribe now")

func2 = function1
del function1
func2()

#function example
def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum
a = funcret(1)
print(a)

#another example
def executor(func):
    func("this")
executor(print)
"""
"""
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("executed")
    return nowexec
@dec1
def who_is_harry():
    print("Harry is good boy")
#who_is_harry = dec1(who_is_harry)
who_is_harry()
"""
"""
def div(a,b):
    print(a/b)


def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
div1 = smart_div(div)

div1(2,4)
"""
def annouce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the Funcion")
    return wrapper
@annouce
def hello():
    print("Hello, World")

hello()