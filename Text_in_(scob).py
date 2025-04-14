def remove_parentheses(text):
    result = []
    level = 0
    for char in text:
        if char == '(':
            level += 1
        elif char == ')':
            if level > 0:
                level -= 1
        elif level == 0:
            result.append(char)
    return ''.join(result)

text = "Это пример (с вложенностью (да)) и скобками () в тексте."
print(remove_parentheses(text))

# я бы импортировал sys и re для удаления пробелов + для cntrl + D

