class Vector : 
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"Vector : {self.i}i + {self.j}j + {self.k}k "
    

v1 = Vector(1,2,3)

v2 = Vector(4,5,6)

print(v1,v2)
    
