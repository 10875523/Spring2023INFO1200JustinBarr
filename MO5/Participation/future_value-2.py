#!/usr/bin/env python3

#Imports validation file
import validate as v

#Welcome message
print("Barr's Validated Future Value App")
print()
        
def calculate_future_value(monthly_investment, yearly_interest, years):
    """
    Calculates a future value of an investment for a duration of years

    Args:
        monthly_investment (float): Amount invested monthly
        yearly_interest (float): Interest amount per year
        years (int): Amount of years for investment

    Returns:
        float: Future value of investment
    """
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    #Return future value variable
    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user by referencing validate file
        monthly_investment = v.get_float("Enter monthly investment:\t", 0, 1000)
        print()
        yearly_interest_rate = v.get_float("Enter yearly interest rate:\t", 0, 15)
        print()
        years = v.get_int("Enter number of years:\t\t", 0, 50)
        print()

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    #Exit message
    print("Bye!")
    
#Calls main function
if __name__ == "__main__":
    main()
