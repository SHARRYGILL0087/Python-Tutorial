try :
    with open("1.txt") as f:
        print(f.read())

except Exception as e :
    print("1.txt not found")

    
try :
    with open("2.txt") as f:
        print(f.read())

except Exception as e :
    print("2.txt not found")

try :
    with open("3.txt") as f:
        print(f.read())

except Exception as e :
    print("3.txt not found")

