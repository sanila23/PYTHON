#To check whether the number is armstrong or not
r=int(input("Enter the number:"))
k=r
rem=0
i=0
h=0
while(r!=0):
    rem=r%10
    rem=rem*rem*rem
    h=h+rem
    r=r//10
if(k==h):
    print(h,"is an Armstrong number.")
else:
    print(h,"is not a Amstrong number.")