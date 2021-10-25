#!/usr/bin/env python3

# create a list containing three items
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# display the first item in the list
print(f"The first item in the list (IP): {iplist[0]}" )

# display the second item in the list
print(f"The second item in the list (port): {iplist[1]}" )

# display the third item in the list
print(f"The last item in the list (state): {iplist[-1]}" )

# Display the IP addesses only
print(f"The IPs are: {iplist[3]} & {iplist[3]}")