#!/usr/bin/env python3
from random import randint

def main():

    icecream= ["flavors", "salty"]
    northerntrust= ["Bala", "Inderjeet", "Jon", "Nikita", "Steve", "Vinod"]
    icecream.append(99)
    start = 0
    end = northerntrust.__len__() - 1
    user_input = input(f"Please enter number between {start} and {end}:")
    try:
        if int(user_input):
            name = northerntrust[int(user_input)]
    except ValueError:
        if not user_input:
            name = northerntrust[randint(start,end)]
        else:
            for name in northerntrust:
                if user_input == name:
                    break
      

    print(f"Name found = {name}")

    print(f"{icecream[2]} {icecream[0]}, and {name} chooses to be {icecream[1]}.")


main()