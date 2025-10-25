class Employee : 
    a = 34

    @classmethod
    def show(cls) :
        print(f"The instance value of a is {cls.a}")

b = Employee()
b.a = 23

b.show()
