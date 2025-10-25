# Super -> use to call the constuctor of parent class 

class Employee : 
    name =  "Sharry"
    def __init__(self):
        print("Constructor of Employee")
        # self.name = name        
        # self.salary = salary

class Programmer(Employee) : 
    role = "Developer"
    def __init__(self):
        print("Constructor of Programmer")


class Manager(Programmer) : 
    salary = 100000
    def __init__(self):
        super().__init__ # Now Constuctor of parent class also called 
        print("Constructor of Manager")


c = Manager()

print(c.name , c.role , c.salary)
