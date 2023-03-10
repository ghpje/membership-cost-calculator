# Membership cost calculator
# App to help you calculate the cost of a membership over time

import os
from time import sleep

# Clear screen for linux or mac
if(os.name == 'posix'):
   os.system('clear')
# Clear screen for windows
else:
   os.system('cls')

# Welcome header
print("**************************")
print("MEMBERSHIP COST CALCULATOR")
print("**************************")

# Default values
monthly_fee = 17.99
annual_fee = 49.99
initiation_fee = 59.00
total_years = 1

# Prompt to change default fee values
change_defaults = input("Would you like to use the default fees based on the Fitness 19 Basic plan? (Y/N): ").upper()
print("")

# If no, set fee values
if change_defaults == "N":
    monthly_fee = float(input("What is the monthly fee?: "))
    annual_fee = float(input("What is the annual fee?: "))
    initiation_fee = float(input("What is the initiation fee (also known as the Enrollment Fee)?: "))
    total_years = int(input("How many years?: "))
    print("")
# If yes, use defaults
elif change_defaults == "Y":
    print("Using default values (Fitness 19 Basic Plan)")
    total_years = int(input("How many years?: "))
# If invlid, use defaults
else:
    print("Invalid input. Using default values (Fitness 19 Basic Plan)")

# Print results
print("")
print(f"The monthly fee is: ${monthly_fee}")
print(f"The annual fee is: ${annual_fee}")
print(f"The initiation fee (also known as the Enrollment Fee) is: ${initiation_fee}")
first_month_dues = monthly_fee
print(f"First month's dues: ${monthly_fee}")
#last_month_dues = monthly_fee
#print(f"Last month's dues: ${monthly_fee}")
total_init_payment = initiation_fee + first_month_dues# + last_month_dues
print(f"Total due at signing: ---> ${round(total_init_payment,2)} <---")
print("")
total_first_year = total_init_payment + (monthly_fee * 11)
print(f"The first year will cost: ${round(total_first_year,2)}")
print("")
total_second_year = (monthly_fee * 12)
print(f"The second year will cost: ${round(total_second_year,2)}")
print("")
if total_years == 1:
    total_cost = total_init_payment + (monthly_fee * 11)
    print(f"The total cost for {total_years} year will be: ${round(total_cost,2)}")
elif total_years > 1:
    total_cost = total_init_payment + (monthly_fee * 11) + (monthly_fee * 12 * total_years)
    print(f"The total cost for {total_years} years will be: ${round(total_cost,2)}")
else:
    print("Invalid input")
print("")