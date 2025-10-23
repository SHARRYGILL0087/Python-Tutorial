
with open("poems.txt") as f : 
    a = f.read()
    
    if ("twinkle" in a) :
        print("twinkle present in poems.txt")
    else : print("twinkle not present in poems.txt")