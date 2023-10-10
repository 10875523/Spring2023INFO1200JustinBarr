#!/usr/bin/env python3
        
def get_number(prompt, low, high):
    """
    Validates user input for float
    """
    while True:
        #Checks for errors
        try:
            number = float(input(prompt))#Sets number equal to input if valid
        except:
            #Error message if invalid
            print("You entered an invalid number. Please try again.")
            continue
        #Checks if the user input is within the bounds for computation
        if number > low and number <= high:
            return number#Returns Input
        else:
            #Error Message
            print(f"Entry must be greater than {low} " 
                  f"and less than or equal to {high}.")
            
def get_integer(prompt, low, high):
    """
    Validates user input for integer
    """
    while True:
        #Checks for errors
        try:
            number = int(input(prompt))#Sets number equal to input if valid
        except:
            #Error message
            print("You entered an invalid number. Please try again.")
            continue
        #Checks if the user input is with the bounds for computation
        if number > low and number <= high:
            return number#Returns input
        else:
            #Error message
            print(f"Entry must be greater than {low} " 
                  f"and less than or equal to {high}.")


def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        #Prints formatted results
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    #Exit message
    print("Bye!")
    
#Runs main if its meant to
if __name__ == "__main__":
    main()
