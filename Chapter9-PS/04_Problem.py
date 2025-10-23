cont = ""

with open ("file.txt") as f : 
    cont = f.read() 

with open ("file.txt" , "w") as f : 
    newCont =  cont.replace("donkey" , "#####")
    f.write(newCont)
    