class Adder():
    def __init__(self) -> None:
        self.nums: list[int] = []

    def inject(self, num: int) -> None:
        self.nums.append(num)

    def __call__(self) -> int:
        return sum(self.nums)


a = Adder()
a.inject(2)
a.inject(5)
print(a())  # 7