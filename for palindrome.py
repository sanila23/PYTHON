#To find a palindome number using for loop
num=int(input("Enter a number:"))
rev=num
sum = 0
temp = str(num)
x = len(temp)
for i in range(0,x):
    r=num%10
    sum=sum*10+r
    num=num//10
if(rev==sum):
    print("The number", rev, "is a palindrome!")
else:
    print("The number",rev, "is not palindrome!")