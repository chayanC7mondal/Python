#4.	Write a program to reverse a string entered by the user. Display the reversed string as output.

#word = input("Enter a word: ")
#print(f"The reversed word is: {word[::-1]}")

# Get input from the user
user_string = input("Enter a string to reverse: ")

# Initialize an empty string to store the reversed string
reversed_string = ""

# Loop through the original string in reverse order
for char in user_string:
    reversed_string = char + reversed_string

# Display the reversed string
print(f"The reversed string is: {reversed_string}")