#!/usr/bin/env python3
#Name: Justin Barr
#Class: INFO 1200
#Section: 001
#Professor: Crandall
#Date: 3/25/2023
#Project #: MO8_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#Import modules
import tkinter as tk
from tkinter import ttk, messagebox 

class TestScoreFrames(ttk.Frame):
    def __init__(self, parent):
        #Set up the window for program
        ttk.Frame.__init__(self, parent)
    
        #Add the TestScoreFrames
        TestScoreFrame(parent).grid(row=0, column=0)

        #Add the Exit button
        ttk.Button(parent, text="Exit", command=parent.destroy).grid(row=1, column=1, sticky=tk.E, padx=15, pady=10)

class TestScoreFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10") #Padding in the frame
        
        #Define variables
        self.parent = parent
        self.message = ""        

        # Define string variables for text entry fields
        self.firstScore = tk.StringVar()
        self.secondScore = tk.StringVar()
        self.results = tk.StringVar()

        self.initComponents() 

    def initComponents(self):
        #Initializes and organizes components
        self.pack()

        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Test Score 1:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.firstScore).grid(
            column=1, row=0)

        ttk.Label(self, text="Test Score 2:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.secondScore).grid(
            column=1, row=1)

        ttk.Label(self, text="Results:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.results,
                  state="readonly").grid(
            column=1, row=3)

        self.makeButtons() #Creates the buttons

        #Padding
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def clear(self):
        #Resets the entry fields
        self.firstScore.set("")
        self.secondScore.set("")
        self.results.set("")

    def makeButtons(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Clear", command=self.clear) \
            .grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Average", command=self.calculate) \
            .grid(column=1, row=0)
    
    def get_float(self, val, fieldName):
        #Returns the float of entry field or adds to an error message
        try:
            return float(val)
        except ValueError:
            self.message += f"{fieldName} must be a valid number.\n"

    def calculate(self):
        self.message = "" # clear any previous error message

        #Sets variables used for results calculations
        scoreA = self.get_float(self.firstScore.get(), "First Test Score")
        scoreB = self.get_float(self.secondScore.get(), "Second Test Score")
                
        if self.message == "": # no errors
            #Calculates result and displays in the text box
            result = self.get_float(round((scoreA + scoreB) / 2 , 2), "Results")
            self.results.set(result)
        else:
            #Displays error message if it exists
            messagebox.showerror("Error", self.message)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test Score Calculator")
    TestScoreFrames(root)
    root.mainloop()
