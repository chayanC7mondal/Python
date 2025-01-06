#9.	Write a Python program to count the total number of digits in a number using a while loop.

# Input from the user
num = int(input("Enter a number: "))

# Initialize count to 0
count = 0

# Handle negative numbers
if num < 0:
    num = abs(num)

# Check if the number is zero
if num == 0:
    count = 1
else:
    # Loop to count digits
    while num > 0:
        num //= 10  # Remove the last digit
        count += 1  # Increment the digit count

print(f"The total number of digits is: {count}")
