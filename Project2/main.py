from random import randint

n = randint(0,100)


a = int(input("Enter Your Guess - "))
print(n)

guess = 1

while(a!=n) :
    if(a<n) : 
        a = int(input("Please Guess a Higher Number - "))
    else :
         a = int(input("Please Guess a Lower Number - "))
    guess += 1

print(f"Corrent Answer in {guess} attempts")