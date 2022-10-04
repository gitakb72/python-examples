def next_num(i):
    yield i
    yield from next_num(i+1)

iterator = next_num(10)

assert next(iterator) == 10
assert next(iterator) == 11
assert next(iterator) == 12
