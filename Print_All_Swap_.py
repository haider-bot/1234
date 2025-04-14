def median_decorator(f):
    def wrapper(self):
        return f(self)
    return wrapper

class Class:
    def __init__(self, nums):
        self.nums = nums
        self.solution = []

    def permute(self):
        from itertools import permutations
        self.solution = list(permutations(self.nums))

    @median_decorator
    def mediana(self):
        a = sorted(p[0] for p in self.solution)
        n = len(a)
        mid = n // 2
        return a[mid] if n % 2 else (a[mid - 1] + a[mid]) / 2

    def __str__(self):
        return f"Перестановки {self.nums}: {self.solution}"


a = Class([1, 2, 3])
a.permute()
print(a)
print(a.mediana())

b = Class([0, 3])
b.permute()
print(b)
print(b.mediana())


