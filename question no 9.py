#Question no 9
'''
Write a function is_member()
that takes a value ( i.e. a number, string, etc ) x and a list of values a,
and returns True if x is a member of a, False otherwise.
(Note that this is exactly what the in operator does, but for the sake of the
exercise you should pretend
Python did not have this operator).

'''
'''def is_member(x,a=[]):
    if a in b:
        return True
    else:
        return False'''

#Question no 9 (b)
'''
def ismember(x, a):
    if len(a) == 0:
        return False
    return x == a[0] or ismember(x, a[1:])
'''
#Question no 9 (C)
def ismember(x, a):
    if len(a) == 0:
        print("ddddddddd")
    return x== a[1:]  

