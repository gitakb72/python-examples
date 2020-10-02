"""
Show how classes work
"""

class Person:
  def __init__(self, first_name, last_name):
    self.first_name = last_name
    self.last_name = last_name
    
  @property
  def full_name(self):
    return f'{first_name} {last_name}'

me = Person('Anandi', 'B')
print(me.full_name) # Anandi Bhanushali
