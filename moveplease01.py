#!/usr/bin/env python3

import shutil
import os

def main():
    # Get current script folder
    WorkDir = os.getcwd()

    # Set current working directory to script folder
    os.chdir(WorkDir)

    # Move file to a new SUB folder 
    shutil.move('raynor.obj', 'ceph_storage/')

    # Ask user for the new file name
    xname = input('What is the new name for kerrigan.obj? ')

    # Rename the file using input from user
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()