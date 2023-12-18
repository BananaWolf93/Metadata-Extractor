#!/usr/bin/env python3

# Needed libraries:

import os
from tika import parser

# Defining a function to grab the user's input, determine the value as the file path and passing it along to parse after it has been verified and confirmed as "valid".

def data_extraction():
    user_input = input("Please enter the absolute path for the file you'd like to analyze: ")
    file_path = user_input

    if os.path.exists(file_path):
        try:
            parsed = parser.from_file(file_path)
            print("Path verified! Attempting to extract metadata...")
            
            metadata = parsed.get("metadata", {})
            if metadata:
                for key, value in metadata.items():
                    print(f"{key}: {value}")
            else:
                print("No metadata found in the file.")
                
        except Exception as e:
            print(f"An error occurred during parsing: {e}")
            
    else:
        print("Path NOT valid, please check the absolute path for the target and try again.")

data_extraction()
