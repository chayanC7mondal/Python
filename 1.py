#1.	Write a program to check whether a given number is even or odd. Accept an integer input from the user and print the result.

number = int(input("Enter an integer: "))
if number%2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")