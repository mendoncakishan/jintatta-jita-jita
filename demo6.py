# wap to print char and numm differently from a string
m=input("enter a string:")
numbers = ""
characters = ""
i = 0
while i < len(m):
        char = m[i]
        if char.isdigit():
            numbers += char
        else:
            characters += char
        i += 1
print("Characters in the string:", characters)
print("Digits in the string:", numbers)



