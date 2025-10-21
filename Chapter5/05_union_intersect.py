s1 = {1,2,4,5}
s2 = {2,6,7,8,5}

print(s1.union(s2))
print(s1.intersection(s2)) 

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # Union -> {1, 2, 3, 4, 5, 6}
print(a & b)   # Intersection -> {3, 4}
print(a - b)   # Difference -> {1, 2}
print(a ^ b)   # Symmetric difference -> {1, 2, 5, 6}