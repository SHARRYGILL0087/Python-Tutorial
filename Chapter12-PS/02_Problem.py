l = [1,42,5,53,674,234,63,12,64]

for idx , item in enumerate(l) :
    if(idx + 1 == 3 or idx + 1 == 5 or idx + 1 == 7) :
        print(item)