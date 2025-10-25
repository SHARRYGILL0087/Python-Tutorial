# Parent1 + Parent2 = Child 
#Two Base classes -> One Derived Class

class Employee :  # Base Class
    company = "ICT"
    def __init__(self,name,salary):
        self.name = name        
        self.salary = salary

    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

class Codder :
    lang = "Python"
    def printLanguage(self) :
        print(f"Your language is {self.lang}")
 
class Programmer(Employee , Codder) : # Derived Class
    company = "ICT Infotech"
    def showlanguage(self) :
        print(f"The language is {self.lang}")



b = Programmer("Sharry" , 9000000)
b.printLanguage()
print(b.lang)



