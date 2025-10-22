a = int(input("Enter a -> "))
b = int(input("Enter b -> "))
c = int(input("Enter c -> "))
d = int(input("Enter d -> "))

if(a>b and a>c and a>d) : print("a is Greatest")
elif(b>a and b>c and b>d) : print("b is Greatest")
elif(c>a and a>c and a>d) : print("c is Greatest")
else : print("d is Greatest")