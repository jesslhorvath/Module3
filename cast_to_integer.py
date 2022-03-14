"""
Program: cast_to_integer.py
Author: Jessie Horvath
Last date modified: 01/16/2022

The purpose of this program is to accept any input, 
convert to a integer type and output the integer. 
"""

print("Enter any number", end=' ')
number = input()

float_for_conversion = float(number)
float_to_int = int(float_for_conversion)

print(f"Your integer is: {float_to_int}")

# Testing
# Input     Expected Output     Actual Output
#   4               4                 4
#   6.5             6                 6
#   2.3             2                 2
#  'hello'         error            error
# The string 'hello' is not converted to an integer because it cannot be converted to a float (step 1).
