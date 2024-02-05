#program to convert camelcase into snakecase

#input form the user
camel = input("camelCase: ")
#print result
print("snake_case: " , end="")

#loop to scan letters
for l in camel:
     #condition
     if l.isupper():
           print("_"+ l.lower(), end="")
     else:
          print(l, end="")

#to end next line
print()

