print("Factoreial program")
print("-------------------")
n=int(input("Enter the number :"))
fact=1
for i in range(1, n + 1):
    fact=fact * i

print("factorial of", n, "is",fact)
