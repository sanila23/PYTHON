#To find the sum of given numbers
lst=[]
num=int(input('how many numbers:'))
for i in range(num):
    numbers=int(input("enter the number="))
    lst.append(numbers)
print("sum of the element in given list is:",sum(lst))