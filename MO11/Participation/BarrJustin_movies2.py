#!/usr/bin/env python3

#Imports modules
import csv
import sys

FILENAME = "movies.csv" #Global constant for file name

def exit_program():
    """
    Exits the program
    """
    #Exit message
    print("Terminating program.")
    sys.exit()

def read_movies():
    """
    Interact with CSV file
    """
    #Try to open file and read it
    try:
        movies = [] #Creates list for movies
        #Opens file and adds contents to movies list
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies #Return movies list
    #Exception for file not found
    except FileNotFoundError as e:
        #print(f"Could not find {FILENAME} file.")
        #exit_program()
        return movies
    #Exception for all other movies
    except Exception as e:
        #Prints exception type and exits
        print(type(e), e)
        exit_program()

def write_movies(movies):
    """
    Open file and write to it
    """
    #Try to open file and write to it
    try:
        #Open file and write movies list
        with open(FILENAME, "w", newline="") as file:
            ##raise BlockingIOError("Test the OSError exception.")
            writer = csv.writer(file)
            writer.writerows(movies)
    #Catches OSErrors
    except OSError as e:
        #Prints exception type and exits
        print(type(e), e)
        exit_program()
    #Catches all exceptions
    except Exception as e:
        #Prints exception type and exits
        print(type(e), e)
        exit_program()

def list_movies(movies):
    """
    Iterates through movies and prints
    """
    #Iterates through list and prints
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()
    
def add_movie(movies):
    """
    Adds a new movie to the file
    """
    #Get movie details
    name = input("Name: ")
    while True:
        #Validation for year input
        try:
            year = int(input("Year: "))
        except ValueError:
            #Error message if invalid input
            print("Invalid year. Please try again.")
            continue
        #Validation for non-negative year
        if year <= 0:
            print("Year must be greater than zero. Please try again.")
            continue
        else:
            break
        
    #Add movie to details to movies list 
    movie = [name, year]
    movies.append(movie)
    #Write movies to file and print success message
    write_movies(movies)
    print(f"{name} was added.\n")

def delete_movie(movies):
    """
    Remove a movie from the file
    """
    while True:
        #Validates user input
        try:
            number = int(input("Number: "))
        #Catches ValueError exceptions
        except ValueError:
            #Prints error message
            print("Invalid integer. Please try again.")
            continue
        #Validates input to be within range
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        else:
            break
    #Remove the movie from movies list, update file, print confirmation
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(f"{movie[0]} was deleted.\n")

def display_menu():
    """
    Displays information about the program
    """
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    """
    Main function to call
    """
    display_menu() #Show menu
    movies = read_movies() #Read movies from file
    while True:        
        #Checks which command was input
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            #Error message for validation
            print("Not a valid command. Please try again.\n")
    print("Bye!") #Exit message

#Calls the main function
if __name__ == "__main__":
    main()
