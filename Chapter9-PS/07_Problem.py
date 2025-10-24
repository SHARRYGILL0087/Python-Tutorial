i = 1

with open ("log.txt") as f : 
    line = f.readline()
    while(not "python" in line) :
        line = f.readline()
        i += 1
    
print(i)