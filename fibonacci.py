#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

user_input = input("How many terms of the Fibonacci sequence do you want? ")
input = int(user_input)
print("User Input: ", input)

# variables for Fibonacci Sequence
a = 0
b = 1

if input >= 0:
  for i in range(input): 
    print("Expected Output: ", a, end=' ')
    print(a, end=' ')
    temp = a + b
    a = b
    b = temp
else: 
  print("Expected output: Please enter a positive integer.")
