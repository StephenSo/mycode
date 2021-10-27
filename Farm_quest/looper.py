#!/usr/bin/env python3

def main():
    farms = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
            {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
            {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
            {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

    animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"] # could go inside get_agriculture()
                                                                      # what does B.P say?

    def get_agriculture(farm): # farm is a farm object ('name',[agriculture])
        print(f"\nIn the {farm['name']} the animals to be found are:")
        found_animal = False  # we have not got a match yet
        for item in farm['agriculture']: # loop through the agri' list in farm as 'item'
            if item in animals: # is the item in the animals list?
                found_animal = True # we have found an animal
                print(f" - {item}") # print the item
        
        if not found_animal: # no animals found in this farm
            print("There are no animals in this farm")

    def get_farm(farms):
        user_selection = 0 # set up invalid value for user_selection
        while user_selection < 1 or user_selection > len(farms): # ensure the valid values match the number of books
            
            for count,value in enumerate(farms): # Display the list of known farms
                print(f"{count+1}: {value['name']}") # print the list of farms with a counter.
            try:
                user_selection = int(input(f"Select a farm number in the range 1-{count+1}:"))
            except ValueError: # If user entered something other than a number
                print("Please enter a valid number")
                user_selection = 0 
        
        return farms[user_selection-1]

    get_agriculture(get_farm(farms)) # get user to select a farm from the farms list
                                     # get the argi' in the selected farm

main()
