#1. Function to return the sum of all numbers in a list

def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

#2. Function to return the reverse of a string.

def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

#3. Function to calculate and return the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

#4. Function to count uppercase and lowercase letters in a string.

def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

#5. Function to print even numbers from a given list

def print_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)

#6. Function to check if a number is prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True