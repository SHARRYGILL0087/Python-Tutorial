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

if(computer==youNum) :
    print("Its a Draw")

elif(computer == -1 and youNum == 1) :
    print("You Win!")

elif (computer == -1 and youNum == 0) :
    print("You Lose!")

elif (computer==1 and youNum == -1) :
    print("You Lose!")

elif (computer == 1 and youNum == 0 ):
    print("You Win!")

elif (computer == 0 and youNum == 1) :
    print("You Lose!")

elif (computer == 0 and youNum == -1) :
    print("You Win!")

else : 
    print("Something Went Wrong!")