#program to add food amount
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
price = 0 #initialisation
#loop for adding cost
while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            price += menu[item] #updation
            print("Total: ${:.2f}".format(price),  sep="")
#break when face eoferror !!
    except EOFError:
        break