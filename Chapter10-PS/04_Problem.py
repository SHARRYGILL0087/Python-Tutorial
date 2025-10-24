class Calculator : 
    def __init__(self,num):
        self.num = num

    def square(self) :
        return self.num * self.num

    def cube(self) :
        return self.num * self.num * self.num

    def squareRoot(self) :
        return self.num ** 0.5
    
    @staticmethod
    def hello():
        print("Hello !!")
    
    

n = int(input("Enter a number - "))

c = Calculator(n)

sq = c.square()
cb = c.cube()
sqr = c.squareRoot()

c.hello()

print(sq,cb,sqr)