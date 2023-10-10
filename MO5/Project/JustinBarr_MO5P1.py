#! bin/usr/env python3

#Name: Justin Barr
#Class: INFO 1200
#Section: 001
#Professor: Crandall
#Date: 2/21/2023
#Project #: MO5_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#Welcome message
print("Justin Barr's Even or Odd Checker")
print()

def is_even(num):
    """
    Check if num is even or odd
    """
    #Define function is_even to test if passed perameter is even or not and returning true or false accordingly
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    """
    Define main
    """
    #Welcome message again?
    print("Justin Barr's even or odd checker")
    print() 

    #Gets input from user and passes it through predefined function is_even
    my_num = int(input("Enter an integer: "))
    if  is_even(my_num):
        print("This is an even number.")
    else:
        print("This is an odd number.")

if __name__ == "__main__": main() #Calls the main function
