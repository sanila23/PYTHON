#To find the sum of digits.
n=int(input("Enter the number:"))
sum=0
while(n!=0):
    m=int(n%10)
    sum=sum+m
    n=n/10
print("The sum of digits is ",sum)