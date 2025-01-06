#7.	Write a program to check whether a given number is a prime number. Accept an integer input from the user and display the result.


# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num // 2 + 1):  # Check divisors up to half of the number
        if num % i == 0:
            return False
    return True

# Input from the user
number = int(input("Enter a number: "))

# Check and display the result
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")