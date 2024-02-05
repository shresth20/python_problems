#create calculater program
# input from user
expression =input("Expression: ")

x, y, z = expression.split(" ")
new_x = float(x)
new_z = float(z)

#condition statement
if y == '+':
    print(new_x + new_z)

elif y == '-':
    print(new_x - new_z)

elif y == '/':
    print(new_x / new_z)

elif y == '*':
    print(new_x * new_z)

else:
    print("Invalid")






