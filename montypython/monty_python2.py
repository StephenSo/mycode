#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

round = 0
answer = " "
holy_grail = {"brian":"not the messiah","shrubbery":"we need a special plant"}

while round < 3 and answer not in holy_grail:
    round += 1     # increase the round counter by 1
    answer = (input('Finish the movie title, "Monty Python\'s The Life of ______": ')).lower()

    if answer == "brian": # logic to check if user gave correct answer
        print("Correct!")
    elif answer == "shrubbery":
        print("You gave the super secret answer!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    elif answer == "help":
        print("A clue could be one of these: ",end="\n")
        for count,value in enumerate(holy_grail):
            print(holy_grail[value])
    else:                 # if answer was wrong
        print("Sorry. Try again!")
