#!/usr/bin/env python3
"""RZFeeser@alta3.com | Alta3 Research
   Using the CSV library to work with CSV data."""

# standard library import
import csv, os

WorkDir = os.getcwd()

# open our csv data (we want to loop across this)
with open(f"{WorkDir}/credmaker/csv_users.txt", "r") as csvfile:
    # counter to create unique file names
    i = 0
    # loop across our open file line by line
    for row in csv.DictReader(csvfile):
        i = i + 1 # increase i by 1 (to create unique admin.rc file names)
        filename = f"{WorkDir}/credmaker/admin.rc{i}" # this f string says "fill in the value of i"

        # open a file via "with". This file will autoclose when the indentations stop
        with open(filename, "w") as rcfile:
            # use the standard library print function to print our data
            # out to the open file open rcfile (open in write mode)
            # Headers
            # authurl,projectname,domainname,username,userdomainname,password
            print("export OS_AUTH_URL=" + row['authurl'], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + row['projectname'], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row['domainname'], file=rcfile)
            print("export OS_USERNAME=" + row['username'], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + row['userdomainname'], file=rcfile)
            print("export OS_PASSWORD=" + row['password'], file=rcfile)

# all of the indentation ends, so all files are auto closed

# display this to the screen when all of the looping is over
print("admin.rc files created!")
