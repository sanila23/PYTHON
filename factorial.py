#To find the factorial of a number
w=int(input("Enter the number:"))
factorial=1
x=1
while(x<=w):
    factorial=factorial*x
    x=x+1
print("Factorial of",w,"is",factorial)