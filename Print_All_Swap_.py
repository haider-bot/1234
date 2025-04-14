def median_decorator(func):
    def wrapper(self):
        return func(self)
    return wrapper

class Class:
    def __init__(self, nums):
        self.nums = nums
        self.solution = []

    def permute(self):
        self.solution = []
        self._permute(self.nums, 0)

    def _permute(self, arr, start):
        if start == len(arr):
            self.solution.append(arr[:])
        else:
            for i in range(start, len(arr)):
                arr[start], arr[i] = arr[i], arr[start]
                self._permute(arr, start + 1)
                arr[start], arr[i] = arr[i], arr[start]

    @median_decorator
    def mediana(self):
        a = sorted(self.nums)
        n = len(a)
        mid = n // 2
        return a[mid] if n % 2 else (a[mid - 1] + a[mid]) / 2

    def __str__(self):
        return f"Для массива {self.nums} будут такие перестановки: {self.solution}"

a = Class([1, 2, 3])
a.permute()
print(a)
print(a.mediana())

b = Class([0, 3])
b.permute()
print(b)
print(b.mediana())


