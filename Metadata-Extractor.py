#!/usr/bin/env python3

# The following libraries are first imported:

import os
from tika import parser

# The following variables are needed for the identification of the user's input and then checking for path validation and a value to send to parse the file:

user_input = input("Please enter the absolute path for the file you'd like to analyze: ")
file_path = user_input
parsed = parser.from_file(file_path)

# The following function grabs the user's input and determines if it is valid or not. If valid, the user will be notified then the script will complete by extracting all metadata found.
# Otherwise, if invalid, the user will also be notified and advised to recheck the absolute path of the targeted file.

def data_extraction():
    if os.path.exists(file_path):
        print("Path verified! Returning results... ")
        metadata = parsed.get("metadata", {})
        for key, value in metadata.items():
            print (f"{key}: {value}")
    else:
        print("Path NOT valid, please check the absolute path for the target and try again.")
    return file_path