s = input("Enter any statement : ")
vowels =['a','e','i','o','u']
m=[]
for x in s:
   if (x in vowels and x not in m):
      m.append(x)
print("Vowels present in given statement : ",m)