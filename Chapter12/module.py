def myworld() :
    print("Hello World")

myworld()

print(__name__)

if __name__ == "__main__" : # if this code is directly executed by running the file it present in
    print("we are directly running this code")
else : 
    print("we are running this code from 08_main.py")
