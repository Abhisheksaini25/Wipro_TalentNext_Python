#Project 1:
'''
Sort hyphen-separated colors alphabetically
'''
def sort_hyphenated_colors(color_string):
    colors = color_string.split('-')
    sorted_colors = sorted(colors)
    return '-'.join(sorted_colors)

# Project 2:
'''
This module provides:
- ispalindrome(name): Checks if a string is a palindrome.
- count_the_vowels(name): Counts vowels in the string.
- frequency_of_letters(name): Returns frequency of each character.
'''

def is_palindrome(name):
    return name == name[::-1]

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return count

def frequency_of_letters(name):
    frequency = {}
    for char in name:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

import mymodule

name = input("Enter name: ")

print(mymodule.ispalindrome(name))
print(mymodule.count_the_vowels(name))
print(mymodule.frequency_of_letters(name))

