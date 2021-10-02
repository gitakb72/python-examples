def add(a: int, b: int) -> int:
    return a + b

the_total: int = add(5, 10)
assert the_total == 15

def append(lst: list[int], item: int) -> None:
    lst.append(item)

the_list: list[int] = [1, 2, 4]
append(the_list, 8)
assert the_list[-1] == 8

print('All ok!')