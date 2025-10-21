# 🔄 Tuple Operations
# -----------------------------
my_tuple = (10, 20, 30, 20, 40)
print("Tuple:", my_tuple)
t1 = (1, 2)
t2 = (3, 4)

# Concatenation
combined = t1 + t2
print("Concatenated Tuple:", combined)

# Repetition
repeated = t1 * 3
print("Repeated Tuple:", repeated)

# Membership
print("Is 2 in tuple?", 2 in t1)
print("Is 5 not in tuple?", 5 not in t1)

# Slicing
print("Sliced Tuple:", my_tuple[1:4])

# Unpacking
a, b, c = (100, 200, 300)
print("Unpacked Values:", a, b, c)

# -----------------------------
# 🔁 Tuple Conversion
# -----------------------------

list_data = [1, 2, 3, 4]
converted = tuple(list_data)
print("Converted from list:", converted)