#To find reverse of a number using for loop
num = int(input("Enter a number: "))
rev = num
temp = str(num)
x = len(temp)
sm = 0
for i in range(0,x):
    r = num % 10
    sm = sm * 10 + r
    num = num // 10
print( "The reverse of number", rev, "is", sm)