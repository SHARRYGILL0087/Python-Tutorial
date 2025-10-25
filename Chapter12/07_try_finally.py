def main() :
    try :
        a = int(input("Enter Your marks : "))
        return 

    except ValueError as v : # if error in try
        print("ValueError  : " , v)
        return

    finally :  # Always run if err or not err even after return
        print("I am inside finally")


main()