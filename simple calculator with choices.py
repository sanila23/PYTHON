#To find a simple calculator using elif ladder
n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
print("Enter your choice as 1)Addition 2)Subtraction 3)Multiplication 4)Division.")
choice=int(input("Enter the choice:"))
if(choice==1):
    o=n+m
    print(o)
elif(choice==2):
    o=n-m
    print(o)
elif(choice==3):
    o=n*m
    print(o)
elif (choice==4):
    o=n/m
    print(o)