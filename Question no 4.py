#Question no 4

'''
Write a function that takes a character ( i.e. a string of length 1 )
and returns True if it is a vowel, False otherwise.
'''

#code

def is_vowel(string):
    if len(string)==0:
        print("u have pass empty string")

    elif len(string)<2:
        vowels="aeoiu"
        string=string.lower()
        if string in vowels:
            print("True")
        else:
            print("False")
    else:
        print("Length of string is more than 1 so we are sorry")
    
