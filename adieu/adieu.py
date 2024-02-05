#import packge
import inflect
p = inflect.engine()

#create empty list
mylist = []

#loop to store value in loop
while True:
    try:
       mylist.append(input("Name: "))

    except EOFError:
        print()
        break
#print list with infliect packge
print("Adieu, adieu, to " +  p.join(mylist))