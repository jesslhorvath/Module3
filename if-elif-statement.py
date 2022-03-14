"""
Program: if-elif-statement.py
Author: Jessie Horvath
Last date modified: 01/30/2022

The purpose of this program is to ask users to sign up for a subscriptiob program
and then inquire which level of the program they would like to purchase using
if statements.
"""

print("Would you like to sign up for Programmer's Toolkit Monthly Subscription Box?")

# I added the data validation step for this section to only accept upper case letters.
answer = input("Y or N? ")
while not answer.isupper():
    answer = input("Error: Enter Y or N: ")

if answer == "Y":
    level = input(
        "Select a level: Platinum, Gold, Silver, Bronze, Free Trial:  ")
    print("The cost of this level is: ")
    if level == "Platinum" or "platinum":
        print("$60")
    elif level == "Gold" or "gold":
        print("$50")
    elif level == "Silver" or "silver":
        print("$40")
    elif level == "Bronze" or "bronze":
        print("$30")
    else:
        print("Free")

else:
    print("Goodbye")
