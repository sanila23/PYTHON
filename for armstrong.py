#To find the armstrong number using for loop
num = int(input("Enter a three digit number:"))
sum = 0
temp = num
for i in range(0,num):
    r=num%10
    sum = r * r * r + sum
    num=num//10
if(sum==temp):
    print("Number is amstrong!")
else:
    print("Number is not amstrong")