"""
Program: coupon_calculations.py
Author: Jessie Horvath
Last date modified: 01/30/2022

The purpose of this program is to prompt users for the following inputs:
- purchase amount
- cash-off coupon and the amount
- percentage-off coupon and the amount
and to calculate the subtotal of the final purchase after coupons, and sales tax.
Then, shipping is calculated based on the subtotal price to give the user their
final total price.
"""
print("Hello, thank you for shopping at SuperAwesomeCouponDealsAndStuff.com \n")
price_str = input("Please enter the purchase amount: ")
price = float(price_str)

cash_off_answer = input("Do you have any cash-off coupons? Yes or No ")
if cash_off_answer == "Yes" or cash_off_answer == "yes":
    cash_off_str = input("Please enter the dollar amount of the coupon: ")
    cash_off = float(cash_off_str)
else:
    print("That's too bad...\n")

percent_off_answer = input(
    "Do you have any percentage off coupons? Yes or No ")
if percent_off_answer == "Yes" or percent_off_answer == "yes":
    percent_off_str = input("Please enter the percentage off amount: ")
    percent_off = float(percent_off_str)
    # If the user inputs percentage as a whole number, convert to decimal for calculations
    if percent_off > 1:
        percent_off /= 100
else:
    print("That's too bad...\n")

# Price after coupons and sales tax
SALES_TAX_MULTIPLIER = 1.06  # sales tax rate is 6%
if cash_off_answer == "Yes" or cash_off_answer == "yes":
    if percent_off_answer == "Yes" or percent_off_answer == "yes":
        subtotal = ((1 - percent_off) * (price - cash_off)) * \
            SALES_TAX_MULTIPLIER
    else:
        subtotal = (price - cash_off) * SALES_TAX_MULTIPLIER
elif percent_off_answer == "Yes" or percent_off_answer == "yes":
    subtotal = ((1 - percent_off) * price) * SALES_TAX_MULTIPLIER
else:
    subtotal = price * SALES_TAX_MULTIPLIER

print(f"Your subtotal comes to ${subtotal:.2f}.\n")
print("Calculating total after shipping...\n")

# Price after shipping
if subtotal <= 10:
    total = subtotal + 5.95
elif 10 < subtotal <= 30:
    total = subtotal + 7.95
elif 30 < subtotal <= 50:
    total = subtotal + 11.95
else:
    total = subtotal

print(f"Your total comes to ${total:.2f}.")
