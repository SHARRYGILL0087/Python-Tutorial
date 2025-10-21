my_tuple = (10, 20, 30, 20, 40)
print("Tuple:", my_tuple)

# 🎯 Basic Tuple Methods
# -----------------------------

# 1️⃣ count() -> counts how many times a value appears
count_20 = my_tuple.count(20)
print("Count of 20:", count_20)

# 2️⃣ index() -> returns the index of the first occurrence
index_30 = my_tuple.index(30)
print("Index of 30:", index_30)

# 🧩 Useful Built-in Functions
# -----------------------------

print("Length:", len(my_tuple))      # number of elements
print("Max value:", max(my_tuple))   # maximum element
print("Min value:", min(my_tuple))   # minimum element
print("Sum:", sum(my_tuple))         # sum of all elements
print("Sorted (as list):", sorted(my_tuple))  # returns a sorted list
print("Any True?:", any(my_tuple))   # True if any non-zero or True value
print("All True?:", all(my_tuple))   # True if all are non-zero or True