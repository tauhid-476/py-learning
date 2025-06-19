import time
print("chai")

# File:
# >>> f = open('i.py')
# >>> f.__next__()
# 'import time\n'
# >>> f.__next__()
# 'print("chai")\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<python-input-6>", line 1, in <module>
#     f.__next__()
#     ~~~~~~~~~~^^
# StopIteration
# >>> 

# List:
# >>> myList = [1,2,3,4]
# >>> I = iter(myList)
# >>> I
# <list_iterator object at 0x7f11a2547eb0>
# >>> I.__next__()
# 1
# >>> I
# <list_iterator object at 0x7f11a2547eb0>
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3


# for file:
# >>> f = open('i.py')
#  here iter(f) is same as f, cuz for file , it is hadled internally
#  iter(f) == f ==> True


# Dict:
# >>> D = {'a':1,'b':2}
# >>> I = iter(D)
# >>> I
# <dict_keyiterator object at 0x7f11a25f7b00>
# >>> next(I)
# 'a'
# >>> next(I)
# 'b'
# >>> next(I)
# Traceback (most recent call last):
#   File "<python-input-17>", line 1, in <module>
#     next(I)
#     ~~~~^^^
# StopIteration
# >>> 

# Same with range