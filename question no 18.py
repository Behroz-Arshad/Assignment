
#Question no 18
'''
A pangram is a sentence that contains all the letters
of the English alphabet at least once,
for example: "The quick brown fox jumps over the lazy dog".
Your task here is to write a function to check a sentence to see
if it is a pangram or not.
'''

#Code
def ispangram(string): 
    letter = "abcdefghijklmnopqrstuvwxyz"
    for i in letter: 
        if i not in string.lower(): 
            return False
  
    return True
