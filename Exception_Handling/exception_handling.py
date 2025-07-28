# 1. Write a program to accept two numbers from the user and perform division. 
# If any exception occurs, print an error message or else print the result.

def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    else:
        print("Result:", result)
divide_numbers()

# 2. Write a program to accept a number from the user and check whether it's 
# prime or not. If user enters anything other than number, handle the 
# exception and print an error message.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_prime():
    try:
        number = int(input("Enter a number: "))
        if is_prime(number):
            print(number, "is a prime number.")
        else:
            print(number, "is not a prime number.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

check_prime()

# 3. Write a program to accept the file name to be opened from the user. If 
# file exists, print the contents of the file in title case. If not, handle 
# the exception and print an error message.

def read_file():
    file_name = input("Enter the file name to open: ")
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            print(contents.title())
    except FileNotFoundError:
        print("Error: File not found.")

read_file()

# 4. Declare a list with 10 integers and ask the user to enter an index. 
# Check whether the number at that index is positive or negative. If any 
# invalid index is entered, handle the exception and print an error message.

def check_number_at_index():
    numbers = [10, -5, 3, 8, -2, 0, 7, -1, 4, 6]
    try:
        index = int(input("Enter an index (0-9): "))
        if numbers[index] > 0:
            print("The number at index", index, "is positive.")
        else:
            print("The number at index", index, "is negative.")
    except IndexError:
        print("Error: Invalid index. Please enter a number between 0 and 9.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

check_number_at_index()
