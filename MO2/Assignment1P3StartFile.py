#Name: (Justin Barr)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 2/2/2023
#Project #: 1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

firstName = 'Justin' #Creates first name variable
print('Hello, my name is ' + firstName) #Prints introduction message

school = 'Utah Valley University' #Sets school variable
print('I go to ' + school) #Prints what school I go to

#Creates a variable for credits, classes, and total credits
credits = 3
classes = 6
totalCredits = credits * classes

#Prints how many credits I am taking, and that I would like to save money
print('If I take 6 classes this semester and all are three credits each I will be taking ' + str(totalCredits) + ' credits')
print('I would like to save money by taking this many credits.')

#Sets a variable for Maximum paid credits, how much 3 credits cost, and what a class fee is
maxCredits = 12
costPerClass = 350
classFee = 20

freeClassValuePerSemester = (((totalCredits - maxCredits) / credits) * costPerClass) + 20 * ((totalCredits - maxCredits) / credits) #Sets variable for the value of taking more than 12 credits

print('If classes are free after the ' + str(maxCredits) + ' credits and each class cost $' + str(costPerClass) + ' (plus an additional $' + str(classFee) + ' per class fee), I will be saving $' + str(freeClassValuePerSemester) + ' a semester.') #Wordily states how much I would save per semester

freeClassValuePerYear = freeClassValuePerSemester * 3 #Sets a variable for the value of taking more than 12 credits for 3 semester per year

print('That is a wopping $' + str(freeClassValuePerYear) + ' a year!') #Prints how much I would save per year

print('This was a very informative and worth while Python assignment!') #Prints exit message
