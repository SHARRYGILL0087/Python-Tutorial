a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

if(b==0):
    raise ZeroDivisionError("first number cannot be devided by 0")

else : 
    print(f"The division of a and b i {a/b}")

