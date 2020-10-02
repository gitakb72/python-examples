"""
Flow with the control
"""

for i in range(3):
  print(i)
# Prints 0, 1, 2 on separate lines

i = 1
while i <= 3:
  print(i)
  i += 1
# Prints 1, 2, 3 on separate lines

def ifelse(var):
  if var:
    print('This is the if side')
  else:
    print('This is the else side')

ifelse(True) # This is the if side
ifelse(False) # This is the else side
