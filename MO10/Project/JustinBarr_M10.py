#Name: Justin Barr
#Class: INFO 1200
#Section: 001
#Professor: Crandall
#Date: 4/7/2023
#Project #: M10
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import csv #Imports CSV module

FILENAME = "D:/GitRepos/INFO1200Spring2023/MO10/Project/monthly_sales.csv" #File name for csv file

def display_title():
    """Displays title for program
    """
    print("Justin Barr's Monthly Sales")
    print()

def display_menu():
    """Displays menu for program
    """
    print("COMMAND MENU")
    print()
    print("monthly\t- View monthly sales")
    print("yearly\t- View yearly summary")
    print("edit\t- Edit sales for a month")
    print("exit\t- Exit program")
    print()

def read_sales():
    """
    Puts CSV file in a list
    """
    sales = [] #Defines empty list
    #Appends each row in csv file to list
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            sales.append(row)
    return sales #Returns list

def view_monthly_sales(sales):
    """Prints every monthly sale from list
    """
    for row in sales:
        print(f"{row[0]} - {row[1]}")
    print()

def view_yearly_summary(sales):
    """Finds yearly total for sales and monthly average
    """
    total = 0 #Variable for calculations
    #Finds total sales
    for row in sales:
        amount = int(row[1])
        total += amount

    # get count
    count = len(sales)
    
    # calculate average
    average = total / count
    average = round(average, 2)

    # format and display the result
    print("Yearly total:    ", total)
    print("Monthly average: ", average)        
    print()

def edit(sales):
    """User can edit the sales list
    """
    names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] #List with abreviated month names
    name = input("Please Input Month: ") #Gets user input to determine where to edit
    name = name.title() #Makes input not case sensitive
    #Validates user input and replaces it
    if name in names:
        index = names.index(name) #Variable for replacing
        amount = int(input("Sales Amount: ")) #Variable for replacing
        month = [] #Empty list to help replace
        #Appending variables to list
        month.append(name)
        month.append(str(amount))
        sales[index] = month #Sets sales list equal to the month list to replace
        write_sales(sales) #Calls function to replace the indexed list
        print(f"Sales amount for {month[0]} was modified.")
        print()
    else:
        print("Invalid three-letter month.")

def write_sales(sales):
    """Edits the sales list as according to the user input
    """
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sales)

def main():
    display_title() #Calls funciton
    display_menu() #Calls funciton
    sales = read_sales() #Sets variable equal to called function

    print(sales)
    #Creates a constant input menu loop until user enters exit
    while True:
        command = input("Command: ")
        if command == "monthly":
            view_monthly_sales(sales)
        elif command == "yearly":
            view_yearly_summary(sales)
        elif command == "edit":
            edit(sales)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!") #Exit message

if __name__ == "__main__":
    main()