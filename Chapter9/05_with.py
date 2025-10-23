# f = open("file.txt")

# print(f.read())

# f.close()

# Same can be done by using with statement -> 

with open("file.txt") as f:
    print(f.read())

# No need to close the file