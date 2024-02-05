# creata a program to ques ans..

#input to the user
x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

#condition statement
if  x.strip() == "42" or x.lower().strip() == "forty-two" or x.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")

