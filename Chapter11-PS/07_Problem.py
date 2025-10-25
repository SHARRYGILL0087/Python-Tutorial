class Vector : 
    def __init__(self,l):
        self.i ,self.j,self.k = l
    
    def __str__(self):
        return f"Vector : {self.i}i + {self.j}j + {self.k}k "
    
    def __len__(self):
        # Return the magnitude as an integer (optional: round or cast)
        magnitude = (self.i**2 + self.j**2 + self.k**2) ** 0.5
        return int(magnitude)  # or return magnitude if you want float

v1 = Vector([1,2,3])

v2 = Vector([4,5,6])

print(v1,v2)

print(len(v1))
    
