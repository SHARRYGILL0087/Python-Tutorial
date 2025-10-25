l = [2,53,5,7,52,9]

# idx = 0
# for i in l :
#     print(f"The item number at idx {idx} is {i} ")
#     idx +=1

# ->  Above can be simplefied using enumerate fxn

for idx , item in enumerate(l) :
    print(f"The item number at idx {idx} is {item} ")
