from random import randint

class Train : 

    def __init__(self,train_no):
        self.train_no = train_no

    def book(self,fro,to):
        print(f"Tickit is booked in train no :  {self.train_no} from {fro} to {to}")

    def getStatus(self ) :
        print(f"Train no :  {self.train_no} is running successfully ")


    def getFare(self , fro , to) :
        print(f"Tickit fare in train no :  {self.train_no} from {fro} to {to} is {randint(222,5552)}")


t = Train(1231)

t.book("Delhi" ,"Mumbai")
t.getFare("Delhi" ,"Mumbai")
t.getStatus()