"""
Comparison of boolean operators
"""

t1 = True
t2 = True
f1 = False
f2 = False

print(t1 and t2) # True
print(t1 and f2) # False
print(f1 and t2) # False
print(f1 and f2) # False

print(t1 or t2) # True
print(t1 or f2) # True
print(f1 or t2) # True
print(f1 or f2) # False

print(not True) # False
print(not False) # True
