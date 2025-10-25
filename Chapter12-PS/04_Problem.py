a = int(input("Enter a - "))
b = int(input("Enter b - "))

try : 
    print(f"The division of a and b is {a/b}")

except ZeroDivisionError as e :
    print("Infinity")