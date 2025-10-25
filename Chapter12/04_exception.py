
try :
    a = int(input("Enter Your marks : "))

except ValueError as v :
    print("ValueError  : " , v)

except Exception as e :
    print("Error - " , e)
    print("Please Enter a valid marks !!")