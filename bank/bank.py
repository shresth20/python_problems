#input form the user
x = input("Greeting: ")

#condition statement
if "hello" in x.lower().strip():
    print("$0")

elif "h" == x.lower().strip()[0]:
    print("$20")

else:
    print("$100")