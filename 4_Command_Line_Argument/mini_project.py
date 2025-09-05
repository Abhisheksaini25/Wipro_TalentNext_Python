# Project 1
'''Q1. Write a Python function that accepts a hyphen-separated sequence of 
colors as input and returns the colors in a hyphen-separated sequence after 
sorting them alphabetically.'''

def sort_colors(color_string):
    color_list = color_string.split('-')
    color_list.sort()
    return '-'.join(color_list)

'''Q2. Through command line arguments three strings separated by space are 
given to you. Each string is a series of numbers separated by hyphen(-). 
You like all the numbers in string 1 and dislike all the numbers in string 
2. Third string contains the numbers given to you.'''

import sys

def calculate_happiness(like_str, dislike_str, data_str):
    likes = set(like_str.split('-'))
    dislikes = set(dislike_str.split('-'))
    data = data_str.split('-')
    
    happiness = 0
    for num in data:
        if num in likes:
            happiness += 1
        elif num in dislikes:
            happiness -= 1
    return happiness

# Project 2
'''Q1. Write a function ispalindrome(name) that checks if the name is a 
palindrome.'''

def ispalindrome(name):
    return name == name[::-1]

'''Q2. Write a function count_the_vowels(name) to count vowels in a name.'''

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in name if ch in vowels)

'''Q3. Write a function frequency_of_letters(name) to count frequency of 
each letter.'''

def frequency_of_letters(name):
    freq = {}
    for ch in name:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

'''Q4. Spiritual function to return the sum of all numbers in a list.'''

def sum_of_list(lst):
    return sum(lst)

'''Q5. Write a function to return the reverse of a string.'''

def reverse_string(s):
    return s[::-1]

'''Q6. Write a function to calculate the factorial of a number.'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

'''Q7. Write a function to count uppercase and lowercase letters in a string.'''

def count_case(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return upper, lower

'''Q8. Write a function to print even numbers from a list.'''

def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

'''Q9. Write a function to check if a number is prime.'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

'''Q10. Write a program to remove given items from a set.'''

def remove_items(original_set, items_to_remove):
    return original_set - set(items_to_remove)

'''Q11. Write a program to create an intersection of sets.'''

def intersection_of_sets(set1, set2):
    return set1 & set2

'''Q12. Write a program to create a union of sets.'''

def union_of_sets(set1, set2):
    return set1 | set2

'''Q13. Write a program to find the maximum and minimum value in a set.'''

def max_min_in_set(s):
    return max(s), min(s)