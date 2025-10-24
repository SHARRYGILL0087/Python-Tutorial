
with open ("this.txt") as f :
    txt = f.read()


with open("copy.txt" , "w") as f : 
    f.write(txt)