print("Sum of N numbers")
print("----------------")

n=int(input("Enter the number:"))

sum=0
print("Result")
for i in range(1, n + 1):
    print("+", i, end=" ")
    sum+= i
    
print("\nSum of first", n,"numbers is:",sum)
