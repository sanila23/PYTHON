m=input("Enter the message:")
mylist =list(m)
mylist = [ord(character) + 1 for character in mylist]
print(mylist)