
with open ("log.txt") as f : 
    cont = f.read()


if("python" in  cont) : print("Python present in log.txt")
else : print("Python not present")
    
    