
def square_num(n):
    return n ** 2

result = square_num(4)
print(result)


def add_two(a,b):
    return a + b

result = add_two(8,8)
print(result)


def multiply(p1, p2):
    return p1 * p2

result = multiply("h",5)
print(result)
# hhhhh

import math
def compute_area_and_circumference(radius):
    area = round(math.pi * (radius **2), 2)
    circumference = round(2 * math.pi *radius, 2)
    return area, circumference

result = compute_area_and_circumference(3)
print(result[0])
print(result[1])


def greet_user(name = "Random"):
    return "Hello" + " " + name

result = greet_user()
print(result)


# lambda fn( fn with no name)
cube = lambda x: x ** 3
print(cube(2))

def sum_all(*args):
    print(*args)
    print(args)
    return sum(args)

print(sum_all(1,2))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7))

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# print_kwargs(name="tauhid",surname="khan")
# print_kwargs(name="tauhid")
# print_kwargs(addres="mumbai")

def print_evens(n):
    for i in range(0,n+1,2):
        yield i

# The **yield** keyword is used to turn a function into a generator — a special kind of function that returns values one at a time using an iterator, instead of returning them all at once like return   

for num in print_evens(10):
    print(num)


def calc_fact(n):
    if n <= 1: return 1
    return n * calc_fact(n-1)

result = calc_fact(5)
print(result)
