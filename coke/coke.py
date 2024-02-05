#program to sell coke in 50 cents
#define var..
price = 50

#create loop
while price > 0:
    print("Amount Due:",price)
    cent = int(input("Insert Coin: "))

    #create condition
    if cent in [25, 10, 5]:
        price -= cent

#print result
print("Change Owed:",abs(price))
