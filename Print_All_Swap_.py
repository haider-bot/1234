from itertools import permutations

def with_median(cls):
    def mediana(self):
        sorted_nums = sorted(self.nums)
        n = len(sorted_nums)
        if n % 2 == 1:
            return sorted_nums[n // 2]
        else:
            return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    cls.mediana = mediana
    return cls

@with_median
class Class:
    def __init__(self, nums):
        self.nums = nums
        self.solution = []

    def permute(self):
        self.solution = [list(p) for p in permutations(self.nums)]

    def __str__(self):
        return f"Для массива {self.nums} будут такие перестановки: {self.solution}"

a = Class([1, 2, 3])
a.permute()
print(a)            
print(a.mediana())  
