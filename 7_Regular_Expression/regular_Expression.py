import re

# 1. Write a program to find check if a string has only octal digits. 

given_string = ['789','123','004']

def is_octal(s):
    pattern = r'^[0-7]+$'
    return bool(re.match(pattern, s))

# 2. Extract the user if, domain name and suffix from the email addresses.

emails = ['zuk@facebook.com','sunder33@google.com','jeff42@amazon.com']

def extract_email_components(email):
    pattern = r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})'
    match = re.match(pattern, email)
    if match:
        return match.groups()
    return None

# 3. Split the following irregular sentence into proper words.

sentence = 'A, very     very; irregular_sentence'

def split_sentence(sentence):
    pattern = r'[;,\s]+'
    return re.split(pattern, sentence.strip())

# 4. Clean up the following tweet so that it contains only the user's message. That is, remove all URLs, hashtags, mentions, 
# punctuations, RTs and CCs.

tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0px0d cc: @garybernhardt #rstats'

def clean_tweet(tweet):
    tweet = re.sub(r'http\S+', '', tweet)  # Remove URLs
    tweet = re.sub(r'@\w+', '', tweet)     # Remove mentions
    tweet = re.sub(r'#\w+', '', tweet)     # Remove hashtags
    tweet = re.sub(r'\bRT\b', '', tweet)   # Remove RTs
    tweet = re.sub(r'\bCC\b', '', tweet)   # Remove CCs
    tweet = re.sub(r'[^\w\s]', '', tweet)  # Remove punctuations
    return tweet.strip()

# 5. Extract all the text portions between the tags from the following HTML code.


def extract_text_from_html(html):
    pattern = r'>([^<>]+)<'
    return re.findall(pattern, html)

#6. Given below list of words, identify the words that begin and end with the same character.

words = ['civic','trust','widows','maximum','musems','aa','as']

def words_same_start_end(words):
    pattern = r'^(.).*\1$'
    return [word for word in words if re.match(pattern, word)]