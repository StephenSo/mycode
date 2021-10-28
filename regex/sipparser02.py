#!/usr/bin/python3

# Python standard library
import re,requests,os 

WorkDir = f"{os.getcwd()}\\regex\\"
file_name = "networktrace.txt"
webdata = "https://static.alta3.com/files/networktrace.txt"

def save_webdata(url,path):
    resp = requests.get(url) # GET data from given URL
    with open(path, "w") as text:
        text.write(resp.text) # Save the data to the given PATH 
    return resp

def main():
    full_path = f"{WorkDir}{file_name}" # Create full path (folders\filename)
    #Grab the text from a URL and save to local disk
    save_webdata(webdata,full_path) 

    # open the networktrace (text format)
    with open(full_path) as trace:
        # loop across the text file
        for line in trace:
            # look for a line that begins with sip:+ followed by digits@IP:port
            conobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', line)
            if conobj:
                print(conobj.group())
                print("The phone number is...")
                print(conobj.group(1))
                print("The IPv6 is...")
                print(conobj.group(2))
                print("The port is...")
                print(conobj.group(3))
if __name__ == "__main__":
    main()
