from random import randint

class Train : 

    def __init__(slf,train_no):
        slf.train_no = train_no

    def book(slf,fro,to):
        print(f"Tickit is booked in train no :  {slf.train_no} from {fro} to {to}")

    def getStatus(slf ) :
        print(f"Train no :  {slf.train_no} is running successfully ")


    def getFare(slf , fro , to) :
        print(f"Tickit fare in train no :  {slf.train_no} from {fro} to {to} is {randint(222,5552)}")


t = Train(1231)

t.book("Delhi" ,"Mumbai")
t.getFare("Delhi" ,"Mumbai")
t.getStatus()