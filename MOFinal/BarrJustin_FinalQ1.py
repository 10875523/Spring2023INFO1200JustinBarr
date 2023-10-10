#!/usr/bin/env python3

TAX = 0.06 #Defines universal constant

def sales_tax(t):
    """
    Finds the sales tax amount and returns it
    """
    sales_tax = t * TAX #Calculates sales tax from pre-tax total
    return sales_tax #Returns sales tax

def main():
    """
    Runs as the main function to recieve user input and call appropriate functions
    """
    print("Sales Tax Calculator\n") #Welcome message
    while True: #While loop to ensure user enters proper input
        try: #Validation to make sure user enters number
            total = float(input("Enter total: ")) #Sets variable to the input of the user
            if total < 0: #Validation to check if user enters negative total
                print("Please enter a positve value for the total.") #Formatted error message
                continue #Redirects to the start of the while loop
            else: #If user input is valide, executes code inside
                break #Allows the code to break from while loop and complete calculations
        except: #If user input is not a number, executes code inside
            print("Please enter a decimal value for the total.") #Formatted error message
    total_after_tax = round(total + sales_tax(total), 2) #Sets variable to the user input plus the sales_tax function call and rounds to 2 decimal places
    print("Total after tax: ", total_after_tax) #Prints results
    
#Calls main function if file is the executing file
if __name__ == "__main__":
    main()
