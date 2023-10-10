#Justin Barr validation file for the Future Value App

def get_float(prompt, low, high):
    """Validates a users float input

    Args:
        prompt (str): Prompt for user to input
        low (float): Lowest value
        high (float): highest value

    Returns:
        float: The user input
    """
    #Infinite loop
    while True:
        #Gets user input
        number = float(input(prompt))

        #Validates user input or display error message
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low, "and less than or equal to", high)

def get_int(prompt, low, high):
    """Validates user integer input

    Args:
        prompt (str): Prompt for user input
        low (int): Lowest valid input
        high (int): Highest valid input

    Returns:
        int: The validated user input
    """

    #Infinite loop
    while True:
        #Get user input
        number = int(input(prompt))

        #Validate user input or display error message
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low, "and less than or equal to", high)
            
def main():
    #Set variable for while loop
    choice = "y"

    #Loop to repeat until user is finished
    while choice.lower() == "y":

        #Get user input, validate, and print that input
        valid_number = get_float("Enter number: ", 0, 1000)
        print("Valid number = ", valid_number)
        print()

        #Get user input, validate, and print that input
        valid_integer = get_int("Enter integer: ", 0, 50)
        print("Valid integer: ", valid_integer)
        print()

        #Check to see if user is finished
        choice = input("Repeat? (y/n): ")

    #Exit message
    print("Bye!")

#Calls main function
if __name__ == "__main__":
    main()