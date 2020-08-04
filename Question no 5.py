#Question no 5
'''
Write a function translate() that will translate a text into "rövarspråket"
(Swedish for "robber's language"). That is, double every consonant and place
an occurrence of "o" in between. For example,
translate("this is fun") should return the string "tothohisos isos fofunon"
'''

#Code
def translate(string):
    translation=""
    for consonent in string:
        if consonent not in ["a","e","o","i","u"," "]:
            translation=translation+consonent+"o"+consonent
        else:
            translation=translation+consonent

    print(translation)
        
