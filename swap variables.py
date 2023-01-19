#To swap 2 variables
u=int(input("Enter the variable of u:"))
v=int(input("Enter the variable of v:"))
print("Before swapping the variables:",(u,v))
#Swapping of 2 variables using an outside variable.Let us consider it as w
w=u
u=v
v=w
print("After swapping the variables:",(u,v))