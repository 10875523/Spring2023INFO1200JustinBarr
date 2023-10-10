#! bin/usr/env python3
#Name: Justin Barr
#Class: INFO 1200
#Section: X01
#Professor: Crandall
#Date: 2/21/2023
#Project #: MO5_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import JBconverter as c #Imports converter file to call on those functions

#Welcome message
print("Justin Barr's Feet / Meters Converter")
print()

def fm_welcome():
    """
    Define a function that prints ANOTHER welcome message
    """
    #Prints a welcome message
    print("Justin's Feet and Meters Converter")
    print()    

def fm_menu():
    """
    Define a function that prints a menu
    """
    #Prints a menu
    print("Conversions Menu:")
    print()
    print("a. Feet to Meters")
    print("b. Meters to Feet")

def main():
    #Define main function and call fm_welcome function
    fm_welcome()
    while True: #While true loop
        fm_menu() #Call fm_menu
        choice = input("Select a conversion (a/b): ") #Set variable equal to user input
        print() #Spacing
        #Validate user input, gets more user input for proper function, and calls the correct function
        if choice.lower() == "a":
            feet = float(input("Enter feet: "))
            meters = c.to_meters(feet)
            print(round(meters, 2), "meters")
        elif choice.lower() == "b":
            meters = float(input("Enter Meters: "))
            feet = c.to_feet(meters)
            print(round(feet, 2), "feet")
        else:
            print("You did not enter a valid selection.")
            print

        #Gets user input to see if program continues
        print()
        more = input("Would you like to perform another conversion? (y/n): ")
        print()

        #Checks user input to know if quitting
        if more.lower() !=  "y":
            print("Thanks, bye!")
            break

if __name__ == "__main__": main()