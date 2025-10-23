
def remove(l , word) :
    n  = []
    for item in l :
       if not(item==word):
           n.append(item.strip(word))
    return n
    
l = ["Sharry" , "Shamsher" , "SSG" , "SharryGill"]

ans = remove(l,"SSG")
print(ans)

