t = ['a','b','c','d','e']

def chop(t):
  del t[0]
  del t[-1]
  return("None")

def middle(t):
  t.pop(0)
  t.pop(-1)
  print(t)

chop(t)
middle(t)
