#Declaring a variable to which the user inputs the required string
Str=input("Enter the required string : ")
Chr=Str[0]
Chr1=Str[0].lower()
Str=Str.replace(Chr,'$')
Str=Str.replace(Chr1,'$')
Str1=Chr+Str[1:]
print(Str1)
