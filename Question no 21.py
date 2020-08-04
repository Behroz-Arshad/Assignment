#Question no 21
'''
Write a function `char_freq()` that takes a string and builds a
frequency listing of the characters contained in it. Represent the
frequency listing as a Python dictionary.
Try it with something like `char_freq("abbabcbdbabdbdbabababcbcbab")`.
'''
#Code
def char_freq(string):
  frequancy = {}
  for i in string:
    if i in frequancy:
      frequancy[i] =frequancy[i] + 1
    else:
      frequancy[i] = 1
  return frequancy
