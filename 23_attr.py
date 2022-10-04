class X:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        else:
            raise AttributeError(f"No attr: '{key}'")

x = X(first_name="First", last_name="Last")

assert x.get("first_name") == "First"
assert x.get("last_name") == "Last"
try:
    x.get("middle_name")
except AttributeError:
    print("All OK!")
