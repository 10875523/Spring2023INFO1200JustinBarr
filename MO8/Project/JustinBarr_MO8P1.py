#!/usr/bin/env python3
#Name: Justin Barr
#Class: INFO 1200
#Section: 001
#Professor: Crandall
#Date: 3/25/2023
#Project #: MO8_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#Import modules
import tkinter as tk
from tkinter import ttk, messagebox 
import math

class HypotenuseFinderFrames(ttk.Frame):
    def __init__(self, parent):
        #Set up the window for program
        ttk.Frame.__init__(self, parent)
    
        #Add the HypotenuseFinderFrames
        HypotenuseFinderFrame(parent).grid(row=0, column=0)

        #Add the Exit button
        ttk.Button(parent, text="Exit", command=parent.destroy).grid(row=1, column=1, sticky=tk.E, padx=15, pady=10)

class HypotenuseFinderFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10") #Padding in the frame
        
        #Define variables
        self.parent = parent
        self.message = ""        

        # Define string variables for text entry fields
        self.firstSide = tk.StringVar()
        self.secondSide = tk.StringVar()
        self.hypotenuse = tk.StringVar()

        self.initComponents() 

    def initComponents(self):
        #Initializes and organizes components
        self.pack()

        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Side A Length:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.firstSide).grid(
            column=1, row=0)

        ttk.Label(self, text="Side B Length:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.secondSide).grid(
            column=1, row=1)

        ttk.Label(self, text="Hypotenuse Length:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.hypotenuse,
                  state="readonly").grid(
            column=1, row=3)

        self.makeButtons() #Creates the buttons

        #Padding
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def clear(self):
        #Resets the entry fields
        self.firstSide.set("")
        self.secondSide.set("")
        self.hypotenuse.set("")

    def makeButtons(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Clear", command=self.clear) \
            .grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate) \
            .grid(column=1, row=0)

    def get_int(self, val, fieldName):
        #Returns the int of entry field or adds to an error message
        try:
            return int(val)
        except ValueError:
            self.message += f"{fieldName} must be a valid whole number.\n"
    
    def get_float(self, val, fieldName):
        #Returns the float of entry field or adds to an error message
        try:
            return float(val)
        except ValueError:
            self.message += f"{fieldName} must be a valid number.\n"

    def calculate(self):
        self.message = "" # clear any previous error message

        #Sets variables used for hypotenuse calculations
        sideA = self.get_int(self.firstSide.get(), "First Side")
        sideB = self.get_int(self.secondSide.get(), "Second Side")
                
        if self.message == "": # no errors
            #Calculates Hypotenuse length and displays in the text box
            hypotenuseLength = self.get_float(round(math.sqrt((sideA * sideA) + (sideB * sideB)), 3), "Hypotenuse Length")
            self.hypotenuse.set(hypotenuseLength)
        else:
            #Displays error message if it exists
            messagebox.showerror("Error", self.message)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hypotenuse Calculator")
    HypotenuseFinderFrames(root)
    root.mainloop()
