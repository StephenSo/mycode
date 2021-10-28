#!/usr/bin/env python3
from random import randint

def main():
    start = 1
    end = 100
    guess_this_number = randint(start,end)
    user_input = end + 1
    while (user_input != guess_this_number):
        user_input = int(input(f"Please enter number between {start} and {end}:"))
        if user_input > guess_this_number:
            print("Too high")
        elif user_input < guess_this_number:
            print("Too low")

    print(f"You did it! The number is: {guess_this_number}")

main()