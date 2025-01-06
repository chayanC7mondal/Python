#6.	Write a program to generate the Fibonacci sequence up to a given number of terms. The user should input the number of terms, and the program should display the sequence.

num_terms = int(input("Enter the number of terms: "))

if num_terms <= 0:
    print("Invalid input. Please enter a positive number.")
else:
    a=0
    b=1

    for i in range(num_terms):
        print(a)
        a,b = b,a+b