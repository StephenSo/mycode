#!/usr/bin/env python3
import os,json
from random import choice

# Get current folder
WorkDir = os.getcwd()

# open the file for reading
with open(f"{WorkDir}/LOB.json","r") as LOB:
    LOB = json.load(LOB)

print("\n\nRandom Life of Brian quote of the day!\n")

print(choice(LOB["Quotes"]))
print()

