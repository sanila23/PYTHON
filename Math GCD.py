x = int(input("Type the first number : "))
y = int(input("Type the second number : "))
while y != 0:
    r = x % y
    x = y
    y = r
print("The GCD of the numbers is", x)