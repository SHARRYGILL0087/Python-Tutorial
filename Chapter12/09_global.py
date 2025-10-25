a = 200
def fun() :
    global a 
    a = 34
    print(a)

a=343
fun()
print(a)