
x = 2
y = 3
z = 4

x+y
# 5

2**4
# 16 power

x + y * z
# confusing
(x + y) * z
# 20

40 + 2.23
# 42.23
# always make sure both have same datatype

int(2.23)
# 2
float(40)
# 40.0

'tauhid' + 'khan'
# tauhidkhan

x, y , z
# (2, 3 , 4) tuples

x + 1, y * 2
# (3, 6)

y % 2
# 1 ( 3 / 2 = 1 (remainder) )

2 ** 1000
#10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376

repr('chai')
# "'chai'"
str('chai')
# 'chai'
print('chai')
# chai


# chained comparisons are not evaluated left-to-right
# Instead, they're interpreted like this:
# x < y and y < z

x, y , z
# (2, 3 , 4) 
x < y < z
# True
(x < y) and (y < z)
# True
# both same

1 == 2 < 3
# (1 == 2) and (2 < 3)
#  False and True = False


import math
# floor --> towards bottom
math.floor(3.5)
# 3
math.floor(-3.5)
# 4
math.floor(3.9)
# 3

# trunc --> toward 0 on num line
math.trunc(2.8)
# 2
math.trunc(-2.8)
# -2

# types of numbers

# Octal
0o20 
# 16

# Hexal
0xFF
# 255

# Binary
0b1000
# 8

# can convert things
oct(64)
# and so one

# one more way
int('64', 8)
# (number to convert , the format) 2, 8, 16

# bitwise operators

# and
a = 5         # 0101
b = 3         # 0011
print(a & b)  # 0001 = 1

# or
a = 5         # 0101
b = 3         # 0011
print(a | b)  # 0111 = 7

# xor
a = 5         # 0101
b = 3         # 0011
print(a ^ b)  # 0110 = 6

# not
a = 5       # 0101
print(~a)   # -6

# Left Shift
a = 5          # 0101
print(a << 1)  # 1010 = 10
# Each left shift << 1 multiplies the number by 2.

a = 5
print(a << 2)  # 0101 -> 10100 = 20


# Right Shift
a = 5          # 0101
print(a >> 1)  # 0010 = 2
# Each right shift >> 1 divides the number by 2 (integer division).


# some libraries
import random
random.random()
# 0.75456789
random.randint(1,100)
# 76

l1 = ['maths','chem','bio','phy']
random.choice(l1)
# 'maths
random.shuffle(l1)
# ['chem',maths,'phy','bio']



(0.1 + 0.1 + 0.1) - 0.3 
# 5.551115123125783e-17
# soln
from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')

from fractions import Fraction
myFra = Fraction(2, 7)
myFra


# set
setOne = {1, 2, 3, 4}
# intersection
setOne & {1,3}
# {1,3}
# union
setOne | {1,3,7}
# {1,2,3,4,7}
setOne - {1,2,3,4}
# set()  ==> empty set

# booleans
True == 1
# True
True is 1
# False
True + 4
# 5

# == and is keyword
a = [1, 2, 3]
b = a

print(a == b)  # True → values are equal
print(a is b)  # True → same object (same memory)

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True → same content
print(a is b)  # False → different objects
