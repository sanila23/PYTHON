#To find the fibonacci series
n=int(input("Enter a limit:"))
m=0
o=1
s=1
c=1
print("Fibonacci series:\t")
while(c<=n):
    c=c+1
    print(m)
    m=o
    o=s
    s=m+o