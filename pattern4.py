#Declaring a variable to which the user inputs the number of rows
r=int(input("Enter the number of rows : "))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print(" ")
