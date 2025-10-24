class Programmer :
    company = "Microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode


p = Programmer("Sharry",10000000,125076)

print(p.name,p.salary,p.pincode)


r= Programmer("Rohan",100000,125023)

print(r.name,r.salary,r.pincode)