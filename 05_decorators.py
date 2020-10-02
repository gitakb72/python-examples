"""
Decorate a function
"""

def abs(func):
  def inner(a, b):
    if a >= b:
      return func(a, b)
    else:
      return func(b, a)
  return inner

@abs
def diff(a, b):
  return a - b
  
print(diff(3, 5)) # 2
print(diff(5, 3)) # 2
