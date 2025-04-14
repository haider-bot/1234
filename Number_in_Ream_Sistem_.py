def cache_result(method):
    cache = {}
    def wrapper(self):
        if self.num not in cache:
            result = method(self)
            cache[self.num] = result
        return cache[self.num]
    return wrapper

class Class:
    def __init__(self, num):
        self.num = num
        self.solution = ""

    @cache_result
    def intToRoman(self):
        val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        rom = ["I", "II", "III", "IV",
               "V", "VI", "VII", "VIII",
               "IX", "X"]

        if self.num in val:
            self.solution = rom[self.num - 1]
        else:
            self.solution = "?"
        return self.solution

    def __str__(self):
        return f"Число {self.num} в римской системе счисления равно {self.solution}"

a = Class(8)
a.intToRoman()
print(a)

b = Class(10)
b.intToRoman()
print(b)

