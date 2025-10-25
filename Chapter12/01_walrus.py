# Without walrus operator:

line = input("Enter something: ")
while line != "quit":
    print(f"You entered: {line}")
    line = input("Enter something: ")


# With walrus operator:

while (line := input("Enter something: ")) != "quit":
    print(f"You entered: {line}")