# Write a Python program that continuously prompts the user to enter numbers. Calculate and print the sum of all entered numbers until the user enters -1 to quit.


num = int(input("Enter a number (enter -1 to quit): "))
i = 0
while num != -1:
    i += num
    num = int(input("Enter a number (enter -1 to quit): "))
print("Sum of all entered numbers:", i)
