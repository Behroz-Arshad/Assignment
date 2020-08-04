
#Question no 20

'''
Represent a small bilingual lexicon as a Python dictionary in the following fashion
{ "merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år" }
and use it to translate your Christmas cards from English into Swedish. That is, write a function `translate()`
that takes a list of English words and returns a list of Swedish words.
'''

#Code

def translate(s):
    dic={ "merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år" }
    a=(s.split(" "))
    is_valid=True
    l=[]
    for i in a:
        if i in dic:
            l.append(dic[i])
        else:
            is_valid=False
            print(i,"is not valid word")
            break
    if is_valid==True:
        for lan in l:
            print(lan,end=" ")
