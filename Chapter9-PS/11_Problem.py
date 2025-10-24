with open ("old.txt") as f :
    cont1 = f.read()


with open("renamed_by_python.txt" , "w") as f : 
    f.write(cont1)