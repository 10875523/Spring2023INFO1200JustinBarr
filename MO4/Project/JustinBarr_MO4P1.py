#Name: (Justin Barr)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 2/18/2023
#Project #: MO4_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#Prints a welcome Message
print("Justin Barr's Letter Grade Converter")
print()

#Creates a variable and while loop to let program loop until the user quits
choice = "y"
while choice.lower() == "y":
    #Create a variable to recieve percentage from user
    number = int(input("Enter Numerical Grade: "))
    #Determine the letter grade from the user input using if statements
    if number >= 94 and number <= 100:
        print("Letter Grade: A")
        print()
    elif number >= 90 and number <= 93:
        print("Letter Grade: A-")
        print()
    elif number >= 87 and number <= 89:
        print("Letter Grade: B+")
        print()
    elif number >= 83 and number <= 86:
        print("Letter Grade: B")
        print()
    elif number >= 80 and number <= 82:
        print("Letter Grade: B-")
        print()
    elif number >= 77 and number <= 79:
        print("Letter Grade: C+")
        print()
    elif number >= 73 and number <= 76:
        print("Letter Grade: C")
        print()
    elif number >= 70 and number <= 72:
        print("Letter Grade: C-")
        print()
    elif number >= 67 and number <= 69:
        print("Letter Grade: D+")
        print()
    elif number >= 63 and number <= 66:
        print("Letter Grade: D")
        print()
    elif number >= 60 and number <= 62:
        print("Letter Grade: D-")
        print()
    elif number >= 0 and number <= 59:
        print("Letter Grade: E")
        print()
    else:
        print("Please enter a number between 0 and 100")
        print()
    
    #Check to see if user wants to continue putting in grades
    choice = input("Continue? (y/n): ")
    print()
    
#Exit Message
print("Bye!")
