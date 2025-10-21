s = {1 , 2 , 3 , 4 , 33 , 64 , 23 , 65 , 11 , 35 , 3, 0 , 1 , 2}

# print(s,type(s))

s.add(99)
print(s)

s.remove(99) # Give err if ele not found
print(s)

s.discard(33) # GIve No err if ele not found
print(s)

s.update([22,44,55])
print(s)

new_set = s.copy()
print(f"new set ->  {new_set}")

s.clear() 
print(s)