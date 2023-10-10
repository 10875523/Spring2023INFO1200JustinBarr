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
print("Justin Barr's Pay Check Calculator App") 
print()

# Create variables and get user input for calculations
hoursWorked = float(input("Hours worked:\t"))
payRate = float(input("Hourly Rate:\t"))
print()

# Calculate and display gross pay
grossPay = hoursWorked * payRate
print("Gross Pay:\t" + str(grossPay))

# Finds the tax amount and displays it
taxRate = .18
print("Tax Rate:\t18%")
taxAmount = grossPay * (taxRate)
print("Tax Amount:\t" + str(taxAmount))

# Find and display take home pay
takeHomePay = round(grossPay - taxAmount, 2)
print("Take Home Pay:\t" + str(takeHomePay))