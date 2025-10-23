'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1, 0, 1])
youDict = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}

you = input("Enter Your Choice - ")
youNum = youDict.get(you)
reverseDict = { 1 : "Snake" , -1 : "Water" , 0 : "Gun"}

print(f"You Choose {reverseDict[youNum]} \nComputer Choose {reverseDict[computer]}")

if(computer==youNum): print("Its a Draw")

else : 
    if((computer-youNum) == 2 or (computer-youNum) == -1 ) :
        print("you Lose!")
    else : 
        print("You Win!")