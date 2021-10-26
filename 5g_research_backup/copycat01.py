#!/usr/bin/env python3

import shutil
import os

def main():
    # Get current folder
    WorkDir = os.getcwd()

    # Set current working directory
    os.chdir(WorkDir)

    # Copy file sdn_network.txt file to sdn_network.txt.copy
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy2")

    # Clone the folder tree to a new location
    shutil.copytree("5g_research/", "5g_research_backup/",dirs_exist_ok=True)

if __name__ == "__main__":
    main()