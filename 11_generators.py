def next_num(i):
    yield i
    yield from next_num(i+1)

iterator = next_num(10)

print(next(iterator)) # 10
print(next(iterator)) # 11
print(next(iterator)) # 12