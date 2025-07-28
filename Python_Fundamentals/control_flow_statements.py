# Q1. Write a program to check if a given number is Positive, Negative or Zero.

def check_number(num):
    if num>0:
        print("The number is Positive.")
    elif num<0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")

# Q2. Write a program to check if a given number is Even or Odd.

def check_even_odd(num):
    if num%2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")

# Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

def same_last_digit(num1, num2):
    return num1%10 == num2%10

# Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.

def print_numbers_with_tabs():
    for i in range(1, 11):
        print(i, end=' ')

# Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.

def print_even_numbers(start, end):
    for num in range(start, end+1):
        if num%2 == 0:
            print(num)

# Q6. Write a program to check if a given number is prime or not.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True

# Q7. Write a program to print prime numbers between 10 and 99.

def print_prime_numbers(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=', ')

# Q8. Write a program to print the sum of all the digits of a given number.

def sum_of_digits(num):
    total = 0
    while num> 0:
        total+= num%10
        num//=10
    return total

# Q9. Write a program to reverse a given number and print.

def reverse_number(num):
    reversed_num = 0
    while num> 0:
        reversed_num = reversed_num*10 + num%10
        num//= 10
    return reversed_num

# Q10. Write a program to find if the given number is palindrom or not.

def is_palindrome(num):
    original_num = num
    reversed_num = reverse_number(num)
    return original_num == reversed_num