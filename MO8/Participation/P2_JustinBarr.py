#!/usr/bin/env python3
#Name: Justin Barr
#Class: INFO 1200
#Section: 001
#Professor: Crandall
#Date: 3/23/2023
#Project #: MO8_Participation
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#Import modules
import tkinter as tk
from tkinter import ttk, messagebox 

class FutureValueFrame(ttk.Frame):
    def __init__(self, parent):
        #Set up the window for program
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent       

        # Define string variables for text entry fields
        self.firstName = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        #Initializes and organizes the components
        self.pack()

        # Display label and entry field
        ttk.Label(self, text="First Name").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.firstName).grid(
            column=1, row=0)

        self.makeButtons() #Calls the makeButtons function

        #Configure padding in pixels
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def hello(self):
        #Set a message to show when called
        tk.messagebox.showinfo("Hello", "Hello " + self.firstName.get())
        

    def makeButtons(self):
        # Create a frame to store the buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Exit", command=self.parent.destroy) \
            .grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Hello", command=self.hello) \
            .grid(column=1, row=0)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hello Name")
    FutureValueFrame(root)
    root.mainloop()
