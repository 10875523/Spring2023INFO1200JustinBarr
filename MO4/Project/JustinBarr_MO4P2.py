#Name: (Justin Barr)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 2/18/2023
#Project #: MO4_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#Prints a welcome Message
print("Justin Barr's Tip Converter")
print()

#Creates two variables to hold percentages to work with and one for the user input of meal cost
tip_percentage = [15, 20, 25]
meal_cost = float(input("Cost of Meal: "))
print()

#Loop through the percentages, calculate the tip from percentage, then calculate meal total. Print Results
for i in range(len(tip_percentage)):
    print(tip_percentage[i], "%")
    tip_percent = tip_percentage[i] / 100
    tip_amount = round((meal_cost * tip_percent), 2)
    print("Tip amount: ", tip_amount)
    print("Total amount: ", meal_cost + tip_amount)
    print()
