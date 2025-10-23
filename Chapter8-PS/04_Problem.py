def sum(n) :
    if(n==1) : return 1
    if(n==0) : return 0 

    return n + sum(n-1)

n = int(input("Enter n - "))

ans = sum(n)

print("Sum is:",ans)

