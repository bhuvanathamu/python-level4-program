print("Sum of N numbers")
print("-----------------")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

sum = 0
print("Result:")
for i in range(start, end + 1):
    print(i, end=" ")
    sum += i

print("\nSum of values is:", sum)

    
