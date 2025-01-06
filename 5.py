#5.	Write a program to check whether a given string or number is a palindrome. A palindrome reads the same backward as forward. Display whether the input is a palindrome or not.

# Get input from the user
user_string = input("Enter a string to reverse: ")

# Initialize an empty string to store the reversed string
reversed_string = ""

# Loop through the original string in reverse order
for char in user_string:
    reversed_string = char + reversed_string

if user_string == reversed_string:
    print(f"The input '{user_string}' is a palindrome.")

else :
    print(f"The input '{user_string}' is not a palindrome.")