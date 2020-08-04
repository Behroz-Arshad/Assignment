#Question no 16
'''
Write a function filter_long_words()
that takes a list of words and an integer n and
returns the list of words that are longer than n.



'''

#Code

def filter_long_words(lst,n):
    lstUpdate=[]
    for i in lst:
        if len(i)>n:
            lstUpdate.append(i)
    print ("New list of Words that are greater length of",n,": ",lstUpdate)
#It can also be done by for loop using range..
#e.g for i in range(len(lst))
