from abc import ABC, abstractclassmethod, abstractmethod

class Abs(ABC):
    @abstractmethod
    def get_name(self):
        pass

class Con(Abs):
    def get_name(self):
        return f"Name"

try:
    abs = Abs()
except TypeError as te:
    assert "Can't instantiate abstract class Abs" in str(te)

con = Con()
print(con.get_name())  # Name
