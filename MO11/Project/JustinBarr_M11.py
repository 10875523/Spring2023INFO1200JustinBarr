#Name: Justin Barr
#Class: INFO 1200
#Section: 001
#Professor: Crandall
#Date: 4/22
#Project #: M11
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import csv #Imports csv module

FILENAME = "contacts.csv" #Global variable

def display_title():
    """
    Displays a welcome message
    """
    print("Justin Barr's Contact Manager App")

def display_menu():
    """
    Displays a menu for program commands
    """
    print("COMMAND MENU")
    print()
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()

def read_contacts():
    """
    Reads contacts from csv file and puts them in a list
    """
    contacts = [] #Creates empty list for contacts
    try: #Error checking
        #Opens and reads file, then puts every row as an item in contacts list
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError: #Error checking
        #Error message if file not found, then creates proper file
        print("Could not find contacts file! Starting new contacts file...\n")
        with open(FILENAME, "w") as file:
            reader = csv.reader(file)
    return contacts #Returns the contacts list

def display(contacts):
    """
    Displays contacts
    """
    #Displays number of contacts with name, or an error message if non exist
    if len(contacts) == 0:
        print("There are no contacts in the list.")
        pass
    else:
        for i, row in enumerate(contacts, start=1):
            print(f"{i}. {row[0]}")
        print()

def view(contacts):
    """
    Displays specific contact from list
    """
    number = get_contact_number(contacts) #Calls the get_contact_number function to get the number of the contact
    #Displays the corresponding items for the person attached to the number
    if number > 0:
        contact = contacts[number-1]
        print("Name:", contact[0])
        print("Email:", contact[1])
        print("Phone:", contact[2])
        print()

def get_contact_number(contacts):
    """
    returns the contact number to reference in the list
    """
    while True:
        try: #Error checking
            number = int(input("Number: ")) #Sets number equal to user input
        except ValueError: #Error Checking
            print("Invalid integer. \n") #Error message
            return -1
        
        #Error checking
        if number < 1 or number > len(contacts):
            print("Invalid contact number.\n")
            return -1
        else:
            return number #Returns number if valid
        
def add(contacts):
    """
    Adds a contact to the list
    """

    #User inputs
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    contact = [] #Creates empty list to add to the contacts
    #Adds the users input
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact) #Adds the input to the contacts list
    write_contacts(contacts) #Updates the csv file
    print(f"{contact[0]} was added.")

def write_contacts(contacts):
    """
    Uses contacts list to update the csv file
    """
    #Opens csv file and updates it to agree with the contacts list
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def delete(contacts):
    """
    Deletes a contact from the list
    """
    number = get_contact_number(contacts) #Gets the contact order number
    if number > 0:
        contact = contacts.pop(number-1) #Deletes the proper contact according to the user
        print(f"{contact[0]} was deleted. \n")
    write_contacts(contacts) #Updates the csv file

def main():
    contacts = read_contacts() #Grabs the contacts list from the csv file
    display_title() #Displays title
    display_menu() #Displays menu
    while True:
        #Gets user input until user exits
        command = input("Command: ")
        if command == "list":
            display(contacts)
        elif command == "view":
            view(contacts)
        elif command == "add":
            add(contacts)
        elif command == "del":
            delete(contacts)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again. \n") #Error message
            
print("Bye!") #Exit message

#Calls file if it is the one running
if __name__ == "__main__":
    main()