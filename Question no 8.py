#Question no 8

'''
Define a function is_palindrome()
that recognizes palindromes (i.e. words that look the same written backwards).
For example, is_palindrome( "radar" ) should return True
'''


#Code
def is_palindrome(string):
    string=str(string)
    if string[0] ==string[len(string)-1]:
        print("True")
    else:
        print("False")
    


