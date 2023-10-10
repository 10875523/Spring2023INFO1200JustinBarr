#!/usr/bin/env python3

import csv #Import csv module

FILE_NAME = "D:/GitRepos/INFO1200Spring2023/MO10/Participation/trips.csv" #File name for csv file

def write_trips(trips):
    """Write trips to the csv file
    """
    with open(FILE_NAME, "w", newline="") as output_file: #opens csv file in write mode
        writer = csv.writer(output_file) #Creates a writer object
        writer.writerows(trips) #Writes trips argument to file

def read_trips():
    """Read from the csv file
    """
    trips = [] #Create empty list
    with open(FILE_NAME, "r", newline="") as input_file: #Opens file in read mode
        reader = csv.reader(input_file) #Create reader object
        #Iterate through file and add to list
        for row in reader:
            trips.append(row)
    return trips #returns list

def list_trips(trips):
    """Read trips and display them
    """
    print("Distance\tGallons\t\tMPG") #Prints Header
    #Iterates through the list and prints individual trips
    for i in range(0, len(trips)):
        trip = trips[i]
        print(f"{trip[0]}\t\t{trip[1]}\t\t{trip[2]}")
    print() #Print blanck line

def get_miles_driven():
    """ Receives user input for miles driven
    """
    #Checks validity of user input
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven #Returns user input if valid
          
def get_gallons_used():
    """Receives user input for gallons used
    """
    #Validates entry
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used #Returns entry if valid

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = read_trips() #2D list
    list_trips(trips) #List out the trips

    more = "y" #Sets variable to check if user wants to continue
    while more.lower() == "y": #Will repeat until user indicates they quit
        #Sets temporary variables to use for calculations
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2) #Calculates mpg
        print(f"Miles Per Gallon:\t{mpg}") #Formats and prints MPG
        print()
        
        single_trip = [miles_driven, gallons_used, mpg] #Create a single trip list
        trips.append(single_trip) #Add the single tirp to the trips 2D list
        write_trips(trips) #Write the trips to the CSV file

        list_trips(trips) #List out the trips

        more = input("More entries? (y or n): ") #Asks if the user wants to continue
    
    print("Bye!") #Exit message

#Calls file when ran
if __name__ == "__main__":
    main()

