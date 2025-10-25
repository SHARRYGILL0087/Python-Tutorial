
try :
    a = int(input("Enter Your marks : "))

except ValueError as v : # if error in try
    print("ValueError  : " , v)

else :  # if not error in try
    print("I am inside else")