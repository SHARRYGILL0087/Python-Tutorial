words = ["donkey" , "bad" , "dirty" , "damn"]
newCont = ""

def censor_words(cont = "") :
    for i in words : 
        if(i in cont) :
           print(i)
           cont = cont.replace(i,"#"*len(i))
    return cont


with open ("file.txt") as f : 
    cont = f.read() 
    # print(cont)
    newCont = censor_words(cont)
    # print(newCont)
    

with open ("file.txt" , "w") as f : 
    f.write(newCont)
    