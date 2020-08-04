#question no 3

'''
Define a function that computes the length of a given list or string.
( It is true that Python has the len() function built in,
but writing it yourself is nevertheless a good exercise ).


'''

#code

#this function count the length including spaces
def length(s):
    count=0
    for i in s:
        count=count+1
    print ("length of string is :",count)

#this function calculate the length of string only without spaces
def len(s):
    count=0
    for i in s:
        if i==" ":
            continue
        else:
            count=count+1
    print("length of string is :",count)
