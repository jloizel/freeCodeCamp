# Convert all number inputs to integers to use in the formulas later on
# Convert all word inputs to lowercase to check match later on

import math

# Obtain the user's input and convert to lowercase
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
type = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Set rules to follow if the user selects 'investment'
if type == "investment":
    print("You have selected 'investment'")
    money = int(input("How much money are you investing? "))
    rate1 = int(input("What interest rate are you looking for? Please enter the number only. "))
    time = int(input("How many years are you planning on investing for? "))
    interest = (input("Please input whether you want 'simple' or 'compound' interest. ").lower())
    # Set rules to follow depending on which sub-option the user inputs
    if interest == "simple":
        total = int(money * (1 + (rate1/100) * time ))
        print("You're potential money gain is £{0}".format(total))
    elif interest == "compound":
        total = int(money * math.pow((1 + (time/100)),time))
        print("You're potential money gain is £{0}".format(total))
    else:
        print("Please enter one of the two options only.")
# Set rules to follow if the user selects 'bond'
elif type == "bond":
    print("You have selected 'bond'")
    house_value = int(input("Please enter the value of your house. "))
    rate2 = int(input("What interest rate are you looking for? Please enter the number only. "))
    period = int(input("Please enter the number of months you plan on taking to repay the bond. "))
    repayment = int(((rate2/100)*house_value)/((1+(rate2/100))**(-period)))
    print("You will have to repay £{0} each month.".format(repayment))
else:
    print("Error, please enter one of the two possible options only")

