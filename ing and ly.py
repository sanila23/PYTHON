#Declaring a variable to which the user inputs the required string
Str=input("Enter the required word ending with either 'ing' or 'ly' : ")
if(Str[-3:]=="ing"):
    Str=Str+"ly"
    print(Str)
else:
    Str = Str + "ing"
    print(Str)