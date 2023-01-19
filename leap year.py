y1 = int(input("Enter current year:"))
y2 = int(input("Enter final year:"))
print("The leap years are ")
for year in (range(y1 , y2)):
   if(year%4==0)and(year%100!=0)or(year%400==0):
      print(year)