#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)

#Using the input function to ask the user how many terms of the Fibonacci sequence they want.

#Validating that the input is a positive integer.
while True:
    user_input = input("How many terms do you want?") # Prompt the user for the number of terms.

    if user_input.isdigit():
        number_of_terms = int(user_input)
        break #If it's a valid input, then exit the loop
    else:
        print("Please enter a positive integer") #If the input is invalid, display an error message and prompt again

# Use a for loop to print the Fibonacci sequence up to that many terms.
a = 0
b = 1 

for i in range (number_of_terms):
  print(a, end=" ")
  temp = a #prints the current value of a
  a = b
  b =  temp + b
      #Update a and b
