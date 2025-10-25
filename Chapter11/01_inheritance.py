class Employee :  # Base Class
    company = "ICT"
    def __init__(self,name,salary):
        self.name = name        
        self.salary = salary

    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

 
class Programmer(Employee) : # Derived Class
    company = "ICT Infotech"
    # def __init__(self,name,salary):
    #     self.name = name        
    #     self.salary = salary

    def showlanguage(self) :
        print(f"The language is {self.language}")


a = Employee("Sharry" , 1222222)
b = Programmer("Shamsher" , 1222999)

a.show()
b.show()

print(a.company,b.company)