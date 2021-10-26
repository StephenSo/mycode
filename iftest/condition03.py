#!/usr/bin/env python3

# Get hostname from user
hostname = input("What value should we set for hostname?")

## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config") # confirm if hostname matches.

# Always display this exit message
print ("Exiting the script.")
