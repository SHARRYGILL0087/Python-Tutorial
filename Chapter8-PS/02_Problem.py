
def covertToC(f) :
    c = 5*(f-32)/9
    return c


f = int(input("Enter temperature in f : "))

ans = covertToC(f)

print("Temperature in C is :" , ans)