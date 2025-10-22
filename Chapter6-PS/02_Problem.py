m1 = int(input("Enter marks of Subject 1 : "))
m2 = int(input("Enter marks of Subject 2 : "))
m3 = int(input("Enter marks of Subject 3 : "))


if(m1<33 or m2<33 or m3<33) : 
    print("Fail")

else :
    total = (m1+m2+m3)/300*100
    if(total < 40) : 
        print("Fail")
    else : 
        print("You are Pass : " , total,"%")

print("End Of Program")