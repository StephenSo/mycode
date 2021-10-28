#!/usr/bin/env python3
import os,json
from random import randint

# Get current folder
WorkDir = os.getcwd()

# open the file for reading
with open(f"{WorkDir}/LOB.json","r") as LOB:
    LOB = json.load(LOB)

no_of_quotes = len(LOB["Quotes"])
RandomQuote = randint(0,no_of_quotes)
print("\n\nRandom Life of Brian quote of the day!\n")
print(LOB["Quotes"][RandomQuote])
print()

