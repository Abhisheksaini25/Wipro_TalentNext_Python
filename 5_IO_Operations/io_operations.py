# 1. Write a program to read the entire content from a .txt file and display it to the user.

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

file_path = 'file.txt'
file_content = read_file(file_path)
print(file_content)

# 2. Write a program to read the first n lines from a .txt file. The value of n should be taken as input from the user.

def read_first_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = [next(file) for _ in range(n)]
    return ''.join(lines)

n = int(input("Enter the number of lines to read: "))
first_n_lines = read_first_n_lines(file_path, n)
print(first_n_lines)

# 3. Wrte a program to accept input from the user and append it to a text file.

def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content + '\n')

content = input("Enter the content to append to the file: ")
append_to_file(file_path, content)

# 4. Write a program to read contents from a .txt file line by line and store each line into a list.

def read_lines_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

lines_list = read_lines_to_list(file_path)
print(lines_list)

# 5. Write a program to find the longest word from the contents of a text file. Assume that there is only one longest word in the file.

def find_longest_word(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    longest_word = max(words, key=len)
    return longest_word

longest_word = find_longest_word(file_path)
print("The longest word is:", longest_word)

# 6. Write a program to count the frequency of a word entered by the user in a text file.

def count_word_frequency(file_path, word):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.lower().split().count(word.lower())

word = input("Enter the word to count its frequency: ")
frequency = count_word_frequency(file_path, word)
print(f"The word '{word}' occurs {frequency} times in the file.")