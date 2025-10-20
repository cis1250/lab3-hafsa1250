#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re
import string

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# 1. Prompt the user
user_sentence = input("Enter a sentence: ")
while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_input = input("Enter a sentence: ")

# 2. Split the sentence into words
updated_sentence = user_sentence #removing punctuation from being counted as a word
for p in string.punctuation:
    updated_sentence = updated_sentence.replace(p, '')

updated_sentence = updated_sentence.lower() #Converting to lowercase so words with diff capitalizations are treated as the same word

words_list = updated_sentence.split() #Split the input sentence into a list of words using the split() method

# 3. Create lists
words = []
frequencies = []

# 4. Iterate through words and update frequencies
for word in words_list: #Iterate through the list of words
    if word in words: #Check for existence
        index = words.index(word)
        frequencies[index] += 1 #Update frequency: If the word exists, update its frequency in the corresponding list
    else:
        words.append(word) #Otherwise, append both the word and a frequency of 1 to the lists.
        frequencies.append(1)
    
# 5. Print results
for i in range(len(words)):
    print(f"{words[i]}: {frequencies[i]}")


    
