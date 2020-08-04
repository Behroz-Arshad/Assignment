#Question no 6
'''
Define a function sum() and a function multiply()
that sums and multiplies (respectively) all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4])
should return 10, and multiply([1, 2, 3, 4]) should return 24.
'''
def sum(a):
    sums=0
    for i in a:
        sums=sums+i
    print("Total sum is :",sums)

#for multiplication

def multiply(a):
    mul=1
    for i in a:
        mul=mul*i
    print("Result of multiplicaton is :",mul)
