#To find the sum of odd and even numbers
s=int(input("Enter the limit:"))
x=1
r=0
while(x<=10):
    if(x%2==1):
      r=r+x
    x=x+1
print("The sum of odd number=",r)

u=1
v=0
while(u<=10):
    if(u%2==0):
      v=v+u
    u=u+1
print("The sum of even numbers=",v)