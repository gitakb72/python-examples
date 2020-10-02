"""
Functional programming in Python
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubles = list(map(lambda x: x * 2, numbers))
print(doubles) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # [2, 4, 6, 8, 10]
