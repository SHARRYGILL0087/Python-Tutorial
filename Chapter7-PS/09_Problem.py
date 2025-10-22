'''
* * *
*   *   for n = 3
* * *
'''

n = int(input("Enter n - "))

for i in range(1,n+1) : 
    if (i==1 or i==n) : print("*" * n)
    else : print(f"*{" " * (n-2)}*")

# print("*" * n)

# for i in range(1,n-1) :
#     print("*" , end="")
#     print(" " * (n-2), end="" )
#     print("*")

# print("*" * n)