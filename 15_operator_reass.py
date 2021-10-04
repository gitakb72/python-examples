class Item:
    def __init__(self, x):
        self.x = x

    def __add__(self, o):
        return self.x + o.x

two = Item(2)
five = Item(5)
print(two + five)  # 7
