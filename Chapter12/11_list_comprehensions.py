myList = [3,5,6,7,2,1,21]

# sqList = []

# for item in myList : 
#     sqList.append(item*item)

# print(sqList)

# ->  using comprehension

sqList = [i*i for i in myList]

print(sqList)