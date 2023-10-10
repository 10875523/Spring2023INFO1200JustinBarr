#Name: (Justin Barr)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 2/18/2023
#Project #: MO4_P3
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#Prints a welcome Message
print("Justin Barr's Change Calculator")
print()

#Creates a variable to let the program run until the user quits
choice = "y"
while choice.lower() == "y":
    #Gets user input for calculations
    cents = int(input("Enter number of cents (0-99): "))
    print()
    
    #Creates variables and calculates quarters, dimes, nickels, and pennies
    quarters = cents // 25
    cents = cents % 25
    dimes = cents // 10
    cents = cents % 10
    nickels = cents // 5
    cents = cents % 5 
    pennies = cents
    
    #Print results
    print("Quarters: ", quarters)
    print("Dimes: ", dimes)
    print("Nickels: ", nickels)
    print("Pennies: ", pennies)
    print()
    
    #Checks to see if user wants to continue
    choice = input("Continue? (y/n): ")
    print()
    
#Exit message 
print("Bye!")
