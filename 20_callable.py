"""Instances of class that implement ``__call__`` can be invoked like functions."""

class Add:
    def __call__(a: int, b: int):
        return a + b

add = Add()
add(5, 5)  # 10
