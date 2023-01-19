m=int(input("Enter the sum of first names:"))
count=0
for i in range(m):
    n=input("Enter the name:")
    count=count+n.count('a');
    print(count)