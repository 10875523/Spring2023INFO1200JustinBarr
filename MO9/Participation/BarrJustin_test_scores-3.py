#!/usr/bin/env python3

#Welcome message
def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = [] #Create empty list to fill
    #Adds inputed scores to list until input equals x
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score) 
            else:
                #Checks for validity of inputs
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    # calculate average score
    count = len(scores)
    score_total = sum(scores)
    average = score_total / count
    #Finds min and max of list
    low_score = min(scores)
    high_score = max(scores)

    scores.sort() #Sorts list smallest to largest

    median = 0 #Set variable for median
    mid_index = count // 2 #Check for how to calculate median from list

    if count % 2 == 1:
        #If list has odd number of scores, picks the middle one to be median
        median = scores[mid_index]
    else:
        #If list is even, calculates median based on the middle two
        score1 = scores[mid_index]
        score2 = scores[mid_index - 1]
        median = (score1 + score2) / 2
                
    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", count)
    print("Average Score:     ", average)
    print("Low Score:         ", low_score)
    print("High Score:        ", high_score)
    print("Median Score:      ", median)

def main():
    display_welcome() #Calls function
    scores = get_scores() #Sets variable to list from function
    process_scores(scores) #Calls function passing in list
    #Exit message
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


