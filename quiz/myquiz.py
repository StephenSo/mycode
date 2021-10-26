#!/usr/bin/env python3
import os

#A program that prompts the user for a value (1 through n), then returns a quick synopsis of a book or movie in that series.
#Harry Potter
#Hobbit & Lord of the Rings
#Chronicles of Narnia
#Indiana Jones

def main():
    print("Synopses of the following books are available.")

    # Get current script folder
    WorkDir = os.getcwd()

    # Set current working directory to script folder
    os.chdir(f"{WorkDir}/quiz")

    # Create initial dictionary of books. The paired value must be a file name 
    # containing a synopsis of the book(s).
    books = {
        "Harry Potter":"HarryPotter.txt",
        "Hobbit & Lord of the Rings":"Hobbit.txt",
        "Chronicles of Narnia":"Narnia.txt",
        "Indiana Jones":"Indiana.txt"
        }
    # Now using the value pair, read the appropriate text file containing the synopsis        
    for count,value in enumerate(books):
        books[value] =  (open((books[value]), "r")).read() # over write the paired values
                                                           # with the synopsis read from a file.

    user_selection = 0 # set up invalid value for user_selection
    while user_selection < 1 or user_selection > count+1: # ensure the valid values match the number of books
        
        for count,value in enumerate(books): # Display the list of know books
            print(f"{count+1}: {value}") # print the list of books with a counter.
        try:
            user_selection = int(input(f"Select a movie number in the range 1-{count+1}:"))
        except ValueError: # If user entered something other than a number
            print("Please enter a valid number")
            user_selection = 0 
    
    print("\n\nHere is your synopsis:\n")
    
    for count,value in enumerate(books):
        if count+1 == user_selection:
            print(f"{value}\n") #  print the book name
            print(f"{books[value]}") # print the synopsis
            break
        
main()