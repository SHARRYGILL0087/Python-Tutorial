class demo :
    a = "Sharry"


s = demo()
print(s.a) # Sharry

s.a = "SSG" # Not change the class attribute but set a instance attribute

print(s.a) # SSG
print(demo.a) # Sharry 