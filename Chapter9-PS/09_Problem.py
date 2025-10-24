with open ("this.txt") as f :
    cont1 = f.read()


with open ("copy.txt") as f :
    cont2 = f.read()


if(cont1==cont2) :
    print("Same COntent")

else : print("Contant Not Match")