def sum_decorator(func):
    def wrapper(self):
        return sum(self.nums)
    return wrapper

class Class:
    def __init__(self, nums):
        self.nums = nums
        self.solution = []

    def removeDuplicates(self):
        self.solution = []
        for i in self.nums:
            if i not in self.solution:
                self.solution.append(i)
        while len(self.solution) < len(self.nums):
            self.solution.append('_')

    def __str__(self):
        return f"После преобразования массив {self.nums} будет выглядеть так: {self.solution}"

    @sum_decorator
    def all_sum(self):
        pass

a = Class([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
a.removeDuplicates()
print(a)
print(a.all_sum())

b = Class([0, 1, 1, 3, 3, 4, 4, 4, 4, 5])
b.removeDuplicates()
print(b)
print(b.all_sum())

"""
Выводы (принты)

После преобразования массив [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] будет выглядеть так: [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']
17

После преобразования массив [0, 1, 1, 3, 3, 4, 4, 4, 4, 5] будет выглядеть так: [0, 1, 3, 4, 5, '_', '_', '_', '_', '_']
29

"""
