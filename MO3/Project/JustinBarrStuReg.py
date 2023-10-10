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
print("Justin Barr's Registration App") 
print()

# Get user inputs
firstName = input("First name:\t")
lastName = input("Last name:\t")
birthYear = input("Birth Year:\t")

# Display welcome message
print()
print(f"Welcome {firstName} {lastName}\t")
print("Your registration is complete\t")

# Create and display a temporary password
print()
password = f"{firstName}{lastName}*{birthYear}"
print(f"Your temporary password is: {password}\t")