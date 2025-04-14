class Class:
    def __init__(self, num):
        self.num = num
        self.solution = ""

    def countAndSay(self):
        s = "1"
        for _ in range(1, self.num):
            s = self.say(s)
        self.solution = s

    def say(self, s):
        result = ""
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result += str(count) + s[i - 1]
                count = 1
        result += str(count) + s[-1]
        return result

    def __str__(self):
        return "Результат после " + str(self.num) + " операций: " + self.solution

a = Class(4)
a.countAndSay()
print(a)

b = Class(7)
b.countAndSay()
print(b)
