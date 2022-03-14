"""
Program: average_scores.py
Author: Jessie Horvath
Last date modified: 01/22/2022

The purpose of this program is to accept input from a user for
first and last name, age, and three test scores. It then returns 
the first and last names, age, and average of the test scores in 
the following format:
Last Name, First Name age: Age average score: Average Score
"""

# First save all user input as individual variables
first_name = input("What is your first name? ")
last_name = input("And your last name? ")
age = input("How old are you? ")

first_score = input("Enter your first test score: ")
second_score = input("Enter your second test score: ")
third_score = input("Enter your third test score: ")

# Convert str variables to int to do arithmetic
first_score_int = int(first_score)
second_score_int = int(second_score)
third_score_int = int(third_score)

# Calculate the average test score using the int variables
average_score = (first_score_int + second_score_int + third_score_int) / 3

# Print the desired format with the input information
print(f"{last_name}, {first_name} age: {age} average grade: {average_score:5.2f}")

"""
Manual test examples:
With user input of Jessie Horvath as first and last names, age of 24, and
test scores of 90, 98, and 62 the output looks like this:
Horvath, Jessie age: 24 average grade: 83.33

With user input of Peter Parker as first and last names, age of 18, and 
test scores of 78, 82, and 95 the output looks like this:
Parker, Peter age: 18 average grade: 85.00
"""
