#!/usr/bin/python3

import time,os,requests, reverse_geocoder as rg

# URL Of API locating ISS
URL= "http://api.open-notify.org/iss-now.json"

# Get current folder
WorkDir = f"{os.getcwd()}\\mtg\\"

def main():
    # Send GET REST request to ISS API
    resp= requests.get(URL).json()

    lat = resp["iss_position"]["latitude"]
    lon = resp["iss_position"]["longitude"]
    timestamp = resp["timestamp"]

    # convert epoch time to current date/time
    timestamp = time.ctime(timestamp)

    # Convert lat,lon to a named location
    locator_resp= rg.search((lat, lon))
    city= locator_resp[0]["name"]
    admin= locator_resp[0]['admin1']

    print(f"""
CURRENT LOCATION OF THE ISS:
Timestamp: {timestamp}
Lon: {lon}
Lat: {lat}
City: {city},{admin}
""")

if __name__=="__main__":
    main()
