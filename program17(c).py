print("Sum of N numbers")
print("------------------")

sn = int(input("Enter the starting number: "))
en = int(input("Enter the ending number: "))
d = int(input("Enter the difference: "))

print("Result:", end=" ")
count = 0
total_sum = 0

for i in range(sn, en + 1, d):
    if count > 0:
        print("+", end=" ")
    print(i, end=" ")
    total_sum += i
    count += 1

print()  

print("Sum value  :", total_sum)
print("Count value:", count)
