#!/usr/bin/env python3
print("Justin Barr's MPG App") # Prints my name and file name

# display a welcome message
# print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
# mpg = miles_driven / gallons_used
mpg = round(miles_driven / gallons_used)

# calculate costs
total_gas_cost = gallons_used * cost_per_gallon
cost_per_mile = total_gas_cost / miles_driven
            
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Gas Cost:\t\t\t" + str(total_gas_cost))
print("Cost Per Mile:\t\t\t" + str(cost_per_mile))
print()
print("Bye")


