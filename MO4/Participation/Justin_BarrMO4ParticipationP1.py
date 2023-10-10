#!/usr/bin/env python3

# display a welcome message
print("Justin Barr's Per Gallon application")
print()

#Makes the program run until created variable is no longer y
another_trip = "y"
while another_trip == "y":
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))
    print()

    #Validates inputs from user
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon, total cost, and cost per mile
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:          ", mpg)
        total_gas_cost = round(gallons_used * cost_per_gallon, 1)
        print("Total cost of gas used:    ", total_gas_cost)
        cost_per_mile = round(total_gas_cost / miles_driven, 1)
        print("Cost per mile:             ", cost_per_mile)
        print()

    #Checks to see if the user wants to enter another trip
    another_trip = input("Get entries for another trip (y/n)? ")
    print()
print("Bye")



