#Question no 10
'''
Define a function overlapping() that takes two lists and returns
True if they have at least one member in common,
False otherwise.
You may use your is_member() function, or the in operator,
but for the sake of the exercise,
you should (also) write it using two nested for-loops.
'''

#Code

def overlaping(a, b):
  for i in a:           
    for j in b:
      if i == j:
        return True
  return False
