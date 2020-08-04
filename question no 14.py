#Question noo 14
'''
Write a program that maps a
list of words into a list of integers representing the lengths of the
corresponding words.
'''
#code
list_of_words=["hello","Behroz","How","are","you"]
list_of_number=[]
for i in list_of_words:
    list_of_number.append(len(i))
    
print(list_of_number)

#2nd
#Function for this

def convert(lstofwords):
    listofnumber=[]
    for i in lstofwords:
        listofnumber.append(len(i))
    
    print(listofnumber)
    
