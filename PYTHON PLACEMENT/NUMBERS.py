x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y and x >= z:
    print("x is max")
elif y >= x and y >= z:
    print("y is max")
else:
    print("z is max")
