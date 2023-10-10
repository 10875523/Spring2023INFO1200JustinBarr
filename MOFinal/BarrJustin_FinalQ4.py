#!/usr/bin/env python3

import csv #Imports CSV module

FILENAME = "D:/apartment_purchases.csv" #File name for csv file

def display_title():
    """Displays title for program
    """
    print("Investments Portfolio") #Welcome message
    print() #Formatting

def display_menu():
    """Displays menu for program
    """
    print("COMMAND MENU") #Menu title
    print() #Formatting
    print("view\t- View portfolio") #Menu Function
    print("total\t- View total investment value") #Menu Function
    print("edit\t- Edit a stock value in your portfolio") #Menu Function
    print("add\t- Add another stock to your portfolio") #Menu Function
    print("remove\t- Remove an investment from your portfolio") #Menu Function
    print("clear\t- Delete entire investment portfolio") #Menu Function
    print("exit\t- Exit program") #Menu Function
    print() #Formatting

def read_investements():
    """
    Puts CSV file in a list
    """
    stocks = [] #Defines empty list
    #Appends each row in csv file to list
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file) #Opens a reader function
        for row in reader: #Reads everything in csv file
            stocks.append(row) #Appends each row to stocks list
    return stocks #Returns list

def view_stock_investments(stocks):
    """Prints every investment and value from list
    """
    for row in stocks: #Loops through every item in list
        print(f"{row[0]} - {row[1]}") #Formats each item in the list
    print() #Formatting

def view_total_investments(stocks):
    """Finds total value of portfolio, and average investment value
    """
    total = 0 #Variable for calculations
    for row in stocks: #Loops through every item in list
        amount = float(row[1]) #Grabs the value from each item
        total += amount #Adds the value to the total

    count = len(stocks) #Gets length of stocks list
    
    #Calculate average
    if count != 0: #Error checking to see if we can perform average operation
        average = total / count #If valid, finds average
        average = round(average, 2) #Rounds the average 
    else: #If not valid, run code inside
        average = 0 #Set average to zero if there is no length in list

    #Format and display the result
    print("Total Portfolio Worth:    ", total) #Total Portfolio Worth
    print("Average Stock Worth:\t ", average) #Average worth of each stock       
    print() #Formatting

def add(stocks):
    """
    Adds a stock and indvestment value according to user input
    """
    stock = str(input("Please enter in a stock company: ")).upper() #User input for company formatted to be uppercase
    while True: #Infinite loop to ensure user input is valid
        try: #Error checking
            amount = float(input("How much is your investment worth in " + stock + ": ")) #If valid, sets variable to user input
            break #Breaks from infinite loop if valid
        except: #If user input is invalid, run code inside
            print("Please enter an integer or decimal point value.") #Error message
            continue #Repeates loop
    investment = [stock, amount] #Sets variable to add to stocks list
    stocks.append(investment) #Adds user input to stocks list
    with open(FILENAME, "w", newline="") as file: #Opens CSV file for editing
        writer = csv.writer(file) #Initializes writer
        writer.writerows(stocks) #Writes the updated stocks list to CSV file
    print(f"Investment value for {investment[0]} was added.") #Confirmation message
    print() #Formatting
    
def remove(stocks):
    """
    Removes a single investment from portfolio according to user
    """
    names = [] #Empty list to add investment names to
    for item in stocks: #Loops through every item in list
        names.append(str(item[0])) #Appends the company name to names list
    name = input("Please Input Company: ") #Gets user input to determine where to edit
    name = name.upper() #Makes input not case sensitive
    if name in names: #Checks to see if input is in the company list from portfolio
        index = names.index(name) #Get the index of the input if valid
        stocks.pop(index) #Destroy the investment
        write_stocks(stocks) #Calls write_stocks function to update CSV file
        print(f"Investment in {name} has been deleted.") #Confirmation message 
        print() #Formatting
    else: #If user input not valid, run code inside
        print("Not a valid entry. Please enter in a stock from your portfolio.") #Error message
        print() #Formatting

def edit(stocks):
    """
    User can edit the stocks list
    """ 
    names = [] #Empty list to add stock names to
    for item in stocks: #Loops through every item in list
        names.append(str(item[0])) #Adds stock names to names list
    name = input("Please Input Company: ") #Gets user input to determine where to edit
    name = name.upper() #Makes input not case sensitive
    if name in names: #Validates user input
        index = names.index(name) #Variable for replacing
        amount = float(input("Investment Amount: ")) #Variable for replacing
        investment = [] #Empty list to help replace
        investment.append(name) #Append company name to temporary list
        investment.append(str(amount)) #Append value to temporary list
        stocks[index] = investment #Sets stocks list equal to the investment list to replace
        write_stocks(stocks) #Calls function to replace the indexed list
        print(f"Investment value for {investment[0]} was modified.") #Confirmation message
        print() #Formatting
    else: #If user input not valid, run code inside
        print("Company not found in your portfolio.") #Error message
        print() #Formatting

def write_stocks(stocks):
    """
    Edits the stocks list as according to the user input
    """
    with open(FILENAME, "w", newline="") as file: #Opens CSV file
        writer = csv.writer(file) #Initializes writer
        writer.writerows(stocks) #Updates CSV file according to the stocks list

def open_investments():
    """
    Creates investments CSV file if it doesn't exits, and has a user start a portfolio
    """
    stocks = [] #Initializes list variable
    
    stock = str(input("Please enter in a starting stock company: ")).upper() #User inputs a company name is converted to uppercase
    while True: #Infinite loop to ensure user enters proper value
        try: #Error checking
            amount = float(input("How much is your investment worth in " + stock + ": ")) #If valid float input, saves it to variable
            print() #Formatting
            break #If valid input, breaks from infinite loop
        except: #If not valid input, run code inside
            print("Please enter an integer or decimal point value.") #Error message
            continue #Returns to top of infinite loop
    investment = [stock, amount] #Initializes temporary list to append to stocks lists
    stocks.append(investment) #Appends user inputs to stocks list
    with open(FILENAME, "w", newline="") as file: #Creates and opens CSV file
        writer = csv.writer(file) #Initializes writer
        writer.writerows(stocks) #Updates CSV file to match stocks list

def clear(stocks):
    """
    Completely clears the users portofolio, and the CSV file
    """
    choice = input("Are you sure you want to clear your portfolio?\nThis will delete every entry and value.\nPlease enter y to confirm or n to cancel: ") #Asks for user confirmation before deletion
    if choice == "y": #If user confirms, run code inside
        stocks = [] #Empties stocks list
        with open(FILENAME, "w+", newline="") as file: #Opens CSV file
            writer = csv.writer(file) #Initializes writer
            writer.writerows(stocks) #Updates CSV file to match empty stocks list
        print("Investment portfolio has succesfully been cleared.") #Confirmation message
        print() #Formatting
    else: #If user does not confirm, run code inside
        print("Investment Portfolio has NOT been cleared.") #Confirmation message
        print() #Formatting
        return False #Returns False value to know whether to end program or not

def main():
    """
    Calls all other function to run the programm
    """
    display_title() #Calls funciton
    try: #Error checking to see if CSV file exists
        stocks = read_investements() #Sets variable equal to called function if CSV file exists
    except: #If CSV file does not exit, run code inside
        open_investments() #Calls function
        stocks = read_investements() #Sets variable equal to called function now that CSV file does exist
    display_menu() #Calls funciton
    while True: #Creates a constant input menu loop until user enters exit
        command = input("Command: ") #Sets variable to be user input
        if command == "view": #Checks to see if user input equals view
            view_stock_investments(stocks) #Calls function
        elif command == "total": #Checks to see if user input equals total
            view_total_investments(stocks) #Calls function
        elif command == "edit": #Checks to see if user input equals edit
            edit(stocks) #Calls function
        elif command == "add": #Checks to see if user input equals add
            add(stocks) #Calls function
        elif command == "remove": #Checks to see if user input equals remove
            remove(stocks) #Calls function
        elif command == "clear": #Checks to see if user input equals clear
            cleared = clear(stocks) #Sets variable equal to called function
            if cleared == False: #If the called function returns false, run code inside
                continue #Returns to the top of infinite loop
            else: #If called function does not return false, run code inside
                break #Exits from infinite loop
        elif command == "exit": #Checks to see if user input equals exit
            break #Exits from infinite loop
        else: #If user input is not valid, run code inside
            print("Not a valid command. Please try again.\n") #Error message

    print("Bye!") #Exit message

if __name__ == "__main__": #Runs main function if this file is ran
    main() #Function call
