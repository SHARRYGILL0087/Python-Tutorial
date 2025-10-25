n = int(input("Enter n - "))

l = [i*n for i in range(1,11)]

# print(l)

with open("table.txt" , "a") as f :
    f.write(str(l) + "\n")
