class Employee : 
    name = "Sharry"  # class attributes
    language = "Py"
    salary = 1200000

    def __init__(self , name , salary , language): # dunder method which is automatically call
        self.name = name
        self.salary = salary
        self.language = language

        print("creating an object")

    def getInfo(self) :
        print(f"The language is {self.language}.The salary is {self.salary}")

    def greet(self) :
        print("Good Morning!")

    @staticmethod 
    def bye() :
        print("Good Bye!!")


sharry = Employee("Sharry_Gill" , 99999999 , "JavaScript") # Object
# sharry.language = "Java"

# sharry.getInfo() 
# sharry.greet()
# sharry.bye()
print(sharry.name ,  sharry.language)

rohan = Employee("Rohan" , 23 , "Py")