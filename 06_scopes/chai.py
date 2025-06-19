# scopes:
username = "tauhid"

def f1():
    # username = "khan"
    print(username)

print(username)
f1()


x = 99

def f2():
    # global x  refers tto global x
    x = 12

f2()
print(x)


def f3():
    x = 88
    def f4():
        print(x) # refer to 88
    f4()

f3()

# Closures:

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2) #calculates square
g = chaicoder(3) #calculates cube

print(f(2)) 
print(g(2)) 


def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply
    
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))
