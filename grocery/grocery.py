#program to basket list

#empty dir..
grocery = {}

#loop to store item in grocery dir..
while True:
    try:
        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1

    #when face error print result and break loop
    except EOFError:
        for element in sorted(grocery.keys()):
            print(grocery[element], element)
        break

