#Question no 15
'''
Write a function find_longest_word() that takes a list of words
and returns the length of the longest one.
'''

def longest(lstofwords):
    listofnumber=[]
    for i in lstofwords:
        listofnumber.append(len(i))
    listofnumber.sort()
    print("Length of longest word in list is : ",listofnumber[-1])
