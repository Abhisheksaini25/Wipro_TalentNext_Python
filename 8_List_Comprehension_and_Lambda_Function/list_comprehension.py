
# 1. Write a LC program to create an output dictionary which contains only  the odd number that are present in the input
# list as keys and their squares as values.

ip = [1,2,3,4,5,6,7]

op = {x:x**2 for x in ip if x%2!=0}
print(op)

# 2. Make a dictionary of the 26 english alphabets mapping each with the corresponding integer.

import string
alphabets = string.ascii_lowercase
alphabet_dict = {char: idx + 1 for idx, char in enumerate(alphabets)}
print(alphabet_dict)