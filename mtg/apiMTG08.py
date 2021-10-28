#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests,os
from random import randint

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform
# Get current folder
WorkDir = f"{os.getcwd()}\mtg\"

def main():
    """Run time code"""

    #setcode = input("What is the code of the set you are trying to lookup (see mtgsets.index for a list of codes)? ").lower()   # collect user input for MTG card set to lookup
    setcode = "C16"

    # create resp, which is our request object
    resp = requests.get(f"{API}cards?set={setcode}")   # this "f" string reads: API + "cards/" + setcode

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    cards = resp.json()
    no_of_cards = len(cards['cards'])
    PAC = randint(0,no_of_cards)
    card = cards['cards'][PAC]
    image = requests.get(card['imageUrl'])
    filename = f"{WorkDir}{card['name']}.png"

    with open(filename, "wb") as cardimage:
        cardimage.write(image.content)
    
    print(f"Your lucky dip is :{card['name']}, card image is in {filename} ")

if __name__ == "__main__":
    main()
