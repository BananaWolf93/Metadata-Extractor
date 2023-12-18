#!/usr/bin/env python3

import os
from tika import parser

user_input = input("Please enter the absolute path for the file you'd like to analyze: ")
file_path = user_input
parsed = parser.from_file(file_path)

metadata = parsed.get("metadata", {})
for key, value in metadata.items():
    print (f"{key}: {value}")



