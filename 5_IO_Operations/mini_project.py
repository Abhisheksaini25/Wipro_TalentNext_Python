#Project 1: 
'''Secret Message Decoder from a Text File
Question
Your friend has sent you a text file containing n lines. He sent a secret message with it, which 
tells you the place and time where you have to go and meet him.
He challenges you to find it without seeing the content of the file directly. Instead, you must 
write a Python program that analyses the text file and extracts the hidden information using the 
following hints:
________________________________________
Hints to find the secret message:
1.	The number of lines in the file tells you the meeting time.
o	Condition: 1 × number of lines < 24
o	If the number of lines is greater than 12, convert it to 12-hour format.
	E.g., If number of lines = 15 → Time is 3 PM
	If number of lines = 10 → Time is 10 AM
2.	The word appearing the maximum number of times tells you the meeting place.
o	The meeting place will be a street name formed by the most frequent word + " Street".
	E.g., If the word Park appears the most → Meeting place: Park Street
________________________________________
 Explanation of the Sample
Let's say your text file (sample.txt) contains 20 lines and the word Apollo appears 25 times, which 
is the highest frequency of any word.
Then:
•	20 lines → 8 PM (12-hour format of 20)
•	Most frequent word: Apollo → Place: Apollo Street'''

def secret_message_decoder(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    num_lines = len(lines)
    if num_lines > 12:
        time = f"{num_lines - 12} PM"
    else:
        time = f"{num_lines} AM"
    
    word_frequency = {}
    for line in lines:
        words = line.split()
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1
    
    most_frequent_word = max(word_frequency, key=word_frequency.get)
    place = f"{most_frequent_word} Street"
    
    return time, place

file_path = 'sample.txt'
time, place = secret_message_decoder(file_path)
print(f"Meeting Time: {time}")
print(f"Meeting Place: {place}")
