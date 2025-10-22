a = int(input("Enter a - "))

fact = 1

for i in range(1,a+1) :
    fact *= i

print(f"The factorial of {a} is {fact} ")