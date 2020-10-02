"""
See how readability is improved by comprehension
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [
  number
  for number in numbers
  if number % 2 == 0
]
odds = [
  number
  for number in numbers
  if number not in evens
]

print(evens) # [2, 4, 6, 8, 10]
print(odds) # [1, 3, 5, 7, 9]
