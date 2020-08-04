#Question no 7

'''
Define a function reverse() that computes the reversal of a string.
For example, reverse( "I am testing" )
should return the string "gnitset ma I".
'''

#code
def reverse(s):
    s=str(s)
    for i in range(len(s),0,-1):
        print(s[i-1], end ="")
    
