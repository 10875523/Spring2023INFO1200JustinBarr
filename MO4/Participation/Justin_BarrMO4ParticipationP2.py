#!/usr/bin/env python3

# display a welcome message
print("Welcome to Justin Barr's Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    #Creates variable, sets it to false, and runs program until it isn't false
    is_valid = False 
    while is_valid == False:
        #Gets input from user, validates input, and either exits while is_valid loop or has user reinput
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment >= 0 and monthly_investment < 1000:
            is_valid = True
        else:
            print("Entry must be greater than 0 and less than 1000. Please try again.")
    is_valid = False #Sets variable back to false

    while is_valid == False:
        #Gets input from user, validates input, and either exits while is_valid loop or has user reinput
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            is_valid = True
        else:
            print("Entry must be greater than 0 and less than or equal to 15. Please try again.")
    is_valid = False #Sets variable back to false
    while is_valid == False:
        #Gets input from user, validates input, and either exits while is_valid loop or has user reinput
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:
            is_valid = True
        else:
            print("Entry must be greater than zero and less than or equal to 50. Please try again.")

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    print() #Formatting

    # calculate the future value and print incrementally
    future_value = 0
    for i in range(months):
        if i % 12 == 0 and i != 0:
            print("Year = ", i // 12, "\tFuture Value = ", round(future_value, 2))
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
       
    # display the final result
    print("Year = ", i // 12 + 1, "\tFuture Value = ", round(future_value, 2))
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
