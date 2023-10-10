#!/usr/bin/env python3
#Name: (Justin Barr)
#Class: (INFO 1200)
#Section: (001)
#Professor: (Crandall)
#Date: 2/10/2023
#Project #: 2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.
# Display a welcome message
print("Justin Barr's Tip Calculator") 
print()

# Create variables from user input
costOfMeal = float(input("Cost of Meal:\t"))
tipPercentage = float(input("Tip Percentage:\t"))
print()

# Calculate tip amount and total check
tip = round(costOfMeal * (tipPercentage / 100), 2)
totalCheck = costOfMeal + tip

# Display tip amount and total check
print("Tip Amount:\t" + str(tip))
print("Total Amount:\t" + str(totalCheck))
