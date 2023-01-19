#To check whether the number is palindrome or not
r=int(input("Enter a number:"))
k=r
Reverse=0
h=0
while(r!=0):
    h=r%10
    Reverse=Reverse*10+h
    r=r//10
if(Reverse==k):
    print(Reverse,"is a palindrome number.")
else:
    print(Reverse,"is not a palindrome number.")