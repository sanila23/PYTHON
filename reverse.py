#To find the reverse of a number
n=int(input("Enter the number:"))
i=0
r=0
z=0
while(n!=0):
    z=n%10
    r=(r*10)+z
    n=n//10
print("The reversed number is",r)