class Item:
    def __init__(self, name):
        self.name = name
        
    def __eq__(self, other):
        return self.name == getattr(other, 'name', None)
    
    def __str__(self):
        return f"<Item: {self.name}>"
        
    def __repr__(self):
        return str(self)

i1 = Item("item")
i2 = Item("item")
assert i1 == i2  # uses ``__eq__`` function
assert str(i1) == "<Item: item>"  # uses ``__str__`` function
