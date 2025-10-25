# Parent -> Child1 -> Child2
# One Base class of Derived Class(Child1) -> and child1 became Base class (Parent) of Child2 (Another Derived Class)

class Employee : 
    name =  "Sharry"

class Programmer(Employee) : 
    role = "Developer"

class Manager(Programmer) : 
    salary = 100000

c = Manager()

print(c.name , c.role , c.salary)
