class Employee : 
    a = 34

    @classmethod
    def show(cls) :
        print(f"The instance value of a is {cls.a}")

    # @property
    # def name(self) :
    #     return  self.ename
    
    # @name.setter
    # def name(self,value) :
        # self.ename = value

    @property
    def name(self) :
        return  f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value) :
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

b = Employee()
b.a = 23

b.show()

b.name = "Sharry Gill"

print(b.fname, 34 , b.lname)
