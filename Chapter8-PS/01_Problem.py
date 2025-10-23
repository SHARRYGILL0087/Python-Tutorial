def greatest(a , b , c) :
    if(a>b and b>c) :
        return a
    elif (b>a and a>c) :
        return b
    else : return c

a = int(input("Enter a - "))
b = int(input("Enter b - "))
c = int(input("Enter c - "))

ans = greatest(a,b,c)
print(f"The greatest is {ans}")

