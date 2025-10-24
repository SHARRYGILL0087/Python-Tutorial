class Employee : 
    name = "Sharry"  # class attributes
    language = "Py"
    salary = 1200000

    def getInfo(self) :
        print(f"The language is {self.language}.The salary is {self.salary}")

    def greet(self) :
        print("Good Morning!")

    @staticmethod # use when method not need self parameter
    def bye() :
        print("Good Bye!!")


sharry = Employee() # Object
sharry.language = "Java"

sharry.getInfo() # sharry.getInfo(sharry) -> By default 
sharry.greet()
sharry.bye()
print(sharry.name ,  sharry.language)