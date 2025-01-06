#3.	Write a program to calculate the factorial of a given number using loops. The number should be entered by the user, and the program should handle invalid input (negative numbers).

number = int(input("Enter a number: "))
if number < 0:
    print("Invalid input. Please enter a positive number.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}")
