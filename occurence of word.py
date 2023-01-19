s=input("Enter the string:")
u=input("Occurence of a word in a string:")
count=0
splt=s.split(" ")
for i in splt:
    if(i==u):
        count=count+1
print("The count is ",count)