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
monthly_fee = 34.99
annual_fee = 49.00
initiation_fee = 99.00

# Prompt to change defaults
change_defaults = input("Would you like to change the default values? (Y/N): ").upper()
print("")

# If yes, set fee values
if change_defaults == "Y":
    monthly_fee = float(input("What is the monthly fee?: "))
    annual_fee = float(input("What is the annual fee?: "))
    initiation_fee = float(input("What is the initiation fee?: "))
# If no or invalid, use defaults
elif change_defaults == "N":
    print("Using default values (LA Fitness example)")
else:
    print("Invalid input. Using default values (LA Fitness example)")

# Print results
print("")
print(f"The monthly fee is: ${monthly_fee}")
print(f"The annual fee is: ${annual_fee}")
print(f"The initiation fee is: ${initiation_fee}")
first_month_dues = monthly_fee
print(f"First month's dues: ${monthly_fee}")
last_month_dues = monthly_fee
print(f"Last month's dues: ${monthly_fee}")
total_init_payment = initiation_fee + first_month_dues + last_month_dues
print(f"Total due at signing: ---> ${round(total_init_payment,2)} <---")
print("")