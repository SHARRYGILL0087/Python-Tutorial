# Write a Python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

# Specify the directory (you can change '.' to any path)
directory = '.'

# List all files and directories in the given path
contents = os.listdir(directory)

print("Contents of directory:", directory)
for item in contents:
    print(item)
